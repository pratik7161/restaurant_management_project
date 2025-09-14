from django.shortcuts import render

def  faq(request):
    faqs = [
        {"question":"what are your opening hours?", "answer": "we are open daily" },
        {"question":"do you offer home delivery?", "answer": "yes , we provide it 24/7 "},
        {"question":"do you accept online payments?", "answer": "yes , but if customer doesn't have cash money"},
        {"question": "do you offer vegetarian options?", "answer":"yes , offcourse"}
        ]
        return render(request,"faq.html",{"faqs": faqs})
def format_datetime(value, format_string="%A,%B,%C,%Y,%I"):
    """formats a datetime object using the given format string."""
    if not value:
        value = timezone.now()
    return value.strftime(format_string)

+
from django.shortcuts import render
def privacy_policy(request):
    return render(request, "privacy_policy.html")

{% block content %}
<div class="container" style="max-width:800px; margin:50px auto; padding:20px; background:#f9f9f9; border-radius:10px;"
     <h2 style="text-align: center; margin-bottom:20px;">Privacy Policy</h2>
     <p>We value your Privacy. This Privacy policy outline how our restaurant websites collect,uses, and protects your information.</p>    