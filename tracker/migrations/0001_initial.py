from django.contrib.gis.db.models import PointField
from django.db import migrations, models

from tracker.models import DangerLevel


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]
    operations = [
        migrations.CreateModel(
            name='RoadCrack',
            fields=[
                ('id_station', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', PointField(srid=4326)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('danger_level', models.CharField(max_length=10, choices=DangerLevel.choices, default=DangerLevel.LOW.value)),
                ('approved', models.BooleanField(default=False)),
                ('requested_amount', models.IntegerField(default=1))
            ],
        ),
        migrations.CreateModel(
            name='PoliceBump',
            fields=[
                ('location', PointField(srid=4326)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50))
            ],
        )
    ]
