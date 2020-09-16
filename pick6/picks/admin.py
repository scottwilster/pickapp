from django.contrib import admin
from .models import Bet


class BetAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Bet Information', {'fields': ['user_name', 'team_text', 'line_text', 'line_pts', 'result']}),
        ('Date Information', {'fields': ['pub_date']}),
    ]
    list_display = ('user_name', 'team_text', 'line_text', 'line_pts', 'result')
    list_filter = ['pub_date']
    search_fields = ['user_name']


admin.site.register(Bet, BetAdmin)
