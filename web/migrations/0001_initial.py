# Generated by Django 3.0.4 on 2020-04-04 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('times', models.PositiveSmallIntegerField(verbose_name='第几次')),
                ('count', models.PositiveSmallIntegerField(verbose_name='生成多少唯一码')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.ClassList')),
            ],
        ),
        migrations.CreateModel(
            name='SurveyChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('score', models.PositiveSmallIntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SurveyCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_code', models.CharField(max_length=10, unique=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('is_used', models.BooleanField(default=False, verbose_name='是否使用')),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Survey')),
            ],
        ),
        migrations.CreateModel(
            name='SurveyQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('survey_type', models.CharField(choices=[('choice', '单选'), ('suggestion', '建议')], max_length=32)),
                ('title', models.CharField(max_length=64)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SurveyTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='模板名称', max_length=64)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('questions', models.ManyToManyField(to='web.SurveyQuestion')),
            ],
        ),
        migrations.CreateModel(
            name='SurveyRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('content', models.CharField(blank=True, max_length=1024, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('choice', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.SurveyChoice')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.SurveyQuestion')),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Survey')),
                ('survey_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.SurveyCode')),
            ],
        ),
        migrations.AddField(
            model_name='surveychoice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.SurveyQuestion'),
        ),
        migrations.AddField(
            model_name='survey',
            name='survey_templates',
            field=models.ManyToManyField(to='web.SurveyTemplate'),
        ),
    ]
