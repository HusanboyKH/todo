from django.contrib import admin
from .models import ToDoListModel
from .forms import ToDoforms
class ToDoAdmin(admin.ModelAdmin):
    list_display =('task',)
    search_fields =('task',)
# Register your models here.
admin.site.register(ToDoListModel,ToDoAdmin)