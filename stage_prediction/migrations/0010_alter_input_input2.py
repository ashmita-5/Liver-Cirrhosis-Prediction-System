# Generated by Django 4.2.4 on 2023-11-29 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stage_prediction', '0009_alter_input_input1_alter_input_input4_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='input',
            name='input2',
            field=models.CharField(choices=[('0.0', 'D'), ('1.0', 'C'), ('2.0', 'CL')], default='2.0', max_length=50),
        ),
    ]
