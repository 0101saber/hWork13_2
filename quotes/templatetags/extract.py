from django import template
from bson.objectid import ObjectId

from ..models import Author, Quote
from ..utils import get_mongo_db

register = template.Library()


def get_author(id_):
    author = Author.objects.get(id=id_)
    if not author:
        return 'No such author'
    return author['fullname']


register.filter('author', get_author)
