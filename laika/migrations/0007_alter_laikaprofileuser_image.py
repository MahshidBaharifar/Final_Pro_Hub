# Generated by Django 4.2.7 on 2024-01-22 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laika', '0006_alter_laikaprofileuser_image_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laikaprofileuser',
            name='image',
            field=models.ImageField(blank=True, default='laika/laika_logo_400.png', null=True, upload_to='laika_img/'),
        ),
    ]
