# Generated by Django 5.1.3 on 2024-11-07 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(null=True, upload_to='image/')),
            ],
            options={
                'db_table': 'book_table',
            },
        ),
    ]
