# Generated by Django 3.2.25 on 2024-03-30 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20240329_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='currency',
            field=models.CharField(choices=[('USD', 'USD'), ('ARS', 'ARS')], default='USD', max_length=3),
        ),
    ]
