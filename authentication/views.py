from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST


@csrf_exempt
@require_POST
def login(request: HttpRequest):
    username = request.POST.get("username")
    password = request.POST.get("password")

    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            return JsonResponse(
                {
                    "username": user.username,
                    "status": True,
                    "message": "Login success!",
                },
                status=200,
            )
        else:
            return JsonResponse(
                {"status": False, "message": "Login failed!"}, status=401
            )
    else:
        return JsonResponse({"status": False, "message": "Login invalid!"}, status=401)


@csrf_exempt
@require_POST
def register(request: HttpRequest):
    username = request.POST.get("username")
    password = request.POST.get("password")
    password_confirmation = request.POST.get("password_confirmation")

    if password != password_confirmation:
        return JsonResponse(
            {"status": False, "message": "Your passwords didn't match!"}, status=400
        )

    if User.objects.filter(username=username).exists():
        return JsonResponse(
            {"status": False, "message": "Username already exists!"}, status=400
        )

    new_user = User.objects.create_user(username=username, password=password)
    new_user.save()

    return JsonResponse(
        {"status": True, "message": "User successfully created!"}, status=201
    )
