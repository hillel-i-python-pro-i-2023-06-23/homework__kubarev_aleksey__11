from datetime import datetime
import random

from django.shortcuts import render


def home_page(request):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return render(
        request=request,
        template_name="base/home_page.html",
        context={
            "greetings_text": f"Welcome! This is the homepage of homework №12." f"The current time in Kyiv is: {time}",
            "nested": {
                "random_number": random.randint(1, 100),
            },
            "title": "Home page",
        },
    )
