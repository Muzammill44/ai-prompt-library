from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Prompt
import json

# ✅ ADD THESE IMPORTS
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])   # 🔐 PROTECTED
def prompt_list(request):

    if request.method == 'GET':
        prompts = Prompt.objects.all().order_by('-id').values()
        return JsonResponse(list(prompts), safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)

        prompt = Prompt.objects.create(
            title=data.get('title'),
            content=data.get('content'),
            complexity=data.get('complexity')
        )

        return JsonResponse({
            "id": prompt.id,
            "title": prompt.title,
            "content": prompt.content,
            "complexity": prompt.complexity,
            "created_at": prompt.created_at
        })


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])   # 🔐 PROTECTED
def prompt_detail(request, id):

    try:
        prompt = Prompt.objects.get(id=id)
    except Prompt.DoesNotExist:
        return JsonResponse({"error": "Not found"}, status=404)

    if request.method == 'GET':
        return JsonResponse({
            "id": prompt.id,
            "title": prompt.title,
            "content": prompt.content,
            "complexity": prompt.complexity,
            "created_at": prompt.created_at
        })

    elif request.method == 'PUT':
        data = json.loads(request.body)

        prompt.title = data.get('title', prompt.title)
        prompt.content = data.get('content', prompt.content)
        prompt.complexity = data.get('complexity', prompt.complexity)
        prompt.save()

        return JsonResponse({"message": "Updated"})

    elif request.method == 'DELETE':
        prompt.delete()
        return JsonResponse({"message": "Deleted"})