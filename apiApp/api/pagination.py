from rest_framework.pagination import PageNumberPagination


class WatchListPagination(PageNumberPagination):

    page_size = 5
    page_query_param = 'p' # results - 'p' will reflect instead of 'pages' in url
    page_size_query_param = 'size'
    max_page_size = 10
    last_page_strings = 'last' # directly go to last page upon click