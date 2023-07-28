from django.http import HttpResponse

from apps.homework.services.users_generator import generate_list_of_users, output_info


def generate_users(request, amount: int = 100):
    formatted_users = generate_list_of_users(amount)
    output = output_info(formatted_users)
    return HttpResponse(f"You generate {amount} variants of users name and email: <ol>{output}</ol>")
