# Generated by Django 3.0.14 on 2022-03-30 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alumni_companies_worked_in'),
    ]

    operations = [
        migrations.CreateModel(
            name='Personal_Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('generator', models.CharField(max_length=20)),
                ('receiver', models.CharField(max_length=20)),
                ('not_name', models.CharField(max_length=20)),
                ('notification', models.TextField(max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='feedback',
            name='feedback',
            field=models.TextField(default='nil', max_length=500),
        ),
    ]
