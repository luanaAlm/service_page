# Generated by Django 3.2.8 on 2021-11-12 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_rename_portifolio_portifolio_cliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='portifolio_cliente',
            name='logomarca',
            field=models.ImageField(default=1, upload_to='img_portifolio/%y'),
            preserve_default=False,
        ),
    ]