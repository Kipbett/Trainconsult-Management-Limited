# Generated by Django 4.1.6 on 2023-02-14 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TrainEvents', '0009_remove_orgbookevents_booking_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='orgbookevents',
            name='transaction_id',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
