# Generated by Django 5.2.3 on 2025-06-13 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_alter_account_created_at_alter_account_updated_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='industry',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
