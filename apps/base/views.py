from django.http import HttpResponse
from datetime import datetime


def home_page(request):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return HttpResponse(
        f"Welcome! This is the homepage of homework №10 (Kubarev Aleksey).<br>"
        f"The current time in Kyiv is: {time}<br>"
        f"You can generate an example of a possible username and email address by going to '/generate-users/'"
        f"you can also specify the required number of examples by entering '/generate-users/number'"
    )
