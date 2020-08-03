from django.shortcuts import render, redirect
from operator import attrgetter
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from blog.views import get_blog_queryset
from artist.views import create_artistportfolio_view, get_artistportfolios_queryset # noqa
# from artist.forms import ContactUsForm
# from blog.models import BlogPost


def home_screen_view(request):
    # context = {}

    # # to accept queries
    # query = ""
    # if request.GET:
    #     query = request.GET.get('q', '')
    #     context['query'] = str(query)

    # blog_posts = sorted(get_blog_queryset(query), key=attrgetter('date_updated'), reverse=True) # noqa

    # # pagination for all website pages
    # page = request.GET.get('page', 1)
    # blog_posts_paginator = Paginator(blog_posts, BLOG_POST_PER_PAGE)

    # try:
    #     blog_posts = blog_posts_paginator.page(page)
    # except PageNotAnInteger:
    #     blog_posts = blog_posts_paginator.page(BLOG_POST_PER_PAGE)
    # except EmptyPage:
    #     blog_posts = blog_posts_paginator.page(blog_posts_paginator.num_pages)

    # context['blog_posts'] = blog_posts
    return render(request, "personal/index.html")


def about_us_view(request):
    return render(request, "personal/about.html")


BLOG_POST_PER_PAGE = 5


def blog_posts_view(request, *args, **kwargs):
    context = {}

    # to accept queries
    query = ""
    if request.GET:
        query = request.GET.get('q', '')
        context['query'] = str(query)

    blog_posts = sorted(get_blog_queryset(query), key=attrgetter('date_updated'), reverse=True) # noqa

    # pagination for all website pages
    page = request.GET.get('page', 1)
    blog_posts_paginator = Paginator(blog_posts, BLOG_POST_PER_PAGE)

    try:
        blog_posts = blog_posts_paginator.page(page)
    except PageNotAnInteger:
        blog_posts = blog_posts_paginator.page(BLOG_POST_PER_PAGE)
    except EmptyPage:
        blog_posts = blog_posts_paginator.page(blog_posts_paginator.num_pages)

    context['blog_posts'] = blog_posts

    return render(request, "personal/blog_posts.html", context)


ARTIST_PORTOFOLIOS_PER_PAGE = 5


def artist_portfolio_screen(request, *args, **kwargs):
    context = {}

    # to accept queries
    query = ""
    if request.GET:
        query = request.GET.get('q', '')
        context['query'] = str(query)

    artistportfolios = sorted(get_artistportfolios_queryset(query), key=attrgetter('id'), reverse=True) # noqa

    # pagination for all website pages
    page = request.GET.get('page', 1)
    artistportfolios_paginator = Paginator(artistportfolios, ARTIST_PORTOFOLIOS_PER_PAGE) # noqa

    try:
        artistportfolios = artistportfolios_paginator.page(page)
    except PageNotAnInteger:
        artistportfolios = artistportfolios_paginator.page(ARTIST_PORTOFOLIOS_PER_PAGE) # noqa
    except EmptyPage:
        artistportfolios = artistportfolios_paginator.page(artistportfolios_paginator.num_pages) # noqa

    context['artistportfolios'] = artistportfolios

    return render(request, "personal/artist_portfolios.html", context)


def contact_us_view(request):
    context = {}

    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            # send email or store requests somewhere
            import pdb; pdb.set_trace()
            pass
            # obj = form.save(commit=False)
            # obj.save()
            # context['success_message'] = "Message sent successfully"
            # return redirect('personal:contact_us.html', {})

    else:
        return render(request, "personal/contact_us.html", {})


def services_screen_view(request):

    return render(request, "personal/services.html", {})
