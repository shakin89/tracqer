'''
Created on 24/nov/2010

@author: manci409
'''
from trACQer.note.models import Nota, DirezioneRichiedente, FunzioneRichiedente
from django.contrib import admin

class NoteAdmin(admin.ModelAdmin):
    list_display = ('anno', 'sigla')
admin.site.register(Nota, NoteAdmin)

class DirezioneRichiedenteAdmin(admin.ModelAdmin):
    pass
admin.site.register(DirezioneRichiedente, DirezioneRichiedenteAdmin)

class FunzioneRichiedenteAdmin(admin.ModelAdmin):
    pass
admin.site.register(FunzioneRichiedente, FunzioneRichiedenteAdmin)


