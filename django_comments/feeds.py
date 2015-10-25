from django.contrib.syndication.views import Feed
from django.utils.translation import ugettext as _

import django_comments

class LatestCommentFeed(Feed):

    def __call__(self, request, *args, **kwargs):
        return super(LatestCommentFeed, self).__call__(request, *args, **kwargs)

    def title(self):
        return _("Comments") 

    def link(self):
        return "#" 

    def description(self):
        return "Latest comments"

    def items(self):
        qs = django_comments.get_model().objects.filter(
            is_public=True,
            is_removed=False,
        )
        return qs.order_by('-submit_date')[:40]

    def item_pubdate(self, item):
        return item.submit_date
