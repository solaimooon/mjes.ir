from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, render
from .models import  Category, Occasion, Night, MediaFile,clip
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.db.models import Min





def index(request):
    categorys = Category.objects.all()
    mediafile_selected = MediaFile.objects.filter(Selected=True)
    clips=clip.objects.all()

    return render(request, 'masjed_template.html', {"categorys": categorys, "mediafile_selected": mediafile_selected,"clips":clips})

# live page of masjed
def live(request):
    return render(request, 'live.html')


# report page of masjed
def report(request):
    return render(request, 'report.html')


# media pagese of masjed


# ۱. لیست دسته‌بندی‌های یک مسجد
# def category_list(request, mosque_slug=None):
#     mosque = get_current_mosque(request, mosque_slug)
#     categories = mosque.categories.all()
#     return render(request, "archive_page_category.html",{"mosque": mosque, "categories": categories})


def year_list(request, category_slug, mosque_slug=None):
    category = get_object_or_404(Category, slug=category_slug,)
    occasions = (
        category.occasions
            .values('year')
            .annotate(first_id=Min('id'))
            .values_list('first_id', flat=True)
    )
    occasions = Occasion.objects.filter(id__in=occasions)
    return render(request, "archive_page_category.html", { "category":category, "occasions":occasions})


def occasion_list(request, category_slug, year, mosque_slug=None):
    category = get_object_or_404(Category, slug=category_slug,)
    occasions = category.occasions.filter(year=year)
    return render(request, "archive_page_occasions.html", {
     "category": category, "year": year, "occasions": occasions
    })


def night_list(request, category_slug,occasion_slug, mosque_slug=None):

    category = get_object_or_404(Category, slug=category_slug)
    print(occasion_slug)
    occasion = get_object_or_404(Occasion, slug=occasion_slug,)
    print("occation",occasion)
    nights = occasion.nights.all()
    print("empty",nights)
    return render(request, "archive_page_night.html", { "occasion": occasion, "nights": nights,"category":category})


def media_list(request,category_slug,year,occasion_slug,night_slug, mosque_slug=None):
    night = get_object_or_404(Night, slug=night_slug,)
    media_files = night.media_files.all()
    return render(request, "archive_page_list_media.html", {"night": night, "media_files": media_files})

def media_single(request,media_slug):
    print("im here")
    media_files = MediaFile.objects.get(slug=media_slug)
    return render(request,'archive_singel_media.html',{"media_files":media_files})


def clip_view(request,slug):
    clip_media=clip.objects.get(slug=slug)
    return render(request,'clip_single.html',{"clip":clip_media})






