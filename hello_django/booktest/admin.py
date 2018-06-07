from django.contrib import admin
from models import BookInfo, HeroInfo


class HeroInfoInline(admin.StackedInline):
    model = HeroInfo
    extra = 2


class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['pk', 'btitle', 'bpub_date']
    list_filter = ['btitle']
    search_fields = ['btitle']
    list_per_page = 10
    fields = ['bpub_date', 'btitle']
    inlines = [HeroInfoInline]
    # fieldsets = [
    #     ('basic', {'fields': ['btitle']}),
    #     ('more', {'fields': ['bpub_date']}),
    # ]


class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['pk', 'hname', 'gender', 'hcontent', 'hbook']
    list_filter = ['hname']
    search_fields = ['hname']
    list_per_page = 10
    fields = ['hgender', 'hname', 'hcontent', 'hbook']


# Register your models here.
admin.site.register(HeroInfo, HeroInfoAdmin)
admin.site.register(BookInfo, BookInfoAdmin)
