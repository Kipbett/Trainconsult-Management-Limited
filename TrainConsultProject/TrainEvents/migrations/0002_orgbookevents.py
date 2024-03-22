# Generated by Django 4.1.6 on 2023-02-12 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TrainEvents', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrgBookEvents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organisation_name', models.CharField(max_length=100)),
                ('participants_attending', models.PositiveIntegerField()),
                ('amount_paid', models.PositiveIntegerField()),
                ('mode_of_payment', models.CharField(choices=[('mpesa', 'M-Pesa'), ('visa', 'Visa')], max_length=10)),
            ],
        ),
    ]