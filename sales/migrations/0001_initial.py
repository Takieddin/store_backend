# Generated by Django 3.2.6 on 2021-10-02 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('quantity', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('prix_final', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Restore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('basket', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='restores', to='sales.basket')),
                ('client', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='restores', to='sales.client')),
            ],
        ),
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('total', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('paied', models.IntegerField()),
                ('client', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='processes', to='sales.client')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('client', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='sales.client')),
                ('process', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='sales.process')),
            ],
        ),
        migrations.AddField(
            model_name='basket',
            name='process',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='baskets', to='sales.process'),
        ),
        migrations.AddField(
            model_name='basket',
            name='stock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='baskets', to='stock.stock'),
        ),
    ]
