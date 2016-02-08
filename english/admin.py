from django.contrib import admin

from .models import User,article,question,choice,comment,performance,word,word_meaning

admin.site.register(User)
admin.site.register(article)

admin.site.register(question)
admin.site.register(choice)
admin.site.register(comment)
admin.site.register(performance)
admin.site.register(word)
admin.site.register(word_meaning)

# Register your models here.


# Register your models here.
