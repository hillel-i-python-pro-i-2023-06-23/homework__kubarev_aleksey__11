from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("contacts", "0006_contact_created_at_contact_modified_at"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="contact",
            options={"ordering": ["modified_at", "name"]},
        ),
    ]
