import os
from django.http import JsonResponse

import jwt
from ..models import Account


def user_token(request, token):
    try:
        # token = request.headers.get('token')
        key = os.environ["SECRET_KEY"]
        algorithm = os.environ["JWT_ALGORITHM"]

        if token is None:
            return JsonResponse({"message": "INVALID_TOKEN"}, status=401)
        else:
            decode = jwt.decode(token, key, algorithms=algorithm)
            request.user = Account.objects.get(id=decode["user_id"])
            return {"token": token}

    except jwt.ExpiredSignatureError:
        return JsonResponse({"message": "EXPIRED_TOKEN"}, status=400)
