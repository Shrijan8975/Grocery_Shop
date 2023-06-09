# Generated by Django 3.2.4 on 2021-07-12 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Categorty',
            },
        ),
        migrations.CreateModel(
            name='Grocery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gname', models.CharField(max_length=20)),
                ('price', models.FloatField(default=200)),
                ('description', models.CharField(max_length=100)),
                ('imageurl', models.ImageField(upload_to='images')),
                ('cat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminApp.category')),
            ],
            options={
                'db_table': 'Grocery',
            },
        ),
    ]
