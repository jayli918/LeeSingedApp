from django.contrib import admin

# Register your models here.
from .models import SummonerInput

class SummonerInputAdmin(admin.ModelAdmin):
    class Meta:
        model = SummonerInput

admin.site.register(SummonerInput, SummonerInputAdmin)