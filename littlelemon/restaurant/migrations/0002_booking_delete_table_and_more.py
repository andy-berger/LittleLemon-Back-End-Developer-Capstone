# Generated by Django 4.1.5 on 2023-02-08 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("restaurant", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="Booking",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("no_of_guests", models.IntegerField()),
                ("bookingdate", models.DateField()),
            ],
        ),
        migrations.DeleteModel(name="Table"),
        migrations.RenameField(
            model_name="menu", old_name="no_of_guests", new_name="inventory"
        ),
        migrations.RenameField(model_name="menu", old_name="name", new_name="title"),
        migrations.RemoveField(model_name="menu", name="bookingdate"),
        migrations.AddField(
            model_name="menu",
            name="price",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
    ]
