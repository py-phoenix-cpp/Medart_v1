# Generated by Django 4.0.6 on 2022-09-13 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_delete_introduction_doctors_bio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctors',
            name='bio',
            field=models.TextField(),
        ),
    ]
