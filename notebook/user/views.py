from django.shortcuts import render

from .models import User


def all_users(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'all_users.html', context)

def user_details(request, id):
    user = User.objects.get(id=id)
    return render(request, 'user_details.html', {'user': user})