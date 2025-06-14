from django.db import models
from django.utils.html import strip_tags
from django.utils.text import Truncator
from wagtail.admin.panels import MultiFieldPanel, FieldPanel

from wagtail.models import Page
from wagtail.fields import RichTextField

from wagtail.search import index


class TopicMainPage(Page):
    background_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Main background image of the Topic Main Page."
    )

    name = models.CharField(
        blank=True,
        max_length=255,
        help_text="Write the title of the new topic. For example, 'Verbs'"
    )
    description = models.CharField(
        blank=True,
        max_length=255,
        help_text="Write a short description of the new topic."
    )

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        topicpages = self.get_children().live().order_by('-first_published_at')
        context['topicpages'] = topicpages
        return context

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [

                FieldPanel("background_image"),
                FieldPanel("name"),
                FieldPanel("description"),
            ],
            heading="Header Section",
        ),
    ]

class TopicPage(Page):
    date = models.DateField("Post date")
    body = RichTextField(blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('title'),
        index.SearchField('body'),
    ]

    def get_body_preview(self):
        body_string = strip_tags(self.body)
        return Truncator(body_string).chars(50)

    def get_context(self, request):
        context = super().get_context(request)

        parent_page = self.get_parent(update=False)
        context["parent_page"] = parent_page

        body_preview = self.get_body_preview
        context["body_preview"] = body_preview

        return context

    content_panels = Page.content_panels + ["date", "body"]



