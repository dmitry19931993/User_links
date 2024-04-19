from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Link, Collection
from .serializers import LinkSerializer, CollectionSerializer
from .utils import take_link_info



class LinkAPIView(APIView):
    """CRUD для сылок"""

    def get(self, request):
        links = Link.objects.filter(user_id=request.user)
        if links:
            return Response(LinkSerializer(links, many=True).data)
        else:
            return Response("Нет созданных ссылок")

    def post(self, request):
        link = request.data.get("link")
        data = take_link_info(link)
        if data:
            serializer = LinkSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            link_new = Link.objects.create(
                title=data["title"],
                description=data["description"],
                link=data["link"],
                image=data["image"],
                type=data["type"],
                user_id=request.user,
            )
            return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error":"Method PUT not Allowed"})

        try:
            instance = Link.objects.get(pk=pk)

        except:
            return Response({"error":"Object does not exist"})
        if instance.user_id == request.user:
            link = request.data.get("link")
            data = take_link_info(link)
            if data:
                serializer = LinkSerializer(data=data)
                serializer.is_valid(raise_exception=True)
                link_update = Link.objects.filter(pk=pk).update(
                    title=data["title"],
                    description=data["description"],
                    link=data["link"],
                    image=data["image"],
                    type=data["type"],
                )
                return Response(serializer.data)
        else:
            return Response({"error": "Choose other pk"})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error":"Method Delete not Allowed"})

        try:
            instance = Link.objects.get(pk=pk)

        except:
            return Response({"error":"Object does not exist"})
        if instance.user_id == request.user:
                link_delete = Link.objects.filter(pk=pk).delete()
                return Response({f"delete link {pk}"})
        else:
            return Response({"error": "Choose other pk"})


class CollectionAPIView(APIView):
    """CRUD для коллекций"""

    def get(self, request):
        collections = Collection.objects.filter(user_id=request.user)
        if collections:
            return Response(CollectionSerializer(collections, many=True).data)
        else:
            return Response("Нет созданных ссылок")

    def post(self, request):
        serializer = CollectionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        collection_new = Collection.objects.create(
            name=request.data["name"],
            description=request.data["description"],
            user_id=request.user,
        )
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error":"Method PUT not Allowed"})

        try:
            instance = Collection.objects.get(pk=pk)

        except:
            return Response({"error":"Object does not exist"})
        if instance.user_id == request.user:
            serializer = CollectionSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            collection_update = Collection.objects.filter(pk=pk).update(
                name=request.data["name"],
                description=request.data["description"],
            )
            return Response(serializer.data)
        else:
            return Response({"error": "Choose other pk"})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error":"Method PUT not Allowed"})

        try:
            instance = Collection.objects.get(pk=pk)

        except:
            return Response({"error":"Object does not exist"})
        if instance.user_id == request.user:
            collection_delete = Collection.objects.filter(pk=pk).delete()
            return Response({f"Delete collection {pk}"})
        else:
            return Response({"error": "Choose other pk"})