# Generated by Django 3.2.8 on 2021-10-28 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_alter_expense_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='initial_payment',
            field=models.IntegerField(default=0),
        ),
    ]
