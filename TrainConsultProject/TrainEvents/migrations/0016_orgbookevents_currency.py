# Generated by Django 4.1.6 on 2023-02-23 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TrainEvents', '0015_remove_orgbookevents_middle_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='orgbookevents',
            name='currency',
            field=models.CharField(default=1, max_length=3),
            preserve_default=False,
        ),
    ]