# Generated by Django 5.1 on 2024-10-25 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_alter_visitor_ctime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='ctime',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
