# Generated by Django 2.2 on 2019-05-02 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20190502_2105'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='username',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='user',
            name='password',
        ),
    ]