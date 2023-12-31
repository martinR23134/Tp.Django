# Generated by Django 4.2.5 on 2023-11-20 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Destacado_por_categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destacado', models.BooleanField(null=True)),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='core.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Stock_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('foto', models.ImageField(upload_to='imgs/')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('color', models.CharField(choices=[('B', 'Blanco'), ('N', 'Negro'), ('A', 'Azul')], max_length=1, null=True)),
                ('descripcion', models.TextField(max_length=500, null=True)),
                ('info_adicional', models.TextField(max_length=500, null=True)),
                ('categorias', models.ManyToManyField(through='core.Destacado_por_categoria', to='core.categoria')),
            ],
        ),
        migrations.AddField(
            model_name='destacado_por_categoria',
            name='stock_item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='core.stock_item'),
        ),
    ]
