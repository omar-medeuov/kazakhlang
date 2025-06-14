from django.db import models
from wagtail.admin.panels import FieldPanel, MultiFieldPanel

from wagtail.models import Page
from wagtail.fields import RichTextField

from blog.models import TopicMainPage, TopicPage


# HomePage following the wagtail tutorial:
class HomePage(Page):
    background_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Main background image of the Homepage."
    )
    header_title = models.CharField(
        blank=True,
        max_length=255,
        help_text="Write a short slogan for the website's Homepage."
    )
    header_subtitle = models.CharField(
        blank=True,
        max_length=255,
        help_text="Write a supporting short text that will sit below the title."
    )

    body = RichTextField(blank=True)

    def get_context(self, request):
        context = super().get_context(request)

        latest_topic_pages = TopicPage.objects.none()

        for topic_main_page in self.get_children().type(TopicMainPage).live().specific():
            latest_topic_pages = topic_main_page.get_children().type(TopicPage).live().specific()

        # latest_topic_pages = (self.get_children().type(TopicMainPage).live().specific()
        #                       .get_children().live().order_by('-first_published_at'))
        context["latest_topic_pages"] = latest_topic_pages
        return context


    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [

        FieldPanel("background_image"),
        FieldPanel("header_title"),
        FieldPanel("header_subtitle"),
        ],
        heading="Header Section",
    ),
        FieldPanel("body"),

    ]


