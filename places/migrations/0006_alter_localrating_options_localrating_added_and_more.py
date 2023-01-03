# Generated by Django 4.1.4 on 2023-01-03 13:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_locals_logo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='localrating',
            options={'ordering': ['-added']},
        ),
        migrations.AddField(
            model_name='localrating',
            name='added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='localrating',
            name='rating',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
