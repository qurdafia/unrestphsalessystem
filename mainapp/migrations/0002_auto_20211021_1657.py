# Generated by Django 3.2.8 on 2021-10-21 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='description',
            field=models.TextField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='order',
            name='height_inches',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='width_inches',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
