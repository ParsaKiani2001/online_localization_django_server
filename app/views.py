from rest_framework import  status
from rest_framework.views import APIView
from .models import LanguageModel, DictionaryModel
from .serializer import LanguageSerializer, DictionarySerializer
from rest_framework.response import Response

class LanguagesViewSet(APIView):
    queryset = LanguageModel
    serializer_class = LanguageSerializer

    def put(self, request):
        try:
            lang_id = request.data.get('id')
            query = LanguageModel.objects.filter(id=lang_id)
            if not query.exists():
                return Response({"error": "No data found. ID might be incorrect."},
                                status=status.HTTP_204_NO_CONTENT)
            instance = query.last()
            serializer = self.serializer_class(instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request):
        version = request.query_params.get('version')
        if version is None:
            serializer = self.serializer_class(self.queryset.objects.all(), many=True)
        else:
            serializer = self.serializer_class(LanguageModel.objects.filter(version=version),many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DictionaryViewSet(APIView):
    queryset = DictionaryModel
    serializer_class = DictionarySerializer

    def put(self, request):
        serialize = self.serializer_class(data= request.data)
        if serialize.is_valid():
            try:
                selected_data = DictionaryModel.objects.filter(keys=serialize.validated_data['keys'],local=serialize.validated_data['local'])
                if len(selected_data) == 0:
                    return Response({"error": str('this data not found.keys or local must be incorrect')}, status=status.HTTP_400_BAD_REQUEST)
                serialize.update(validated_data=serialize.validated_data, instance=selected_data.last())
                return Response(serialize.data, status=status.HTTP_204_NO_CONTENT)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        serializer = self.serializer_class(self.queryset.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class DictionaryDetailViewSet(APIView):
    queryset = DictionaryModel
    serializer_class = DictionarySerializer

    def get(self, request,pk):
        data = {}
        vrt = request.GET.get('version')
        if vrt is None:
            vrt = 1
        for item in self.queryset.objects.filter(local__name=pk,local__version=vrt):
            data[item.keys] = item.values
        return Response(data, status=status.HTTP_200_OK)

