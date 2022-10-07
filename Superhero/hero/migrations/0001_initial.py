# Generated by Django 4.1 on 2022-09-26 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Superhero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='My Superhero', max_length=100)),
                ('identity', models.CharField(default='No identity.', max_length=100)),
                ('description', models.TextField(default='No description.')),
                ('strength', models.CharField(default='No strengths.', max_length=100)),
                ('weakness', models.CharField(default='No weaknesses.', max_length=100)),
                ('image', models.CharField(default='No image url.', max_length=100)),
            ],
        ),
    ]
