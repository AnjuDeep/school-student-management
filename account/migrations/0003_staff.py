# Generated by Django 4.1.3 on 2022-12-06 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_courses_loc_name_alter_courses_prgm_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=15)),
                ('phno', models.CharField(max_length=10)),
            ],
        ),
    ]
