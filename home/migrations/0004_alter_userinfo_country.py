# Generated by Django 5.0.3 on 2024-04-13 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_userinfo_designation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='country',
            field=models.CharField(max_length=15),
        ),
    ]
