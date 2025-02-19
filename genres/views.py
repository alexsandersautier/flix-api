import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from genres.models import Genre

@csrf_exempt
def gender(request):

    if request.method == 'GET': 
        genres = Genre.objects.all()
        data = [{'id': genre.id, 'name': genre.name} for genre in genres]
        return JsonResponse(data, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        new_gender = Genre(name=data['name'])
        new_gender.save()
        return JsonResponse(
            {
                "id": new_gender.id,
                "name": new_gender.name
            },
            status=201
        )    

@csrf_exempt
def gender_detail_view(request, pk):
    genre = get_object_or_404(Genre, pk=pk)
    if request.method == 'GET':
        return JsonResponse(
            {'id': genre.id, 'name': genre.name}
        )
    elif request.method == 'PUT':
        data = json.loads(request.body.decode('utf-8'))
        genre.name = data['name']
        genre.save()
        return JsonResponse(
            {
                "id": genre.id,
                "name": genre.name
            },
            status=201
        )    
    
    elif request.method == 'DELETE':
        genre.delete()
        return JsonResponse(
            {f'message': 'Gênero excluído'},
            status=204
        )