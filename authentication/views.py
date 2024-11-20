from django.contrib.auth import authenticate, login as auth_login
from django.http import JsonResponse, HttpRequest


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
