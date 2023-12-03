from django.shortcuts import render
from django.views.generic import ListView
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import PictureForm
from .serializers import PictureSerializer
from .models import PictureFile


# class PictureListView(APIView):
#     def get(self, request):
#         picture_list = PictureFile.objects.all()
#         serializer = PictureSerializer(picture_list, many=True)
#         return Response(serializer.data)


# class PictureDetailView(APIView):
#     def get(self, request, id):
#         picture = PictureFile.objects.get(id=id)
#         serializer = PictureSerializer(picture)
#         return Response(serializer.data)
#
#
#     def delete(self, request, id):
#         picture = PictureFile.objects.get(id=id)
#         picture.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class DeletePicture(generics.RetrieveDestroyAPIView):
    serializer_class = PictureSerializer
    queryset = PictureFile.objects.all()
    lookup_field = 'id'


class PictureListView(generics.ListCreateAPIView):
    queryset = PictureFile.objects.all()
    serializer_class = PictureSerializer


class PictureDetail(generics.RetrieveAPIView):
    queryset = PictureFile.objects.all()
    serializer_class = PictureSerializer
    lookup_field = 'id'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = PictureSerializer(instance)
        return Response(serializer.data)


def image_upload(request):
    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form_img = form.instance
            return render(request, 'pictures_templates.html',
                          {'form': form, 'form_img': form_img})

    else:
        form = PictureForm()
    return render(request, 'pictures_templates.html', {'form': form})


class PictureList(ListView):
    model = PictureFile
    template_name = 'picture_list.html'
    context_object_name = 'pictures'
