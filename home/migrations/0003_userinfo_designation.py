# Generated by Django 5.0.3 on 2024-04-13 16:38

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_contact_userinfo_company_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='designation',
            field=models.CharField(default=django.utils.timezone.now, max_length=155),
            preserve_default=False,
        ),
    ]
