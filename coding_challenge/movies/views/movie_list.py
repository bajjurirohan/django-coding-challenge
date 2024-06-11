from rest_framework.generics import ListCreateAPIView

from movies.models import Movie
from movies.serializers import MovieSerializer


class MovieListView(ListCreateAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        queryset = Movie.objects.order_by("id")

        runtime = self.request.query_params.get('runtime')
        filter_type = self.request.query_params.get('filter')  # 'longer' or 'shorter'


        if runtime and filter_type:
            runtime = int(runtime)
            if filter_type == 'longer':
                queryset = queryset.filter(runtime__gt=runtime)
            elif filter_type == 'shorter':
                queryset = queryset.filter(runtime__lt=runtime)

        return queryset