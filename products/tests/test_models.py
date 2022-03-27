from django.test import TestCase
from products.models import (ProductUnit, ProductCategory,
    Product, ProductVariant)

class ProductUnitTest(TestCase):
    def setUp(self):
        ProductUnit.objects.create(
            name_singular='kilogram',
            name_plural='kilograms',
            symbol='kg')
        ProductUnit.objects.create(
            name_singular='gram',
            name_plural='grams',
            symbol='g')

    def test_str(self):
        kilogram = ProductUnit.objects.get(symbol='kg')
        gram = ProductUnit.objects.get(symbol='g')
        self.assertEqual(str(kilogram), 'kg - kilogram')
        self.assertEqual(str(gram), 'g - gram')

class ProductCategoryTest(TestCase):
    def setUp(self):
        ProductCategory.objects.create(name='fruits')
        ProductCategory.objects.create(name='vegetables')

    def test_str(self):
        fruits = ProductCategory.objects.get(name='fruits')
        vegetables = ProductCategory.objects.get(name='vegetables')
        self.assertEqual(str(fruits), 'fruits')
        self.assertEqual(str(vegetables), 'vegetables')

class ProductTest(TestCase):
    def setUp(self):
        Product.objects.create(name='potato', amount=5000)
        Product.objects.create(name='banana', amount=2500)

    def test_str(self):
        potato = Product.objects.get(name='potato')
        banana = Product.objects.get(name='banana')
        self.assertEqual(str(potato), 'potato')
        self.assertEqual(str(banana), 'banana')

class ProductVariantTest(TestCase):
    def setUp(self):
        potato = Product.objects.create(name='potato', amount=5000)
        banana = Product.objects.create(name='banana', amount=2500)
        kilograms = ProductUnit.objects.create(
                    name_singular='kilogram',
                    name_plural='kilograms',
                    symbol='kg')
        ProductVariant.objects.create(
                    amount=20,
                    price=120,
                    product=banana,
                    unit=kilograms)
        ProductVariant.objects.create(amount=15,
                    price=100,
                    product=potato,
                    unit=kilograms)

    def test_str(self):
        banana_variant = ProductVariant.objects.get(amount=20)
        potato_variant = ProductVariant.objects.get(amount=15)
        self.assertEqual(str(banana_variant), 'banana - 20 x 120')
        self.assertEqual(str(potato_variant), 'potato - 15 x 100')
