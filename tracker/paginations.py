from rest_framework.pagination import PageNumberPagination


class SimplePagination(PageNumberPagination):
    page_size = 10
<<<<<<< HEAD:RoadScan/tracker/paginations.py
    page_size_query_param = 'page_size'
=======
    page_size_query_param = 'page_size'
>>>>>>> 36d2f2dbe56a8de0d6b7f133fb27ce44d993f839:tracker/paginations.py
