
from words.models import Expression, Group, Language


# TODO paginacja

def words_search(request, exp, group=None, lang=None):
    # select only user words
    query = Expression.objects.filter(groups__user=request.user)

    query = query.filter(key__icontains=exp)

    if lang is not None:
        query = query.filter(groups__language=lang)

    if group is not None:
        query = query.filter(groups=group)
        # list of groups or one group??

    query = query.order_by('key')
    return query


def group_search(request, group_id, lang=None):

    query = Group.objects.filter(user=request.user)
    query = query.filter(id=group_id)

    if lang is not None:
        query = query.filter(language=lang)

    query = query.order_by('name')
    return query
