# Generated by Django 3.0.8 on 2020-07-31 11:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtistryCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ArtistPortfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=200)),
                ('profile_image', models.ImageField(upload_to='pics')),
                ('email_address', models.EmailField(blank=True, max_length=70, null=True)),
                ('phone_number', phone_field.models.PhoneField(max_length=31, unique=True)),
                ('description', models.TextField(max_length=1000)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('status', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive')], max_length=1)),
                ('artistry_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artist.ArtistryCategory')),
                ('business_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Artist Portfolio',
                'verbose_name_plural': 'Artist Porfolios',
                'ordering': ['business_owner', 'business_name'],
            },
        ),
    ]
