from blog.models import TopicMainPage
from wagtail.models import Site

def global_variables(request):
    topics = TopicMainPage.objects.live()


    site = Site.objects.get(is_default_site=True)
    root_page_children = site.root_page.get_children().live()

    return {
        'topic_main_pages': topics,
        'default_site':site,
        'root_page_children':root_page_children
    }