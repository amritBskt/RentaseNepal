# Generated by Django 5.1.2 on 2025-01-12 17:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_blog_summary_alter_blog_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostel',
            name='admission_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='hostel',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='hostel',
            name='food_menu',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
        migrations.AddField(
            model_name='hostel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='hostel',
            name='isFeatured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='hostel',
            name='rules',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='summary',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.CreateModel(
            name='HostelImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('hostel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='additional_images', to='api.hostel')),
            ],
        ),
    ]
