# Generated by Django 5.0.6 on 2024-06-19 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('position', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
                ('status', models.CharField(max_length=50)),
            ],
        ),
    ]
