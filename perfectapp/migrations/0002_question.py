# Generated by Django 4.0.3 on 2022-08-28 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfectapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('qno', models.IntegerField(primary_key=True, serialize=False)),
                ('subject', models.CharField(max_length=20)),
                ('question', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=40)),
                ('a', models.CharField(max_length=20)),
                ('b', models.CharField(max_length=20)),
                ('c', models.CharField(max_length=20)),
                ('d', models.CharField(max_length=20)),
            ],
        ),
    ]
