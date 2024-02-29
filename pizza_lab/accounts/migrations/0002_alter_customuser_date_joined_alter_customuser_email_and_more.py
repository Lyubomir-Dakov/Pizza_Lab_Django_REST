# Generated by Django 5.0.2 on 2024-02-29 12:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="date_joined",
            field=models.DateField(auto_now_add=True, verbose_name="Date joined"),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="email",
            field=models.EmailField(max_length=100, unique=True, verbose_name="Email"),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="is_active",
            field=models.BooleanField(default=True, verbose_name="Active user"),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="is_staff",
            field=models.BooleanField(default=False, verbose_name="Employee"),
        ),
        migrations.AlterField(
            model_name="profile",
            name="first_name",
            field=models.CharField(max_length=30, verbose_name="First name"),
        ),
        migrations.AlterField(
            model_name="profile",
            name="last_name",
            field=models.CharField(max_length=30, verbose_name="Last name"),
        ),
    ]
