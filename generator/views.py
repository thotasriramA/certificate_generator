from django.shortcuts import render
import google.generativeai as genai
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
from django.http import HttpResponse, JsonResponse

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Landing page
def index(request):
    return render(request, 'index.html')


# Home page after login
@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')
def signup(request):
    return render(request, 'signup.html')
def courses(request):
    return render(request, 'courses.html')
def login(request):
    return render(request, 'login.html')
def languages(request):
    return render(request, 'languages.html')

def roadmap(request):
    return render(request, 'roadmap.html')
def about(request):
    return render(request, 'about.html')

def fullstackdevelopment(request):
    return render(request, 'fullstackdevelopment.html')
def datanalysiscourse(request):
    return render (request, 'datanalysiscourse.html')
    
import json
from openai import OpenAI
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def chatbot(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_message = data.get('message', '')

            # ✅ Grok API
            client = OpenAI(
                api_key=settings.GROKE_API_KEY,
                base_url="https://api.x.ai/v1",
            )

            response = client.chat.completions.create(
                model="grok-3-mini",
                max_tokens=500,
                messages=[
                    {
                        "role": "system",
                        "content": """You are a helpful AI assistant for MyProject website.
MyProject is a free learning platform where students can:
- Watch free courses like Full Stack Development, Data Science, Cyber Security, AI/ML, Cloud Computing, DevOps, UI/UX Design, Mobile App Development.
- Complete courses and generate certificates.
- Learn programming languages and follow roadmaps.

Rules:
- Always reply in the same language the user is typing in.
- If user types in Telugu, reply in Telugu.
- If user types in English, reply in English.
- Be friendly, helpful and keep answers short and clear.
- Only help with course and learning related questions."""
                    },
                    {
                        "role": "user",
                        "content": user_message
                    }
                ]
            )

            bot_reply = response.choices[0].message.content
            return JsonResponse({'reply': bot_reply})

        except Exception as e:
            print("Chatbot error:", e)
            return JsonResponse({'reply': f'ERROR: {str(e)}'})

    return JsonResponse({'reply': 'Invalid request'})
