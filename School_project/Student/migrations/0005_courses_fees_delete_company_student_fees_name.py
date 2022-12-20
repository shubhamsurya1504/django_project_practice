# Generated by Django 4.1 on 2022-11-10 12:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Student', '0004_alter_company_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(blank=True, max_length=300, null=True)),
                ('level', models.CharField(blank=True, max_length=300, null=True)),
                ('fees', models.IntegerField()),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Student.country')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Fees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fees_date', models.DateTimeField()),
                ('amount', models.IntegerField()),
                ('course_name', models.CharField(max_length=70)),
                ('level', models.CharField(max_length=70)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.AddField(
            model_name='student',
            name='fees_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Student.fees'),
            preserve_default=False,
        ),
    ]