# Generated by Django 5.1.4 on 2025-01-01 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=320)),
                ('Password', models.CharField(max_length=50)),
            ],
        ),
    ]
