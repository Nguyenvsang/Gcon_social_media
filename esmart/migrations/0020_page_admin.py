# Generated by Django 4.2.5 on 2023-10-31 04:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('esmart', '0019_personalinformation'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='admin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='admin_page', to=settings.AUTH_USER_MODEL),
        ),
    ]
