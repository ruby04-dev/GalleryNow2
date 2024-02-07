from django.contrib import admin
from django.db import models, router, transaction
from django.shortcuts import render, redirect
from django.urls import path, include, re_path
from django.http import HttpResponseServerError

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.contrib.admin.templatetags.admin_urls import add_preserved_filters
from django.template.response import SimpleTemplateResponse, TemplateResponse
from django.utils.translation import gettext as _


# Register your models here.
from .models import Gallery, Log
import pandas as pd


class GalleryAdmin(admin.ModelAdmin):
    # def add_view(self, request, form_url="", extra_context=None):
    #     print("form_url: ", form_url)
    #     return self.changeform_view(request, None, form_url, extra_context)

    def get_urls(self):
        info = self.opts.app_label, self.opts.model_name

        urls = super().get_urls()
        my_urls = [
            path("import/", self.admin_site.admin_view(self.bulk_update_data_view),
                 name="%s_%s_import" % info)
        ]
        return my_urls + urls

    def bulk_update_data_view(self, request, form_url="", extra_context=None):
        log_admin = self.admin_site._registry[Log]
        return log_admin.add_view(request)

    actions = ['bulk_update_data']


class LogAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        """
        Given a model instance save it to the database.
        """
        file = obj.data
        df = pd.read_excel(file, header=0)
        for index, row in df.iterrows():
            # print(*row_data)
            fields = [field.name for field in Gallery._meta.fields]
            row_data = row.tolist()[:21]  # 데이터프레임 행을 리스트로 변환
            Gallery.objects.create(**dict(zip(fields[1:], row_data)))

        # for file in request.FILES.getlist('excel_file'):
        #     df = pd.read_excel(file, header=0)
        #     for index, row in df.iterrows():
        #         row_data = row.tolist()  # 데이터프레임 행을 리스트로 변환
        #         Gallery.objects.create(*row_data)
        obj.save()


admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Log, LogAdmin)
