# Generated by Django 3.2.9 on 2022-06-30 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0003_delete_detail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=122)),
                ('price', models.CharField(max_length=122)),
                ('image_link', models.CharField(max_length=122)),
            ],
        ),
    ]
