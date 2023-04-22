from haystack.agents import Tool
from haystack.document_stores import FAISSDocumentStore


class HierarchicalSearchTool(Tool):
    def __init__(self, doc_store: FAISSDocumentStore):
        super().__init__(
            name="hierarchical_search",
            description="",
            pipeline_or_node=None,
            output_variable="json"
        )
