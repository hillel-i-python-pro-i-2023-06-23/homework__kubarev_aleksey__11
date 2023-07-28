from django.shortcuts import render
from datetime import datetime


def home_page(request):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return render(
        request=request,
        template_name="base/home_page.html",
        context={
            "greetings_text": f"Welcome! This is the homepage of homework №11."
        f"The current time in Kyiv is: {time}",
            "title": "Home page",
        },
    )