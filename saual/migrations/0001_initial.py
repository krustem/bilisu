# Generated by Django 2.1.1 on 2018-10-03 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Suraq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suraq_matini', models.CharField(max_length=150)),
                ('zhar_kun', models.DateTimeField(verbose_name='zharialangan kuni')),
            ],
        ),
    ]