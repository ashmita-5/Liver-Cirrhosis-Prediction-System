# Generated by Django 4.2.4 on 2023-11-30 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stage_prediction', '0010_alter_input_input2'),
    ]

    operations = [
        migrations.AddField(
            model_name='input',
            name='input13',
            field=models.FloatField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='input',
            name='input14',
            field=models.FloatField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='input',
            name='input15',
            field=models.CharField(choices=[('0.0', 'F'), ('1.0', 'M')], default='0.0', max_length=30),
        ),
        migrations.AddField(
            model_name='input',
            name='input16',
            field=models.FloatField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='input',
            name='input17',
            field=models.FloatField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='input',
            name='input18',
            field=models.FloatField(default=None, null=True),
        ),
    ]
