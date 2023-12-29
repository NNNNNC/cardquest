from django.contrib import admin

# Register your models here.
from .models import PokemonCard, Trainer, Collection


@admin.register(PokemonCard)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ("name","rarity")
    search_fields = ("name",)

@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    search_fields = ('name',)

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('trainer', 'card', 'created_at')
    search_fields = ('trainer', 'card')


