import jwt
import json
from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from .auth_service import AuthService
from django.views.decorators.csrf import csrf_exempt
from utils.middlewares.middleware import auth_required


@csrf_exempt
def signup(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            name = data.get("name")
            email = data.get("email")
            password = data.get("password")

            if not name or not email or not password:
                return JsonResponse({"error": "All fields are required"}, status=400)

            if AuthService.get_user_by_email(email):
                return JsonResponse({"error": "Email already exists"}, status=400)

            user = AuthService.create_user(name, email, password)
            return JsonResponse(
                {"message": "User created successfully", "user_id": user.id}, status=201
            )

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON payload"}, status=400)
    return JsonResponse({"error": "Invalid HTTP method"}, status=405)


@csrf_exempt
def login(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            email = data.get("email")
            password = data.get("password")

            if not email or not password:
                return JsonResponse({"error": "All fields are required"}, status=400)

            user = AuthService.get_user_by_email(email)
            if not user or not AuthService.check_password(password, user.password):
                return JsonResponse({"error": "Invalid credentials"}, status=401)

            token = AuthService.generate_token(user.id)
            return JsonResponse(
                {"message": "Login successful", "token": token}, status=200
            )

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON payload"}, status=400)
    return JsonResponse({"error": "Invalid HTTP method"}, status=405)


@auth_required
def auth_me(request):
    if request.method == "GET":
        user = request.user
        return JsonResponse(
            {"user": {"id": user.id, "name": user.name, "email": user.email}},
            status=200,
        )
    return JsonResponse({"error": "Invalid HTTP method"}, status=405)
