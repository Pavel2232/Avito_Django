from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import pagination, viewsets, status

from ads.models import Ad
from ads.serializers import AdSerializer,AdDetailSerializer
from rest_framework.generics import ListAPIView,   get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


from ads.permissions import AdsPermission

from ads.models import Comment

from ads.serializers import CommentSerializer

from ads.permissions import CommentPermission

from ads.filters import AdFilter


class AdPagination(pagination.PageNumberPagination):
    pass


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all().order_by('-created_at')
    serializer_class = AdSerializer
    permission_classes = [AdsPermission]
    filter_backends = [DjangoFilterBackend,]
    filterset_class = AdFilter


    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = AdDetailSerializer(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save(author = self.request.user)
    def partial_update(self,request, *args, **kwargs):
        super().partial_update(request)
        return Response(AdDetailSerializer(self.get_object()).data)

class Ad_by_User(ListAPIView):
    permission_classes = [IsAuthenticated]
    def get(self,request, *args, **kwargs):
        result = Ad.objects.filter(author__exact = request.user.id)
        serializer = AdDetailSerializer(result,many=True)
        return self.get_paginated_response(self.paginate_queryset(serializer.data))


class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all().select_related('ad')
    serializer_class = CommentSerializer
    permission_classes = [CommentPermission]

    def get_queryset(self,*args, **kwargs):
        as_ad = self.kwargs.get('ad_pk')
        ad = get_object_or_404(Ad, pk= as_ad)

        return  self.queryset.filter(ad= ad)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save(author = self.request.user,ad=get_object_or_404(Ad, pk= self.kwargs.get('ad_pk')))

    def partial_update(self,request, *args, **kwargs):
        super().partial_update(request)
        return Response(self.serializer_class(self.get_object()).data)

    @method_decorator(csrf_exempt, name='dispatch')
    class Image(UpdateView):
        model = Ad

        def post(self, request, *args, **kwargs):
            self.object = self.get_object()

            self.object.image = request.FILES['image']
            self.object.save()

            return Response({
                "id": self.object.id,
                "name": self.object.name,
                "image": self.object.image.url if self.object.image else None,

            })



