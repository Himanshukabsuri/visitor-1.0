# Generated by Django 5.1.2 on 2024-11-05 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0016_sub_alter_visitor_discription'),
    ]

    operations = [
        migrations.AddField(
            model_name='sub',
            name='name',
            field=models.CharField(default='a', max_length=100),
        ),
    ]
