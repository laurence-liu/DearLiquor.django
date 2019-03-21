# Generated by Django 2.1.5 on 2019-03-18 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cocktail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('pic', models.URLField(blank=True)),
                ('link', models.URLField(blank=True)),
            ],
        ),
    ]