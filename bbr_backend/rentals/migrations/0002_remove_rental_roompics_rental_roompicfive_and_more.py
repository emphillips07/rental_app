# Generated by Django 4.2 on 2024-02-28 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rental',
            name='roomPics',
        ),
        migrations.AddField(
            model_name='rental',
            name='roomPicFive',
            field=models.ImageField(blank=True, null=True, upload_to='rental_pics/'),
        ),
        migrations.AddField(
            model_name='rental',
            name='roomPicFour',
            field=models.ImageField(blank=True, null=True, upload_to='rental_pics/'),
        ),
        migrations.AddField(
            model_name='rental',
            name='roomPicOne',
            field=models.ImageField(blank=True, null=True, upload_to='rental_pics/'),
        ),
        migrations.AddField(
            model_name='rental',
            name='roomPicThree',
            field=models.ImageField(blank=True, null=True, upload_to='rental_pics/'),
        ),
        migrations.AddField(
            model_name='rental',
            name='roomPicTwo',
            field=models.ImageField(blank=True, null=True, upload_to='rental_pics/'),
        ),
        migrations.AlterField(
            model_name='rental',
            name='profilePic',
            field=models.ImageField(blank=True, null=True, upload_to='rental_pics/'),
        ),
        migrations.DeleteModel(
            name='RoomPictures',
        ),
    ]
