# Generated by Django 3.0.4 on 2020-04-05 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='survey',
            name='survey_templates',
            field=models.ManyToManyField(blank=True, to='web.SurveyTemplate'),
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('toppings', models.ManyToManyField(to='web.Topping')),
            ],
        ),
    ]
