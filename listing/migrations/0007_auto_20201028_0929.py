# Generated by Django 3.1.2 on 2020-10-28 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0006_auto_20201028_0929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='related_works',
            field=models.ManyToManyField(blank=True, to='listing.Work'),
        ),
    ]
