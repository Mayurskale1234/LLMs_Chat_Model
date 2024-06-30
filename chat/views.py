
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .huggingface_models import HuggingFaceModel
from django.conf import settings
from pymongo.errors import OperationFailure

@csrf_exempt
def chat_view(request):
    response = ''
    chat_history = []

    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')
        model_name = request.POST.get('model_name', 'gpt2')
        max_length = int(request.POST.get('max_length', 100))
        model = HuggingFaceModel()
        response = model.generate_response(user_input, model_name, max_length)

        # Saveing to MongoDB
        try:
            settings.MONGO_DB.chat_history.insert_one({
                'model': model_name,
                'input': user_input,
                'response': response,
            })
        except OperationFailure as e:
            print(f"MongoDB Error: {e}")

    return render(request, 'chat/chat.html', {
        'response': response,
        'chat_history': chat_history
    })


def chat_history(request):
    history = settings.MONGO_DB.chat_history.find()
    chat_history = []
    for entry in history:
        chat_history.append({
            'model': entry['model'],
            'input': entry['input'],
            'response': entry['response']
        })

    return render(request, 'chat/history.html', {'chat_history': chat_history})

