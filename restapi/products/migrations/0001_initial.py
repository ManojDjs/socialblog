# Generated by Django 2.2.13 on 2020-06-10 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufracturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('location', models.CharField(max_length=256)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Prodcut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('price', models.FloatField()),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('shipping_cost', models.FloatField()),
                ('quantity', models.PositiveSmallIntegerField()),
                ('manufracturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.Manufracturer')),
            ],
        ),
    ]
