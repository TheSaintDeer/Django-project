# Generated by Django 5.0.4 on 2024-04-16 12:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0003_alter_lead_agent'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='organisation',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='leads.userprofile'),
            preserve_default=False,
        ),
    ]
