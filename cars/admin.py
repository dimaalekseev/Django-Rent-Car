from django.contrib import admin

from .models import CarsList


class CarListAdmin(admin.ModelAdmin):
    list_display = ("id", "vendor", "model", "engine", "color", "price",
                    "rating", "carmanager_id", "is_published")  # відображати поля з БД прямо в адмінці, пункт ---is published--- вказує чи відображаться дана машина на сайті

    # зробити дані поля клікабельними в адмінці для переходу у вікно редагування інформації про машину
    list_display_links = ("id", "vendor", "model") #зробити поля клікабельними
    list_editable = ("is_published",) #щоб змінювати це поле відразу, не переходячи у вікно редагування інфи про машину(поставити галочку в адмінці)
    search_fields = ("vendor", "price", "engine", "model", "rating") #пошук по заданим полям
    list_per_page = 25 #пагінація
    list_filter = ("carmanager_id", "vendor") # фільтр по полю

admin.site.register(CarsList, CarListAdmin)
