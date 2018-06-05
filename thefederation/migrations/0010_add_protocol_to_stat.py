# Generated by Django 2.0.3 on 2018-04-22 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('thefederation', '0009_add_platform_to_stat'),
    ]

    operations = [
        migrations.AddField(
            model_name='stat',
            name='protocol',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='thefederation.Protocol'),
        ),
    ]