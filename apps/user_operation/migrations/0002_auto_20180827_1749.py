# Generated by Django 2.1 on 2018-08-27 17:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('goods', '0001_initial'),
        ('user_operation', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='userleavingmessage',
            name='user',
            field=models.ForeignKey(on_delete=False, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='userfav',
            name='goods',
            field=models.ForeignKey(help_text='商品', on_delete=False, to='goods.Goods', verbose_name='商品'),
        ),
        migrations.AddField(
            model_name='userfav',
            name='user',
            field=models.ForeignKey(on_delete=False, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='useraddress',
            name='user',
            field=models.ForeignKey(on_delete=False, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AlterUniqueTogether(
            name='userfav',
            unique_together={('user', 'goods')},
        ),
    ]
