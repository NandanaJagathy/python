# Generated by Django 5.1.3 on 2024-12-04 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_register_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='Name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='register',
            name='Password',
        ),
        migrations.RemoveField(
            model_name='register',
            name='Userid',
        ),
        migrations.AddField(
            model_name='register',
            name='password',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
