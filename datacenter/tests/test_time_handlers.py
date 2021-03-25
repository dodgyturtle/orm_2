from datacenter.models import Visit, Passcard
from django.test import TestCase
from datetime import timedelta


class TestTimeHandlers(TestCase):
    def setUp(self):
        user_passcard = Passcard.objects.create(
            is_active=True,
            created_at="11.01.2018 15:28",
            passcode="ceb148a6-fb27-4106-890c-89dc8cedfe83",
            owner_name="Jennifer Martin",
        )
        user_passcard.save()
        user_visit = Visit.objects.create(
            passcard=user_passcard,
            entered_at="2018-01-11 00:01+00:00",
            leaved_at="2018-01-13 23:59+00:00",
        )
        user_visit.save()
        user_visit = Visit.objects.create(
            passcard=user_passcard,
            entered_at="2021-01-11 00:01+00:00",
        )
        user_visit.save()

    def tearDown(self):
        user_passcard = Passcard.objects.get(owner_name="Jennifer Martin")
        user_visits = Visit.objects.filter(passcard=user_passcard)
        user_passcard.delete()
        user_visits.delete()

    def test_get_duration(self):
        user_passcard = Passcard.objects.get(owner_name="Jennifer Martin")
        user_visits = Visit.objects.filter(passcard=user_passcard)
        assert user_visits[0].get_duration() == timedelta(days=2, hours=23, minutes=58)

    def test_is_visit_long_true(self):
        user_passcard = Passcard.objects.get(owner_name="Jennifer Martin")
        user_visits = Visit.objects.filter(passcard=user_passcard)
        assert user_visits[0].is_visit_long() == True

    def test_is_visit_long_not_leaved_true(self):
        user_passcard = Passcard.objects.get(owner_name="Jennifer Martin")
        user_visits = Visit.objects.filter(passcard=user_passcard)
        assert user_visits[1].is_visit_long() == True

    def test_is_visit_long_false(self):
        user_passcard = Passcard.objects.get(owner_name="Jennifer Martin")
        user_visits = Visit.objects.filter(passcard=user_passcard)
        assert user_visits[0].is_visit_long(minutes=4380) == False

    def test_format_duration(self):
        user_passcard = Passcard.objects.get(owner_name="Jennifer Martin")
        user_visits = Visit.objects.filter(passcard=user_passcard)
        assert user_visits[0].format_duration() == "2 д. 23 ч. 58 м."
