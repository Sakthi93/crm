# Generated by Django 5.0.6 on 2024-06-12 14:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='leads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=255)),
                ('contact_person', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('website', models.CharField(blank='true', max_length=255, null='true')),
                ('confidence', models.IntegerField(blank='true', null='true')),
                ('estimated_value', models.IntegerField(blank='true', null='true')),
                ('status', models.CharField(choices=[('lost', 'lost'), ('inprogress', 'inprogress'), ('won', 'won'), ('new', 'new')], default='new', max_length=25)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leads', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
