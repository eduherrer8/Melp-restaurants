# Generated by Django 3.2.6 on 2021-08-23 23:57

import django.contrib.gis.db.models.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.TextField(primary_key=True, serialize=False)),
                ('raiting', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(4), django.core.validators.MinValueValidator(0)])),
                ('name', models.TextField()),
                ('site', models.URLField()),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.TextField()),
                ('street', models.TextField()),
                ('city', models.TextField()),
                ('state', models.TextField()),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
                ('point', django.contrib.gis.db.models.fields.PointField(geography=True, srid=4326)),
            ],
        ),
    ]
