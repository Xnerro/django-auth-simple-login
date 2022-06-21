from django.db.models import CharField, EmailField, BooleanField, DateTimeField, Model

# Create your models here.


class Account(Model):
    fname = CharField(max_length=250)
    lname = CharField(max_length=250)
    email = EmailField(unique=True, max_length=100)
    username = CharField(unique=True, max_length=250)
    password = CharField(max_length=100)
    create_at = DateTimeField(auto_now_add=True)
    last_login = DateTimeField(auto_now=True)
    is_admin = BooleanField(default=False)
    is_active = BooleanField(default=True)
