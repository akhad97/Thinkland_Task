from django_elasticsearch_dsl import Document, Index
from ..product.models import Product



product_index = Index("product")
product_index.settings(
    number_of_shards=1,
    number_of_replicas=0,
)

@product_index.doc_type
class ProductDocument(Document):
    """
    A document representing a Product.

    This class is used to define the mapping between the
    `Product` model and the Elasticsearch index.
    It specifies the fields that should be included in the index.
    """

    class Django:
        """
        A nested class representing the Django settings for the `ProductDocument` document.
        """

        model = Product
        fields = ["id", "title"]

