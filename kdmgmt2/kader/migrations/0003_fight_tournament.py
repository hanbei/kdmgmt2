# Generated by Django 2.0.1 on 2018-02-08 21:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kader', '0002_attendance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('red_point_one', models.CharField(blank=True, choices=[('M', 'M'), ('K', 'K'), ('D', 'D'), ('T', 'T'), ('I', 'I')], max_length=1, null=True)),
                ('red_point_two', models.CharField(blank=True, choices=[('M', 'M'), ('K', 'K'), ('D', 'D'), ('T', 'T'), ('I', 'I')], max_length=1, null=True)),
                ('white_point_one', models.CharField(blank=True, choices=[('M', 'M'), ('K', 'K'), ('D', 'D'), ('T', 'T'), ('I', 'I')], max_length=1, null=True)),
                ('white_point_two', models.CharField(blank=True, choices=[('M', 'M'), ('K', 'K'), ('D', 'D'), ('T', 'T'), ('I', 'I')], max_length=1, null=True)),
                ('red', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='kader.Member')),
                ('white', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='kader.Member')),
            ],
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('fights', models.ManyToManyField(to='kader.Fight')),
            ],
        ),
    ]
