from django.urls import include, path


urlpatterns = [
    path(
        "user/",
        include(
            ("main.apps.user.urls", "main.apps.user.urls"),
            namespace="user",
        ),
    ),
    path(
        "product/",
        include(
            ("main.apps.product.urls", "main.apps.product.urls"),
            namespace="product",
        ),
    ),
    path(
        "category/",
        include(
            ("main.apps.category.urls", "main.apps.category.urls"),
            namespace="category",
        ),
    )
]

