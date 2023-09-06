# Generated by Django 4.2.5 on 2023-09-06 12:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('type', models.IntegerField(choices=[(1, 'Fundacja'), (2, 'Organizacja Pozarządowa'), (3, 'Zbiórka Lokalna')], default=1)),
                ('categories', models.ManyToManyField(to='charity.category')),
            ],
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('address', models.CharField(max_length=128)),
                ('phone_number', models.CharField(max_length=32)),
                ('city', models.CharField(max_length=64)),
                ('zip_code', models.CharField(max_length=16)),
                ('pick_up_date', models.DateField()),
                ('pick_up_time', models.TimeField()),
                ('pick_up_comment', models.TextField()),
                ('Institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charity.institution')),
                ('categories', models.ManyToManyField(to='charity.category')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]