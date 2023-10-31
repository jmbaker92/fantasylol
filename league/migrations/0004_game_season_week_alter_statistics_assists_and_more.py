# Generated by Django 4.2.5 on 2023-10-28 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0003_statistics_rename_postion_player_position'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teamOne', models.CharField(max_length=30)),
                ('teamTwo', models.CharField(max_length=30)),
                ('teamOneScore', models.IntegerField(max_length=30)),
                ('teamTwoScore', models.IntegerField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Week',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='statistics',
            name='assists',
            field=models.IntegerField(max_length=30),
        ),
        migrations.AlterField(
            model_name='statistics',
            name='baronKills',
            field=models.IntegerField(max_length=30),
        ),
        migrations.AlterField(
            model_name='statistics',
            name='deaths',
            field=models.IntegerField(max_length=30),
        ),
        migrations.AlterField(
            model_name='statistics',
            name='dragonKills',
            field=models.IntegerField(max_length=30),
        ),
        migrations.AlterField(
            model_name='statistics',
            name='inhibitors',
            field=models.IntegerField(max_length=30),
        ),
        migrations.AlterField(
            model_name='statistics',
            name='kills',
            field=models.IntegerField(max_length=30),
        ),
        migrations.AlterField(
            model_name='statistics',
            name='turrets',
            field=models.IntegerField(max_length=30),
        ),
    ]
