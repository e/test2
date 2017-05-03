from rest_framework import viewsets, status
from rest_framework.response import Response
from resolutions.models import Resolution
from resolutions.serializers import ResolutionSerializer


class ResolutionViewSet(viewsets.ModelViewSet):
    """
    API endpoint to view/edit resolutions
    """
    queryset = Resolution.objects.all()
    serializer_class = ResolutionSerializer

    def get_queryset(self):
        return Resolution.objects.filter(user=self.request.user)

    def update(self, request, *args, **kwargs):
        return super(ResolutionViewSet, self).update(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj = serializer.save()
        obj.user = request.user
        obj.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def put(self, request):
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
