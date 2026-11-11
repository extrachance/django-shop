from decimal import Decimal

from django.core.management.base import BaseCommand
from django.utils.text import slugify

from shop.models import Category, Product

# (name, price, old_price, stock, is_popular, description)
DATA = {
    'furniture': [
        ('Corner Sofa Milan', '32000', '38000', 5, True,
         'Spacious corner sofa with soft fabric upholstery and a solid '
         'wooden frame. Comfortably seats up to five people.'),
        ('Oak Dining Table', '18500', None, 3, False,
         'Solid oak dining table with a natural finish and rounded edges. '
         'Seats six people.'),
        ('Ergonomic Office Chair', '9800', '11500', 0, False,
         'Office chair with adjustable height, lumbar support and a '
         'breathable mesh back for long working days.'),
    ],
    'household appliances': [
        ('Robot Vacuum Cleaner', '21000', '25000', 8, True,
         'Robot vacuum with smart room mapping, automatic charging and '
         'up to 120 minutes of cleaning on a single charge.'),
        ('Electric Kettle 1.7 L', '1900', None, 25, False,
         'Stainless steel electric kettle with automatic shut-off and '
         'boil-dry protection.'),
        ('Built-in Oven 60 cm', '45300', '49900', 2, True,
         'Built-in electric oven with a convection fan, digital timer and '
         'a self-cleaning enamel interior.'),
    ],
    'technic': [
        ('Wireless Headphones', '3900', '4500', 15, True,
         'Over-ear Bluetooth headphones with active noise cancellation '
         'and up to 30 hours of battery life.'),
        ('Smart Speaker', '5200', None, 10, False,
         'Compact smart speaker with a built-in voice assistant, rich '
         'sound and Wi-Fi connectivity.'),
        ('Power Bank 20000 mAh', '2400', '2900', 30, False,
         'High-capacity power bank with fast charging, two USB-A ports '
         'and one USB-C port.'),
    ],
}


class Command(BaseCommand):
    help = 'Fill the database with demo products'

    def handle(self, *args, **options):
        for cat_name, items in DATA.items():
            category, _ = Category.objects.get_or_create(
                name=cat_name, defaults={'slug': slugify(cat_name)})
            for name, price, old_price, stock, popular, description in items:
                Product.objects.update_or_create(
                    slug=slugify(name),
                    defaults={
                        'category': category,
                        'name': name,
                        'description': description,
                        'price': Decimal(price),
                        'old_price': Decimal(old_price) if old_price else None,
                        'stock': stock,
                        'is_popular': popular,
                        'active': True,
                    },
                )
        self.stdout.write(self.style.SUCCESS('Demo products created'))