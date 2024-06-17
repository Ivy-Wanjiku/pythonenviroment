# Generated by Django 5.0.6 on 2024-06-17 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('country', models.CharField(max_length=20)),
                ('total_amount_paid', models.PositiveSmallIntegerField()),
                ('experience', models.PositiveSmallIntegerField()),
                ('age', models.PositiveSmallIntegerField()),
                ('level_of_education', models.CharField(max_length=15)),
                ('unit_taught', models.CharField(max_length=10)),
            ],
        ),
    ]
