# Generated by Django 4.1 on 2022-08-26 03:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
        ('lead', '0002_rename_assign_to_lead_assigned_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='leads', to='team.team'),
        ),
    ]
