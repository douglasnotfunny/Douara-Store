# Generated by Django 3.1.1 on 2020-09-24 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('douara_app', '0007_carrinho'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrinho',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='douara_app.userprofile'),
        ),
    ]
