# Generated by Django 4.2.5 on 2023-10-25 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('esmart', '0002_group_groupmember_group_members'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='groupmember',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='groupmember',
            name='group',
        ),
        migrations.RemoveField(
            model_name='groupmember',
            name='user',
        ),
        migrations.DeleteModel(
            name='Group',
        ),
        migrations.DeleteModel(
            name='GroupMember',
        ),
    ]