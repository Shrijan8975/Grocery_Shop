# Generated by Django 3.2.4 on 2021-07-17 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0001_initial'),
        ('UserApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField()),
                ('grocery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminApp.grocery')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.userinfo')),
            ],
            options={
                'db_table': 'MyCart',
            },
        ),
    ]
