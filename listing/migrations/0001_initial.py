# Generated by Django 3.1.2 on 2020-10-21 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, verbose_name='Name of Place')),
                ('county', models.CharField(blank=True, max_length=100, verbose_name='County')),
                ('state', models.CharField(blank=True, max_length=100, verbose_name='State')),
                ('latitude', models.CharField(blank=True, max_length=100, null=True, verbose_name='Latitude')),
                ('longitude', models.CharField(blank=True, max_length=100, null=True, verbose_name='Longitude')),
                ('notes', models.TextField(blank=True, max_length=500, verbose_name='Description Field')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(blank=True, max_length=100, verbose_name='Last Name')),
                ('first_name', models.CharField(blank=True, max_length=100, verbose_name='First Name')),
                ('middle_name', models.CharField(blank=True, max_length=100, verbose_name='Middle Name')),
                ('gender', models.CharField(blank=True, max_length=20, verbose_name='Gender')),
                ('birth_date', models.DateField(blank=True, verbose_name='Birth Date')),
                ('death_date', models.DateField(blank=True, verbose_name='Death Date')),
                ('type_of', models.CharField(blank=True, choices=[('au', 'Author'), ('as', 'Assembler'), ('ed', 'Editor'), ('sc', 'Scrivener'), ('tr', 'Translator'), ('ot', 'Others')], default='au', max_length=2, null=True, verbose_name='Roles of the person')),
                ('birth_place', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='birth_place', to='listing.place')),
                ('death_place', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='death_place', to='listing.place')),
            ],
        ),
    ]
