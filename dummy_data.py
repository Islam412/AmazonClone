import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from faker import Faker
import random
from product.models import Brand , Product



def seed_brand(n):
    fake = Faker()
    image = ['1.jpg','2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpg','9.jpg','10.jpeg','11.jpeg','12.jpeg','13.jpeg','14.jpeg','15.jpeg','16.jpeg','17.jpg','18.jpg','19.jpg','20.jpg','21.png','22.jpg','23.jpg','24.jpg','25.jpg','26.jpg','27.jpg','28.jpg','29.jpg','30.jpg','31.jpg','32.jpg','33.jpg','34.jpeg','35.jpg','36.jpg','37.png','38.png','39.jpg','40.jpg','41.png','42.jpg','43.png']
    for _ in range(n):
        Brand.objects.create(
            name=fake.name() ,
            image = f'brands/{image[random.randint(0,44)]}'
        )
    print(f'Seed {n} Brands Successfully')




def seed_product(n):
    pass








seed_brand(5)
#seed_product(5)