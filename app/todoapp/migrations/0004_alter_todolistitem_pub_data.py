# Generated by Django 4.1.1 on 2022-09-29 15:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0003_alter_todolistitem_pub_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolistitem',
            name='pub_data',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
