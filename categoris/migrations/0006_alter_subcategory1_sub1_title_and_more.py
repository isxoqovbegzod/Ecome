# Generated by Django 4.0.4 on 2022-04-30 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categoris', '0005_subcategory2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory1',
            name='sub1_title',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cats_title', to='categoris.category'),
        ),
        migrations.AlterField(
            model_name='subcategory2',
            name='product_title',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub1s_title', to='categoris.subcategory1'),
        ),
    ]
