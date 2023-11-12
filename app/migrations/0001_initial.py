# Generated by Django 4.2.7 on 2023-11-12 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=50)),
                ("author", models.CharField(max_length=50)),
                ("year_published", models.IntegerField()),
                ("received_in", models.DateTimeField(auto_now_add=True)),
                ("active", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="BorrowingBook",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("borrowed_date", models.DateTimeField(auto_now_add=True)),
                ("returned_date", models.DateTimeField(blank=True, null=True)),
                (
                    "book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.book"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Customer",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("full_name", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=100)),
                ("phone_number", models.CharField(max_length=20)),
                ("active", models.BooleanField(default=True)),
                (
                    "borrowed_books",
                    models.ManyToManyField(through="app.BorrowingBook", to="app.book"),
                ),
            ],
        ),
        migrations.AddField(
            model_name="borrowingbook",
            name="customer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app.customer"
            ),
        ),
    ]