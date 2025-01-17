# Generated by Django 4.1.6 on 2023-02-12 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TrainEvents', '0004_orgbookevents_full_names'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orgbookevents',
            old_name='amount_paid',
            new_name='booking_amount',
        ),
        migrations.RemoveField(
            model_name='orgbookevents',
            name='participants_attending',
        ),
        migrations.AddField(
            model_name='orgbookevents',
            name='email_address',
            field=models.EmailField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
