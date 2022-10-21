# Generated by Django 4.1 on 2022-10-11 03:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hsptl', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dep_name', models.CharField(max_length=100)),
                ('dep_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_name', models.CharField(max_length=100)),
                ('doc_spec', models.TextField()),
                ('doc_image', models.ImageField(upload_to='doctors/')),
                ('doc_department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hsptl.department')),
            ],
        ),
        migrations.DeleteModel(
            name='Departments',
        ),
    ]
