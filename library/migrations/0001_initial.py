# Generated by Django 5.0.4 on 2024-04-11 12:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='library.basemodel')),
                ('title', models.CharField(max_length=250)),
                ('status', models.CharField(max_length=150)),
                ('order', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['order'],
            },
            bases=('library.basemodel',),
        ),
        migrations.CreateModel(
            name='Dissertationabstract',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='library.basemodel')),
                ('title', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='images/library/dissertation_abstract')),
                ('status', models.CharField(max_length=150)),
            ],
            bases=('library.basemodel',),
        ),
        migrations.CreateModel(
            name='JournalUzbekistan',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='library.basemodel')),
                ('title', models.CharField(max_length=250)),
                ('status', models.CharField(max_length=150)),
                ('order', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['order'],
            },
            bases=('library.basemodel',),
        ),
    ]
