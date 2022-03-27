from django.db import models

class ProductUnit(models.Model):
    name_singular = models.CharField('Nazwa - lp',max_length=20)
    name_plural = models.CharField('Nazwa - lm', max_length=20)
    symbol = models.CharField(max_length=5)

    class Meta:
        verbose_name = 'Jednostka'
        verbose_name_plural = 'Jednostki'

    def __str__(self):
        return f'{self.symbol} - {self.name_singular}'

class ProductCategory(models.Model):
    name = models.CharField(
                'Kategoria',
                max_length=100,
                unique=True)

    class Meta:
        verbose_name = 'Kategoria'
        verbose_name_plural = 'Kategorie'

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField('Nazwa', max_length=100)
    amount = models.PositiveIntegerField('Ilość')
    categories = models.ManyToManyField(
                ProductCategory,
                verbose_name='Kategorie',
                related_name='products')

    class Meta:
        verbose_name = 'Produkt'
        verbose_name_plural = 'Produkty'
    
    def __str__(self):
        return self.name

class ProductVariant(models.Model):
    amount = models.PositiveSmallIntegerField('Ilość')
    price = models.PositiveSmallIntegerField('Cena')
    product = models.ForeignKey(
                Product,
                on_delete=models.CASCADE,
                related_name='variants')
    unit = models.ForeignKey(
                ProductUnit,
                verbose_name='Jednostka',
                on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Wariant'
        verbose_name_plural = 'Warianty'

    def __str__(self):
        name = f'{self.product} - {self.amount} x {self.price}'
        return name

class ProductPhoto(models.Model):
    height = models.PositiveSmallIntegerField('Wysokość')
    width = models.PositiveSmallIntegerField('Szerokość')
    photo = models.ImageField(
                verbose_name='Zdjęcie',
                upload_to='product_photos/',
                height_field='height',
                width_field='width')
    product = models.ForeignKey(
                Product,
                verbose_name='Produkt',
                on_delete=models.CASCADE,
                related_name='photos')

    class Meta:
        verbose_name = 'Zdjęcie'
        verbose_name_plural = 'Zdjęcia'


    def __str__(self):
        return f'{self.product} - {self.photo}'
