# Generated by Django 5.0.3 on 2024-04-13 05:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='Inventory_User', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Others')], default='male', max_length=10)),
                ('phone', models.CharField(help_text='if has more than one no write separated with comma.', max_length=255)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=25)),
                ('address', models.CharField(max_length=55)),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile')),
                ('is_verify', models.BooleanField(default=False)),
                ('intro', models.TextField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
