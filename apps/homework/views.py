from django.shortcuts import render
from apps.homework.services.users_generator import generate_list_of_users, output_info

def users_generator_view(request, amount=100):
    users_list = generate_list_of_users(amount)
    output = output_info(users_list)
    return render(request, 'homework/users_generator.html', {'users_list': output})
