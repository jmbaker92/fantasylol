# Generated by Django 4.2.5 on 2023-10-28 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0004_game_season_week_alter_statistics_assists_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistics',
            name='assists',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='statistics',
            name='baronKills',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='statistics',
            name='deaths',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='statistics',
            name='dragonKills',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='statistics',
            name='inhibitors',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='statistics',
            name='kills',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='statistics',
            name='turrets',
            field=models.IntegerField(),
        ),
    ]
