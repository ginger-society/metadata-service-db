# Generated by Ginger 5.3.4 on 2024-07-15 14:12

from ginger.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='schema',
            new_name='dbschema',
        ),
        migrations.AlterModelTable(
            name='dbschema',
            table='dbschema',
        ),
    ]
