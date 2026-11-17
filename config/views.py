from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .models import Activity, Club
from .scripts import mail


def home_view(request):
    sent = False

    if request.method == "POST":
        message = request.POST.get("message", "").strip()
        email = request.POST.get("email", "").strip()

        try:
            mail.contact_mail(mail=email, message=message)
            sent = True
        except Exception as exc:
            print("BŁĄD WYSYŁKI MAILA:", type(exc).__name__, exc)


    date = request.GET.get("date", "").strip()
    name = request.GET.get("name", "").strip()
    activities = Activity.objects.all()
    query = request.GET.get("q", "").strip()
    chosen_club = request.GET.get("chosen_club", "").strip()
    chosen_category = request.GET.get("chosen_category", "").strip()

    if query:
        activities = activities.filter(
            Q(name__icontains=query)
            | Q(desc__icontains=query)
            | Q(club__name__icontains=query)
        )

    if chosen_category:
        activities = activities.filter(category=chosen_category)

    if chosen_club.isdigit():
        activities = activities.filter(club_id = int(chosen_club))

    if name == "za":
        activities = activities.order_by("-name", "date")
    elif name == "az":
        activities = activities.order_by("name", "date")
    elif date:
        activities = activities.order_by("date", "name")
    else:
        activities = activities.order_by("-date", "name")

    context = {
        "clubs": Club.objects.count(),
        "activities": activities,
        "activities_count": Activity.objects.count(),
        "club_options": Club.objects.order_by("name"),
        "categories": Activity.Category.choices,
        "query": query,
        "selected_club": chosen_club,
        "selected_category": chosen_category,
        "is_date": date,
        "is_name": name,
        "sent": sent,
    }
    return render(request, "config/main.html", context=context)


def about_view(request):
    clubs = Club.objects.order_by("id")
    return render(request, "config/about.html", context={"clubs": clubs})

def faq_view(request):
    sent = False

    if request.method == "POST":
        message = request.POST.get("message", "").strip()
        email = request.POST.get("email", "").strip()

        try:
            mail.contact_mail(mail=email, message=message)
            sent = True
        except Exception as exc:
            print("BŁĄD WYSYŁKI MAILA:", type(exc).__name__, exc)

    return render(request, "config/faq.html", context={"sent": sent})

def tos_view(request):
    return render(request, "config/tos.html")

def privacy_view(request):
    return render(request, "config/privacy.html")

def activity_view(request, id):
    activity = get_object_or_404(Activity, id=id)

    if request.method == "POST":
        if activity.is_full or activity.is_past:
            return redirect("activity", id=activity.id)

        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()

        try:
            mail.send_email(mail=email, name=name)
        except Exception as exc:
            print("BŁĄD WYSYŁKI MAILA:", type(exc).__name__, exc)
            return redirect(f"{reverse('activity', args=[activity.id])}?error=1")

        activity.current_participants += 1
        activity.save(update_fields=["current_participants"])
        return redirect(f"{reverse('activity', args=[activity.id])}?ok=1")

    context = {
        "activity": activity,
        "signed_up": request.GET.get("ok") == "1",
        "send_error": request.GET.get("error") == "1",
    }
    return render(request, "config/activity.html", context=context)