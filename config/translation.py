from modeltranslation.translator import translator, TranslationOptions
from todo.models import ToDoListModel

class NewsTranslationOptions(TranslationOptions):
    fields = ('task',)

translator.register(ToDoListModel, NewsTranslationOptions)