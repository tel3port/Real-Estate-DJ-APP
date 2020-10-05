import os
import random
from random import randint

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from .models import Entry


def get_random_cta_image():
    cta_image_list = [
        'watch.gif',
        'a.gif',
        'b.gif',
        'c.gif',
        'd.gif',
        'e.gif',
        'f.gif',
        'g.gif',
        'h.gif',
        'i.gif',
    ]
    return cta_image_list[randint(0, len(cta_image_list) - 1)]


def get_random_conj():
    conj_list = [
        'and',
        'A minute later',
        'Accordingly',
        'Actually',
        'After',
        'After a short time',
        'Afterward',
        'Also',
        'And',
        'Another',
        'As an example',
        'As a consequence',
        'As a result',
    ]

    return conj_list[randint(0, len(conj_list) - 1)].lower()


def random_image():
    path = r"./media/"
    rand_img = random.choice([
        x for x in os.listdir(path)
        if os.path.isfile(os.path.join(path, x))
    ])

    return rand_img


url_list = [
    'https://afflat3d1.com/lnk.asp?o=9075&c=918277&a=242672&k=EBF2EDB942180C1F39AC57CE3994F57C&l=8504',
    'https://afflat3d1.com/lnk.asp?o=18084&c=918277&a=242672&k=580FAC50554E1E3F5AACC583D06DE0AD&l=19332',
    'https://afflat3d1.com/lnk.asp?o=18099&c=918277&a=242672&k=89F4A996358DADE546AA2BF166C9A7F9&l=19340',
    'https://afflat3d1.com/lnk.asp?o=18095&c=918277&a=242672&k=C12104E1F23E5C340EAF089395EBD125&l=19345',
    'https://afflat3d1.com/lnk.asp?o=18627&c=918277&a=242672&k=B97D03D349CE4FE1BE27D635A16AD24B&l=19818',
    'https://afflat3d1.com/lnk.asp?o=19322&c=918277&a=242672&k=F5A185D25CB8289CD91DF3803D395C64&l=20323',
    'https://afflat3d1.com/lnk.asp?o=19594&c=918277&a=242672&k=30F2E776196A860C8FE3BBDE6D69D334&l=20556',
    'https://afflat3d1.com/lnk.asp?o=7527&c=918277&a=242672&k=956D04E486409DA8ED5528F3448FB86F&l=6239',
    'https://afflat3d1.com/lnk.asp?o=10721&c=918277&a=242672&k=18DBF0EF0820E9FDB52660B31C464213&l=10603',
    'https://afflat3d1.com/lnk.asp?o=18174&c=918277&a=242672&k=29DA121E59E0456E7F1B9D705D276327&l=19429',
]
headline_list = [
    'Forecasters call for weather on Monday',
    'Amphibious pitcher makes debut',
    'Cows lose their jobs as milk prices drop',
    'Miracle cure kills fifth patient',
    'Man Accused of Killing Lawyer Receives a New Attorney',
    'State population to double by 2040, babies to blame',
    'Missippis literacy program shows improvement',
    'Breathing oxygen linked to staying alive',
    'Police arrest everyone on February 22nd',
    'Thursday is cancelled',
    'Bridge closure date: Thursday or October',
    'Most Earthquake Damage is Caused by Shaking',
    'Federal Agents Raid Gun Shop, Find Weapons',
    'Safety meeting ends in accident',
    'Muddy Creek Problem: Its too muddy',
    'Murderer says detective ruined his reputation',
    'Utah Poison Control Center reminds everyone not to take poison',
    'Bugs flying around with wings are flying bugs',
    'Students Cook & Serve Grandparents',
    'Alton attorney accidentally sues himself',
    'Hospitals resort to hiring doctors',
    'Farmer using cannon to protect watermelons',
    'Voters to vote on whether to vote',
    'Museums full of history',
    'Goat accused of robbery',
]

