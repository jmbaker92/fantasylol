# Generated by Django 4.2.5 on 2023-10-28 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0005_alter_statistics_assists_alter_statistics_baronkills_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='teamOneScore',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='game',
            name='teamTwoScore',
            field=models.IntegerField(),
        ),
    ]
