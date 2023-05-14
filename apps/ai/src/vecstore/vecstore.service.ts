import { Injectable } from '@nestjs/common'
import { Milvus } from './milvus'
import { OpenAIEmbeddings } from 'langchain/embeddings/openai'
import { Subscribe } from '@app/rmq/decorator'
import { EntityCreateMsg, EntityRemoveMsg } from '@app/rmq/subscribe'
import {
  PositionType,
  QueryParams,
  PartitionEnum,
  Doc,
  SimSearchParams,
  SearchParams,
} from './schema'
import { EntityType } from '@app/rmq/types'

@Injectable()
export class VecstoreService {
  vecstore: Milvus
  embeddings: OpenAIEmbeddings

  constructor() {
    this.embeddings = new OpenAIEmbeddings({
      modelName: 'text-embedding-ada-002',
    })
    this.vecstore = new Milvus(this.embeddings, {})
  }

  async search(type: EntityType, params: SearchParams, k = 10) {
    return this.vecstore.search({ collection_name: type }, params, k)
  }

  async simSearch(type: EntityType, params: SimSearchParams, k = 10) {
    const vec = (await this.embeddings.embedDocuments([params.query]))[0]
    return this.search(type, { ...params, query: vec }, k)
  }

  async query(position: PositionType, params: QueryParams) {
    return this.vecstore.query(position, params)
  }

  async create(position: PositionType, doc: Doc) {
    return this.vecstore.addDocuments(position, [doc])
  }

  async createMany(position: PositionType, docs: Doc[]) {
    return this.vecstore.addDocuments(position, docs)
  }

  async update(position: PositionType, doc: Doc) {
    await this.vecstore.delete({ collection_name: position.collection_name }, [
      doc.metadata.id,
    ])
    await this.vecstore.addDocuments(position, [doc])
  }

  async updateMany(position: PositionType, docs: Doc[]) {
    await this.vecstore.delete(
      { collection_name: position.collection_name },
      docs.map((doc) => doc.metadata.id)
    )
    await this.vecstore.addDocuments(position, docs)
  }

  async delete(position: PositionType, id: number) {
    return this.vecstore.delete(position, [id])
  }

  async deleteMany(position: PositionType, ids: number[]) {
    return this.vecstore.delete(position, ids)
  }

  @Subscribe('ai_vecstore', 'entity_create')
  protected async handleEntityCreate({
    type,
    ids,
    projectId,
  }: EntityCreateMsg) {
    console.log(type, ids, 'create')

    this.createMany(
      {
        collection_name: type,
        partition_name: PartitionEnum.undone,
      },
      ids.map(
        (id) =>
          new Doc({
            metadata: {
              id,
              projectId,
              updateAt: new Date(),
              desc: '',
            },
            pageContent: ' ',
          })
      )
    )
  }

  @Subscribe('ai_vecstore', 'entity_remove')
  protected async handleEntityRemove({ type, ids }: EntityRemoveMsg) {
    console.log(type, ids, 'remove')
    await this.deleteMany({ collection_name: type }, ids)
  }
}