# Generated by Django 4.2.5 on 2023-11-13 20:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('esmart', '0022_favorites'),
    ]

    operations = [
        migrations.AddField(
            model_name='favorites',
            name='receiver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='favorites',
            name='page',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='esmart.page'),
        ),
    ]