sidebar_info_list = [
    [headline_list[randint(0, len(headline_list) - 1)], random_image(), url_list[randint(0, len(url_list) - 1)]],
    [headline_list[randint(0, len(headline_list) - 1)], random_image(), url_list[randint(0, len(url_list) - 1)]],
    [headline_list[randint(0, len(headline_list) - 1)], random_image(), url_list[randint(0, len(url_list) - 1)]],
    [headline_list[randint(0, len(headline_list) - 1)], random_image(), url_list[randint(0, len(url_list) - 1)]],
    [headline_list[randint(0, len(headline_list) - 1)], random_image(), url_list[randint(0, len(url_list) - 1)]],
    [headline_list[randint(0, len(headline_list) - 1)], random_image(), url_list[randint(0, len(url_list) - 1)]],
    [headline_list[randint(0, len(headline_list) - 1)], random_image(), url_list[randint(0, len(url_list) - 1)]],
    [headline_list[randint(0, len(headline_list) - 1)], random_image(), url_list[randint(0, len(url_list) - 1)]],
    [headline_list[randint(0, len(headline_list) - 1)], random_image(), url_list[randint(0, len(url_list) - 1)]],
    [headline_list[randint(0, len(headline_list) - 1)], random_image(), url_list[randint(0, len(url_list) - 1)]],
    [headline_list[randint(0, len(headline_list) - 1)], random_image(), url_list[randint(0, len(url_list) - 1)]],
    [headline_list[randint(0, len(headline_list) - 1)], random_image(), url_list[randint(0, len(url_list) - 1)]],
    [headline_list[randint(0, len(headline_list) - 1)], random_image(), url_list[randint(0, len(url_list) - 1)]],
    [headline_list[randint(0, len(headline_list) - 1)], random_image(), url_list[randint(0, len(url_list) - 1)]],
    [headline_list[randint(0, len(headline_list) - 1)], random_image(), url_list[randint(0, len(url_list) - 1)]],
    [headline_list[randint(0, len(headline_list) - 1)], random_image(), url_list[randint(0, len(url_list) - 1)]],
    [headline_list[randint(0, len(headline_list) - 1)], random_image(), url_list[randint(0, len(url_list) - 1)]],
    [headline_list[randint(0, len(headline_list) - 1)], random_image(), url_list[randint(0, len(url_list) - 1)]],
    [headline_list[randint(0, len(headline_list) - 1)], random_image(), url_list[randint(0, len(url_list) - 1)]],
    [headline_list[randint(0, len(headline_list) - 1)], random_image(), url_list[randint(0, len(url_list) - 1)]],
    [headline_list[randint(0, len(headline_list) - 1)], random_image(), url_list[randint(0, len(url_list) - 1)]],
    [headline_list[randint(0, len(headline_list) - 1)], random_image(), url_list[randint(0, len(url_list) - 1)]],
    [headline_list[randint(0, len(headline_list) - 1)], random_image(), url_list[randint(0, len(url_list) - 1)]],
    [headline_list[randint(0, len(headline_list) - 1)], random_image(), url_list[randint(0, len(url_list) - 1)]],
    [headline_list[randint(0, len(headline_list) - 1)], random_image(), url_list[randint(0, len(url_list) - 1)]],
]


class HomeView(ListView):
    model = Entry
    template_name = 'blog/index.html'
    context_object_name = "blog_entries"
    ordering = ['-entry_date']
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sidebar_things'] = sidebar_info_list

        return context


def divide_string(mystring):
    word_list = mystring.split(" ")
    str_len = len(word_list)
    mid_index = int(str_len / 2)
    str_1 = ""
    str_2 = ""
    for ix in range(mid_index):
        str_1 += word_list[ix] + " "

    for iy in range(mid_index, str_len):
        str_2 += word_list[iy] + " "

    return str_1, str_2


def single_post(request, slug):
    template = 'blog/entry_detail.html'
    posts = Entry.objects.all()
    print("num of posts: ", len(posts))
    s_post = Entry.objects.get(slug=slug)
    single_author = s_post.entry_author
    single_date = s_post.entry_date
    single_title = s_post.entry_title
    my_string = s_post.entry_text
    my_sub_id = s_post.site_sub_id
    my_kws = s_post.entry_tags

    my_desc = "this site is about" + my_kws.replace(',', ' and ')

    str_1 = divide_string(my_string)[0]
    str_2 = divide_string(my_string)[1]

    # to remove the last sentence from tha article that has keywords

    stuff_for_single_post = {
        "title": single_title,
        "text_1": str_1,
        "text_2": str_2,
        "author": single_author,
        "date": single_date,
        "rand_cta_im": get_random_cta_image(),
        'rand_im_1': random_image(),
        'rand_im_2': random_image(),
        'rand_thumb': random_image(),
        'rand_url': url_list[randint(0, len(url_list) - 1)],
        "sidebar_things": sidebar_info_list,
        'tags': my_kws,
        'desc': my_desc,
        'sub_id': my_sub_id
    }
    return render(request, template, context=stuff_for_single_post)


# CLASSES NOT IN USE!
class CreateEntryView(CreateView):
    model = Entry
    template_name = 'blog/create_entry.html'
    fields = ['entry_title', 'entry_text']

    def form_valid(self, form):
        form.instance.entry_author = self.request.user
        return super().form_valid(form)


class EntryView(DetailView):
    model = Entry
    slug_field = 'slug'
    template_name = 'blog/entry_detail.html'
    data_set = random_image()
    stuff_for_post = {

        "info": data_set
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rand_im'] = random_image()

        return context
