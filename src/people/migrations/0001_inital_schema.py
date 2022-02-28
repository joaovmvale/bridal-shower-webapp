# Generated by Django 4.0.2 on 2022-02-09 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255, verbose_name='Nome da pessoa')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='E-mail da pessoa')),
            ],
            options={
                'verbose_name': 'person',
                'verbose_name_plural': 'people',
            },
        ),
    ]
