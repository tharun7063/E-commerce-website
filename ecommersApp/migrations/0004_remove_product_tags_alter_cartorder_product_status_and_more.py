# Generated by Django 4.2.5 on 2023-10-27 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommersApp', '0003_alter_cartorder_product_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='tags',
        ),
        migrations.AlterField(
            model_name='cartorder',
            name='product_status',
            field=models.CharField(choices=[('shipped', 'Shipped'), ('process', 'Processing'), ('delivered', 'Delivered')], default='processing', max_length=30),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category', to='ecommersApp.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_status',
            field=models.CharField(choices=[('draft', 'Draft'), ('in_review', 'In Review'), ('published', 'Published'), ('disabled', 'Disabled')], default='in_review', max_length=10),
        ),
        migrations.AlterField(
            model_name='productreview',
            name='rating',
            field=models.IntegerField(choices=[(2, '★★☆☆☆'), (3, '★★★☆☆'), (1, '★☆☆☆☆'), (5, '★★★★★'), (4, '★★★★☆')], default=None),
        ),
    ]
