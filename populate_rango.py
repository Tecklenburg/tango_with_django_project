import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

import django

django.setup()
from rango.models import Category, Page


def populate():
    # First add lists of dicts. containing pages to add into each category
    # create dict of dicts. for categories
    # allows to iterate through eacht data structure

    python_pages = [
        {'title': 'Official Python Tutorial',
         'url': 'http://docs.python.org/3/tutorial/',
         'views': 457283},
        {'title': 'How to Think like a Computer Scientist',
         'url': 'http://www.greenteapress.com/thinkpython/',
         'views': 2435},
        {'title': 'Learn Python in 10 Minutes',
         'url': 'http://www.korokithakis.net/tutorials/python/1',
         'views': 76346}]

    django_pages = [
        {'title': 'Official Django Tutorial',
         'url': 'https://docs.djangoproject.com/en/2.1/intro/tutorial01/',
         'views': 53456},
        {'title': 'Django Rocks',
         'url': 'http://www.djangorocks.com/',
         'views': 74579},
        {'title': 'How to Tango with Django',
         'url': 'http://www.tangowithdjango.com/',
         'views': 4892}]

    other_pages = [
        {'title': 'Bottle',
         'url': 'http://bottlepy.org/docs/dev/',
         'views': 9590},
        {'title': 'Flask',
         'url': 'http://flask.pocoo.org',
         'views': 8507}]

    cats = {'Python': {'pages': python_pages, 'views': 128, 'likes': 64},
            'Django': {'pages': django_pages, 'views': 64, 'likes': 32},
            'Other Frameworks': {'pages': other_pages, 'views': 32, 'likes': 16},
            'Pascal': {'pages': [], 'views': 3, 'likes': 1},
            'Perl': {'pages': [], 'views': 12, 'likes': 8},
            'PHP': {'pages': [], 'views': 43, 'likes': 32},
            'Prolog': {'pages': [], 'views': 11, 'likes': 5},
            'PostScript': {'pages': [], 'views': 9, 'likes': 2},
            'Programming': {'pages': [], 'views': 54, 'likes': 34},
            }

    # add the data
    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data.get('views'), cat_data.get('likes'))
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'], p['views'])

    # print the data added
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'-{c}:{p}')


def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p


def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c


if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
