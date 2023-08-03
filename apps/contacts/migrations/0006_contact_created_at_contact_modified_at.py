from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("contacts", "0001_squashed_0005_rename_contact"),
    ]

    operations = [
        migrations.AddField(
            model_name="contact",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="contact",
            name="modified_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
