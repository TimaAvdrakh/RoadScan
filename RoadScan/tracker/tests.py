from django.test import TestCase
from .models import RoadCrack, Police
from django.contrib.gis.geos import Point

class RoadCrackModelTest(TestCase):
    def setUp(self):
        self.road_crack = RoadCrack.objects.create(
            name="Test Road Crack",
            location=Point(1, 1),
            address="123 Main St",
            city="Test City",
            counter=4,
            approved=False
        )

    def test_road_crack_approve(self):
        self.road_crack.counter += 1
        self.road_crack.approve()
        self.assertEqual(self.road_crack.approved, True)

    def test_road_crack_str(self):
        self.assertEqual(str(self.road_crack), "Test Road Crack")


class PoliceModelTest(TestCase):
    def setUp(self):
        self.police = Police.objects.create(
            name="Test Police",
            location=Point(1, 1),
            address="123 Main St",
            city="Test City",
            approve=True
        )

    def test_police_str(self):
        self.assertEqual(str(self.police), "Police in Test City")