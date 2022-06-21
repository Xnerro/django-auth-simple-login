from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password, check_password

from ..models import Account
from .auth import user_token
from ..forms import RegisterForm
from .__init__ import *

# Create your views here.


def login(request):
    if request.method == "POST":
        try:
            username = request.POST["username"]
            password = request.POST["password"]
            user = Account.objects.filter(username=username).first()
            if user is None:
                return JsonResponse({"msg": "Username not found"}, status=404)
            if check_password(password, user.password):
                key = os.environ["SECRET_KEY"]
                algorithm = os.environ["JWT_ALGORITHM"]
                token = jwt.encode(
                    {"token": "jwt", "user_id": user.id, "exp": datetime.utcnow() + timedelta(days=14)},
                    key,
                    algorithm=algorithm,
                )
                request.session["x"] = token
                # return JsonResponse({"msg": request.session.get("x")})
                return redirect("home")
            return JsonResponse({"msg": "invalid password"})
        except KeyError as e:
            return JsonResponse({"message": f"KEY_ERROR: {e}"}, status=400)
    return render(request, "login.html")


@csrf_exempt
def register(request):
    if request.method == "POST":
        req = request.POST
        form = RegisterForm(req)
        if form.is_valid:
            pw = make_password(req["password"])
            Account.objects.create(
                fname=req["fname"], lname=req["lname"], username=req["username"], email=req["email"], password=pw
            )
            return JsonResponse({"msg": "registered"})
        return JsonResponse({"msg": "failed to registered"})
    return render(request, "register.html")


def home(request):
    token = user_token(request, request.session.get("x"))
    try:
        if "token" in token.keys():
            return JsonResponse({"msg": "awww"})
        else:
            return JsonResponse({"msg": "shuuuuu"})
    except:
        return token


def logout(request):
    try:
        del request.session["x"]
    except:
        pass
    return redirect("login")
