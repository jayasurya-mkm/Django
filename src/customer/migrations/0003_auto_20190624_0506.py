# Generated by Django 2.2.2 on 2019-06-24 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20190512_0616'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='Designation',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='description',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='userID',
        ),
        migrations.AddField(
            model_name='customer',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customer',
            name='age',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(default='', max_length=70),
        ),
    ]
