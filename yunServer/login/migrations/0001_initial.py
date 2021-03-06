# Generated by Django 2.1.1 on 2018-09-27 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('osname', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('identify_num', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=11)),
                ('regist_time', models.CharField(max_length=20)),
                ('client_state', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Master',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=11)),
                ('email', models.CharField(max_length=30)),
                ('regist_time', models.CharField(max_length=20)),
                ('limit_type', models.CharField(max_length=10)),
                ('limit_time', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('product_time', models.CharField(max_length=20)),
                ('product_cost', models.CharField(max_length=20)),
                ('unit_cost', models.CharField(max_length=20)),
                ('regist_time', models.CharField(max_length=20)),
                ('kai_time', models.CharField(max_length=20)),
                ('product_type', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='client',
            name='p_name',
            field=models.ManyToManyField(to='login.Product'),
        ),
    ]
