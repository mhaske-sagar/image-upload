# Generated by Django 4.0.3 on 2022-09-04 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfectapp', '0003_finalsubmit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finalsubmit',
            name='qno',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='finalsubmit',
            name='username',
            field=models.CharField(max_length=20),
        ),
    ]
