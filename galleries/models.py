from django.forms import ModelForm
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Log(models.Model):
    # file will be uploaded to MEDIA_ROOT/imports/<created_at>_upload
    created_at = models.DateTimeField(auto_now_add=True)
    data = models.FileField(
        _("uploaded_file"), upload_to="imports/", max_length=100)

    def __str__(self):
        return str(self.created_at)

    class Meta:
        verbose_name_plural = "Logs"


class Gallery(models.Model):
    # 21 fields
    name = models.CharField(max_length=255)
    management_type = models.CharField(max_length=255)
    address_new = models.CharField(max_length=255)
    address_old = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    operating_organization = models.CharField(max_length=255)
    homepage = models.CharField(max_length=255)
    amenities = models.CharField(max_length=255)
    open_workday = models.CharField(max_length=255)
    close_workday = models.CharField(max_length=255)
    open_holiday = models.CharField(max_length=255)
    close_holiday = models.CharField(max_length=255)
    closed = models.CharField(max_length=255)
    fee_adult = models.CharField(max_length=255)
    fee_youth = models.CharField(max_length=255)
    fee_child = models.CharField(max_length=255)
    fee_info = models.TextField()
    description = models.TextField()
    transportation_info = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Galleries"


class ReadOnlyGalleryForm(ModelForm):
    class Meta:
        model = Gallery
        fields = "__all__"
