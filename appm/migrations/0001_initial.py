# Generated by Django 2.2.2 on 2019-06-26 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('idno', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('doj', models.DateField(auto_now_add=True)),
                ('designation', models.CharField(max_length=30)),
            ],
        ),
    ]