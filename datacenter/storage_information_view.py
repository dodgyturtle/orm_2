from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime


def storage_information_view(request):
    non_closed_visits = []
    visitors = Visit.objects.filter(leaved_at__isnull=True)
    for visitor in visitors:
        user_entered = localtime(visitor.entered_at)
        user_in_warehouse_passcard = visitor.passcard
        non_closed_visits.append(
            {
                "who_entered": user_in_warehouse_passcard.owner_name,
                "entered_at": user_entered,
                "duration": visitor.format_duration(),
                "is_strange": visitor.is_visit_long(),
            }
        )

    context = {
        "non_closed_visits": non_closed_visits,
    }
    return render(request, "storage_information.html", context)
