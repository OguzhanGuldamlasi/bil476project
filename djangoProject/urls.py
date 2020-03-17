from heatMap.models import Urunler
import xlrd
"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('heatMap.urls')),
    path('admin/', admin.site.urls),
]
# loc = ("2.2020.xls")
# wb = xlrd.open_workbook(loc)
# sheet = wb.sheet_by_index(0)
#
# for i in range(sheet.nrows):
#     if sheet.cell_value(i,0)=="Firma":
#         print()
#     else:
#      new_entry = Urunler(firma=sheet.cell_value(i,0),adres=sheet.cell_value(i,1),urunTipi=sheet.cell_value(i,2),urunKategorisi=sheet.cell_value(i,3),urun=sheet.cell_value(i,4),hileGerekcesi=sheet.cell_value(i,5),etkenMadde=sheet.cell_value(i,6),enlem=sheet.cell_value(i,7),boylam=sheet.cell_value(i,8),marka=sheet.cell_value(i,9),partiNo=sheet.cell_value(i,10),tarih=sheet.cell_value(i,11))
#      new_entry.save()
# loc = ("2020.xls")
# wb = xlrd.open_workbook(loc)
# sheet = wb.sheet_by_index(0)
#
# for i in range(sheet.nrows):
#     if sheet.cell_value(i,0)=="Firma":
#         print()
#     else:
#      new_entry = Urunler(firma=sheet.cell_value(i,0),adres=sheet.cell_value(i,1),urunTipi=sheet.cell_value(i,2),urunKategorisi=sheet.cell_value(i,3),urun=sheet.cell_value(i,4),hileGerekcesi=sheet.cell_value(i,5),etkenMadde=sheet.cell_value(i,6),enlem=sheet.cell_value(i,7),boylam=sheet.cell_value(i,8),marka=sheet.cell_value(i,9),partiNo=sheet.cell_value(i,10),tarih=sheet.cell_value(i,11))
#      new_entry.save()
# loc = ("07012015.xls")
# wb = xlrd.open_workbook(loc)
# sheet = wb.sheet_by_index(0)
#
# for i in range(sheet.nrows):
#     if sheet.cell_value(i,0)=="Firma":
#         print()
#     else:
#      new_entry = Urunler(firma=sheet.cell_value(i,0),adres=sheet.cell_value(i,1),urunTipi=sheet.cell_value(i,2),urunKategorisi=sheet.cell_value(i,3),urun=sheet.cell_value(i,4),hileGerekcesi=sheet.cell_value(i,5),etkenMadde=sheet.cell_value(i,6),enlem=sheet.cell_value(i,7),boylam=sheet.cell_value(i,8),marka=sheet.cell_value(i,9),partiNo=sheet.cell_value(i,10),tarih=sheet.cell_value(i,11))
#      new_entry.save()
# loc = ("12202019.xls")
# wb = xlrd.open_workbook(loc)
# sheet = wb.sheet_by_index(0)
#
# for i in range(sheet.nrows):
#     if sheet.cell_value(i,0)=="Firma":
#         print()
#     else:
#      new_entry = Urunler(firma=sheet.cell_value(i,0),adres=sheet.cell_value(i,1),urunTipi=sheet.cell_value(i,2),urunKategorisi=sheet.cell_value(i,3),urun=sheet.cell_value(i,4),hileGerekcesi=sheet.cell_value(i,5),etkenMadde=sheet.cell_value(i,6),enlem=sheet.cell_value(i,7),boylam=sheet.cell_value(i,8),marka=sheet.cell_value(i,9),partiNo=sheet.cell_value(i,10),tarih=sheet.cell_value(i,11))
#      new_entry.save()
# loc = ("17122016.xls")
# wb = xlrd.open_workbook(loc)
# sheet = wb.sheet_by_index(0)
#
# for i in range(sheet.nrows):
#     if sheet.cell_value(i,0)=="Firma":
#         print()
#     else:
#      new_entry = Urunler(firma=sheet.cell_value(i,0),adres=sheet.cell_value(i,1),urunTipi=sheet.cell_value(i,2),urunKategorisi=sheet.cell_value(i,3),urun=sheet.cell_value(i,4),hileGerekcesi=sheet.cell_value(i,5),etkenMadde=sheet.cell_value(i,6),enlem=sheet.cell_value(i,7),boylam=sheet.cell_value(i,8),marka=sheet.cell_value(i,9),partiNo=sheet.cell_value(i,10),tarih=sheet.cell_value(i,11))
#      new_entry.save()
# loc = ("22072015.xls")
# wb = xlrd.open_workbook(loc)
# sheet = wb.sheet_by_index(0)
#
# for i in range(sheet.nrows):
#     if sheet.cell_value(i,0)=="Firma":
#         print()
#     else:
#      new_entry = Urunler(firma=sheet.cell_value(i,0),adres=sheet.cell_value(i,1),urunTipi=sheet.cell_value(i,2),urunKategorisi=sheet.cell_value(i,3),urun=sheet.cell_value(i,4),hileGerekcesi=sheet.cell_value(i,5),etkenMadde=sheet.cell_value(i,6),enlem=sheet.cell_value(i,7),boylam=sheet.cell_value(i,8),marka=sheet.cell_value(i,9),partiNo=sheet.cell_value(i,10),tarih=sheet.cell_value(i,11))
#      new_entry.save()
# loc = ("23032018.xls")
# wb = xlrd.open_workbook(loc)
# sheet = wb.sheet_by_index(0)
#
# for i in range(sheet.nrows):
#     if sheet.cell_value(i,0)=="Firma":
#         print()
#     else:
#      new_entry = Urunler(firma=sheet.cell_value(i,0),adres=sheet.cell_value(i,1),urunTipi=sheet.cell_value(i,2),urunKategorisi=sheet.cell_value(i,3),urun=sheet.cell_value(i,4),hileGerekcesi=sheet.cell_value(i,5),etkenMadde=sheet.cell_value(i,6),enlem=sheet.cell_value(i,7),boylam=sheet.cell_value(i,8),marka=sheet.cell_value(i,9),partiNo=sheet.cell_value(i,10),tarih=sheet.cell_value(i,11))
#      new_entry.save()
# loc = ("28102014.xls")
# wb = xlrd.open_workbook(loc)
# sheet = wb.sheet_by_index(0)
#
# for i in range(sheet.nrows):
#     if sheet.cell_value(i,0)=="Firma":
#         print()
#     else:
#      new_entry = Urunler(firma=sheet.cell_value(i,0),adres=sheet.cell_value(i,1),urunTipi=sheet.cell_value(i,2),urunKategorisi=sheet.cell_value(i,3),urun=sheet.cell_value(i,4),hileGerekcesi=sheet.cell_value(i,5),etkenMadde=sheet.cell_value(i,6),enlem=sheet.cell_value(i,7),boylam=sheet.cell_value(i,8),marka=sheet.cell_value(i,9),partiNo=sheet.cell_value(i,10),tarih=sheet.cell_value(i,11))
#      new_entry.save()
# loc = ("31122015.xls")
# wb = xlrd.open_workbook(loc)
# sheet = wb.sheet_by_index(0)
#
# for i in range(sheet.nrows):
#     if sheet.cell_value(i,0)=="Firma":
#         print()
#     else:
#      new_entry = Urunler(firma=sheet.cell_value(i,0),adres=sheet.cell_value(i,1),urunTipi=sheet.cell_value(i,2),urunKategorisi=sheet.cell_value(i,3),urun=sheet.cell_value(i,4),hileGerekcesi=sheet.cell_value(i,5),etkenMadde=sheet.cell_value(i,6),enlem=sheet.cell_value(i,7),boylam=sheet.cell_value(i,8),marka=sheet.cell_value(i,9),partiNo=sheet.cell_value(i,10),tarih=sheet.cell_value(i,11))
#      new_entry.save()
# Urunler.objects.get()