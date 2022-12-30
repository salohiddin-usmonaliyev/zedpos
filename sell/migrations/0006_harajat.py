# Generated by Django 4.1.4 on 2022-12-28 16:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sell', '0005_sell_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Harajat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sabab', models.CharField(max_length=100, verbose_name='Sababi')),
                ('pul', models.IntegerField(verbose_name='Ishlatilgan pul')),
                ('ishchi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Ishchi')),
            ],
        ),
    ]