import jwt
from django.http import JsonResponse
from auth_manager.auth_service import AuthService


def auth_required(view_func):
    def wrapper(request, *args, **kwargs):
        auth_header = request.headers.get("Authorization")

        if not auth_header or not auth_header.startswith("Bearer "):
            return JsonResponse(
                {"error": "Unauthorized: No token provided"}, status=401
            )

        token = auth_header.split(" ")[1]
        try:
            payload = AuthService.decode_token(token)
            user = AuthService.get_user_by_id(payload["user_id"])
            if not user:
                return JsonResponse(
                    {"error": "Invalid token: User not found"}, status=401
                )

            request.user = user  # Attach user to the request
        except jwt.ExpiredSignatureError:
            return JsonResponse({"error": "Token has expired"}, status=401)
        except jwt.InvalidTokenError:
            return JsonResponse({"error": "Invalid token"}, status=401)

        return view_func(request, *args, **kwargs)

    return wrapper
