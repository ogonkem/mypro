# Generated by Django 3.2.13 on 2022-04-24 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectrequirements',
            name='product',
            field=models.CharField(choices=[('', 'Choose your product'), ('Ecommerce', 'Ecommerce'), ('Social Media', 'Social Media'), ('SAAS', 'SAAS'), ('Search Engine', 'Search Engine'), ('Fintech', 'fintech'), ('others', 'Others')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='targetaudience',
            name='target_name',
            field=models.CharField(choices=[('', 'Choose target_name'), ('Male', 'Male'), ('Female', 'Female'), ('Upper Class', 'Upper Class'), ('Middle Class', 'Middle Class'), ('18 to 45', '18 to 45'), ('45 to 64', '45 to 64')], default=0, max_length=50),
        ),
    ]