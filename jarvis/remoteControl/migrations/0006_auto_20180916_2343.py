# Generated by Django 2.1.1 on 2018-09-17 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remoteControl', '0005_order_silentmode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='ip',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='machine',
            name='mac',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='machine',
            name='notes',
            field=models.TextField(blank=True),
        ),
    ]
