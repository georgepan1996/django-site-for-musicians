# Generated by Django 2.1.4 on 2019-01-05 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_up_down_load', '0003_delete_user1'),
    ]

    operations = [
        migrations.CreateModel(
            name='User1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=250)),
                ('Surname', models.CharField(max_length=250)),
                ('Username', models.CharField(max_length=250)),
                ('Email', models.CharField(max_length=250)),
            ],
        ),
    ]