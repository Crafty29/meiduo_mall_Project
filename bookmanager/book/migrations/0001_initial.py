# Generated by Django 4.1 on 2022-08-12 03:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True)),
                ('pub_date', models.DateField(null=True)),
                ('readcount', models.IntegerField(default=0)),
                ('commentcount', models.IntegerField(default=0)),
                ('is_delete', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '书籍管理',
                'db_table': 'bookinfo',
            },
        ),
        migrations.CreateModel(
            name='PeopleInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True)),
                ('gender', models.SmallIntegerField(choices=[(1, 'male'), (2, 'female')], default=1)),
                ('description', models.CharField(max_length=100, null=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.bookinfo')),
            ],
            options={
                'db_table': 'peopleinfo',
            },
        ),
    ]
