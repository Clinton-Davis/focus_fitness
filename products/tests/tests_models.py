from django.test import TestCase

from products.models import Product


class ProductModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        Product.objects.create(
            name="Product_test",
            description="Product test description",
            price=10,
        )

    def test_product_name(self):
        product = Product.objects.get(id=1)
        self.assertEqual(product.name, "Product_test")

    def test_product_description(self):
        product = Product.objects.get(id=1)
        self.assertEqual(product.description, "Product test description")

    def test_product_has_sizes(self):
        product = Product.objects.get(id=1)
        self.assertEqual(product.has_sizes, False)

    def test_product_in_stock(self):
        product = Product.objects.get(id=1)
        self.assertNotEqual(product.in_stock, False)

    def test_product_display_items(self):
        product = Product.objects.get(id=1)
        self.assertEqual(product.display_items, False)

    def test_get_absolute_url(self):
        product = Product.objects.get(id=1)
        self.assertEquals(product.get_absolute_url(), '/products/1/')
