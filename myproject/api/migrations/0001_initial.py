# Generated by Django 5.1.6 on 2025-02-25 07:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Credits',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('issuance_date', models.DateField()),
                ('return_date', models.DateField()),
                ('actual_return_date', models.DateField(blank=True, null=True)),
                ('body', models.DecimalField(decimal_places=2, max_digits=10)),
                ('percent', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Dictionary',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('login', models.CharField(max_length=255, unique=True)),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sum', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_date', models.DateField()),
                ('credit_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='api.credits')),
                ('type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='api.dictionary')),
            ],
        ),
        migrations.CreateModel(
            name='Plans',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('period', models.DateField()),
                ('sum', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plans', to='api.dictionary')),
            ],
        ),
        migrations.AddField(
            model_name='credits',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='credits', to='api.users'),
        ),
    ]
