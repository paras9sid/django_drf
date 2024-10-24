from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination


class WatchListPagination(PageNumberPagination):

    page_size = 5
    page_query_param = 'p' # results - 'p' will reflect instead of 'pages' in url
    page_size_query_param = 'size'
    max_page_size = 10
    last_page_strings = 'last' # directly go to last page upon click


class WatchListLimitOS(LimitOffsetPagination):
    default_limit = 5
    max_limit = 10
    limit_query_param = 'limit'
    offset_query_param = 'start'

class WatchListCursorPag(CursorPagination):
    page_size = 5
    ordering = 'created'
    cursor_query_param = 'record'