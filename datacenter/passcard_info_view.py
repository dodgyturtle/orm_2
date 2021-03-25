from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    user_visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []
    for user_visit in user_visits:
        this_passcard_visits.append(
            {
                "entered_at": user_visit.entered_at,
                "duration": user_visit.format_duration(),
                "is_strange": user_visit.is_visit_long(),
            }
        )
    context = {"passcard": passcard, "this_passcard_visits": this_passcard_visits}
    return render(request, "passcard_info.html", context)
