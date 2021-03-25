from django.db import models
from django.utils.timezone import localtime


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f"{self.owner_name} (inactive)"


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return "{user} entered at {entered} {leaved}".format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved="leaved at " + str(self.leaved_at)
            if self.leaved_at
            else "not leaved",
        )

    def get_duration(self):
        user_entered_at = localtime(self.entered_at)
        if self.leaved_at:
            time_in_warehouse = localtime(self.leaved_at) - user_entered_at
            return time_in_warehouse
        current_datetime = localtime().replace(microsecond=0)
        time_in_warehouse = current_datetime - user_entered_at
        return time_in_warehouse

    def is_visit_long(self, minutes=60):
        visit_minutes = self.get_duration().total_seconds() // 60
        return visit_minutes > minutes

    def format_duration(self):
        seconds = self.get_duration().total_seconds()
        days = int(seconds // 3600 // 24)
        hours = int(seconds // 3600 % 24)
        minutes = int((seconds % 3600) // 60)
        if days != 0:
            return f"{ days } д. { hours } ч. { minutes } м."
        return f"{ hours } ч. { minutes } м."
