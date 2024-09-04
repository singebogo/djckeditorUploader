from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class SPUModel(models.Model):
    '''这是spu表格'''
    name = models.CharField(max_length=32, verbose_name='商品名')
    sales = models.CharField(max_length=20, verbose_name='销售量')
    desc_pack = RichTextUploadingField(default='', verbose_name='商品详情')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '商品表'
        db_table = verbose_name
        verbose_name_plural = verbose_name