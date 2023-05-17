# Generated by Django 4.1.7 on 2023-03-15 09:58

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fournisseur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('adresse', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('telephone', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='ProduitC',
            fields=[
                ('produit_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='magasin.produit')),
                ('duree_garantie', models.IntegerField()),
            ],
            bases=('magasin.produit',),
        ),
        migrations.RenameField(
            model_name='produit',
            old_name='Img',
            new_name='img',
        ),
        migrations.AlterField(
            model_name='categorie',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='produit',
            name='categorie',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='magasin.categorie'),
        ),
        migrations.AlterField(
            model_name='produit',
            name='libelle',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='produit',
            name='type',
            field=models.CharField(choices=[('fr', 'Frais'), ('cs', 'Conserve'), ('em', 'emballé')], default='em', max_length=2),
        ),
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateCde', models.DateField(default=datetime.date(2023, 3, 15), null=True)),
                ('totalCde', models.FloatField()),
                ('produits', models.ManyToManyField(to='magasin.produit')),
            ],
        ),
        migrations.AddField(
            model_name='produit',
            name='fournisseur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='magasin.fournisseur'),
        ),
    ]