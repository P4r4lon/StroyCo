# Generated by Django 4.0 on 2021-12-22 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_deal_status_of_act'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Manager',
            new_name='Employer',
        ),
        migrations.RenameField(
            model_name='deal',
            old_name='manager',
            new_name='employer',
        ),
    ]