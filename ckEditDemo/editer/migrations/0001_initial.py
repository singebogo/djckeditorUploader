# Generated by Django 5.1.1 on 2024-09-04 13:12

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SPUModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='商品名')),
                ('sales', models.CharField(max_length=20, verbose_name='销售量')),
                ('desc_pack', ckeditor_uploader.fields.RichTextUploadingField(default='', verbose_name='商品详情')),
            ],
            options={
                'verbose_name': '商品表',
                'verbose_name_plural': '商品表',
                'db_table': '商品表',
            },
        ),
    ]
