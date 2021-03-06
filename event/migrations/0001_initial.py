# Generated by Django 3.1.4 on 2020-12-04 15:30

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import event.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^[a-zA-Z0-9 ]+$')])),
                ('description', models.CharField(max_length=500, validators=[django.core.validators.RegexValidator('^[a-zA-Z0-9 ]+$')])),
                ('start_date', models.DateTimeField(validators=[event.validators.validate_date])),
                ('end_date', models.DateTimeField(validators=[event.validators.validate_date])),
                ('location', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^[a-zA-Z0-9 ]+$')])),
                ('priority', models.IntegerField(choices=[(0, 'ALTO'), (1, 'MEDIO'), (2, 'BASSO')])),
                ('category', models.IntegerField(choices=[(1, 'LAVORO'), (2, 'SVAGO'), (3, 'FAMIGLIA'), (4, 'SCUOLA')])),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
