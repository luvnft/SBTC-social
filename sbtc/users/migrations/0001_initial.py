# Generated by Django 3.2 on 2022-11-28 17:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, help_text='tell us about yourself', max_length=500, verbose_name='about the author')),
                ('location', models.CharField(blank=True, help_text='Where do you live?', max_length=30, verbose_name='city')),
                ('birth_date', models.DateField(blank=True, help_text='Enter date of birth', null=True, verbose_name='Date of Birth')),
                ('photo', models.ImageField(blank=True, help_text='Attach your photo', upload_to='profile/', verbose_name='Photo')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
