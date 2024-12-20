# Generated by Django 5.1 on 2024-10-12 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=200)),
                ('student_age', models.PositiveIntegerField()),
                ('student_email', models.EmailField(max_length=254, unique=True)),
                ('student_address', models.TextField()),
                ('student_mobile_number', models.TextField()),
            ],
        ),
    ]
