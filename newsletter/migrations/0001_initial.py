# Generated by Django 2.1.2 on 2018-11-28 21:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=300)),
                ('join_date', models.DateTimeField(default=datetime.datetime.now)),
                ('subscribed', models.BooleanField(default=True)),
            ],
        ),
    ]
