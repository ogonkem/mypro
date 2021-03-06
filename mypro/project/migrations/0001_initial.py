# Generated by Django 3.2.13 on 2022-04-23 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TargetAudience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_name', models.CharField(choices=[(0, 'Choose target_name'), ('Male', 'Male'), ('Female', 'Female'), ('Upper Class', 'Upper Class'), ('Middle Class', 'Middle Class'), ('18 to 45', '18 to 45'), ('45 to 64', '45 to 64')], default=0, max_length=50)),
            ],
            options={
                'verbose_name': 'TargetAudience',
                'verbose_name_plural': 'TargetAudience',
            },
        ),
        migrations.CreateModel(
            name='ProjectRequirements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(choices=[(0, 'Choose your product'), ('Ecommerce', 'Ecommerce'), ('Social Media', 'Social Media'), ('SAAS', 'SAAS'), ('Search Engine', 'Search Engine'), ('Fintech', 'fintech'), ('others', 'Others')], default=0, max_length=100)),
                ('solution_description', models.TextField(max_length=500)),
                ('code_language_preference', models.BooleanField(default=False)),
                ('code_language', models.CharField(max_length=50)),
                ('have_buildups', models.BooleanField(default=False)),
                ('buildups', models.FileField(upload_to='uploads/buildups')),
                ('have_design_elements', models.BooleanField(default=False)),
                ('design_elements', models.FileField(upload_to='uploads/design_elements')),
                ('project_target', models.ManyToManyField(to='project.TargetAudience')),
            ],
            options={
                'verbose_name': 'ProjectRequirements',
                'verbose_name_plural': 'ProjectRequirements',
            },
        ),
    ]
