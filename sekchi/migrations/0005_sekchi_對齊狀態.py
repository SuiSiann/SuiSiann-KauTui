# Generated by Django 4.0.6 on 2022-08-22 02:23

from django.db import migrations, models
from tuitse import kiamtsa


class Migration(migrations.Migration):

    dependencies = [
        ('sekchi', '0004_tsònghóng_sekchi_校對狀況'),
    ]

    def tuitse(apps, schema_editor):
        # We get the model from the versioned app registry;
        # if we directly import it, it'll be the wrong version
        Sekchi = apps.get_model("sekchi", "Sekchi")
        for obj in Sekchi.objects.all():
            kiatko = kiamtsa(obj.漢字, obj.羅馬字)
            obj.對齊狀態 = all(map(lambda x: x[3], kiatko))
            obj.save()

    operations = [
        migrations.AddField(
            model_name='sekchi',
            name='對齊狀態',
            field=models.BooleanField(null=True),
            preserve_default=False,
        ),
        migrations.RunPython(tuitse)
    ]
