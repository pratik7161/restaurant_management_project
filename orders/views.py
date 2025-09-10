from django.shortcuts import render

def  faq(request):
    faqs = [
        {"question":"what are your opening hours?", "answer": "we are open daily" },
        {"question":"do you offer home delivery?", "answer": "yes , we provide it 24/7 "},
        {"question":"do you accept online payments?", "answer": "yes , but if customer doesn't have cash money"},
        {"question": "do you offer vegetarian options?", "answer":"yes , offcourse"}
        ]
        return render(request,"faq.html",{"faqs": faqs})
