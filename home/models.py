from django.db import models

from django.dispatch import receiver
from django.db.models.signals import pre_delete, pre_save

# Create your models here.

class LightStrip(models.Model):
    title = models.CharField(max_length=200, help_text="The name of the light strip.")
    num_pixels = models.IntegerField(help_text="The number of neopixels on the light strip.")
    pwm_pin = models.IntegerField(help_text="The pin the strip is connected to on the Raspberry Pi.")


    class Meta():
        verbose_name = "Light Strip"
        verbose_name_plural = "Light Strips"

    def __str__(self):
        return self.title

class Effects(models.Model):
    title = models.CharField(max_length=200, help_text="The name of the effect.")
    pub_date = models.DateTimeField(auto_now_add=True)
    effect_file = models.FileField(upload_to="effects/")

    class Meta():
        verbose_name = "Effect"
        verbose_name_plural = "Effects"

    def __str__(self):
        return self.title

@receiver(pre_delete, sender=Effects)
def remove_effect_file(sender, instance, **kwargs):
    instance.effect_file.delete()

@receiver(pre_save, sender=Effects)
def remove_old_effect(sender, instance, **kwargs):
    try:
        current = Effects.objects.get(pk=instance.pk)
    except Effects.DoesNotExist:
        pass
    else:
        if current.effect_file != instance.effect_file:
            current.effect_file.delete(save=False)