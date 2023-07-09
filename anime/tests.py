from django.test import TestCase
from .models import Anime
from django.contrib.auth import get_user_model

# Create your tests here.
class animeTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', password='pass')
        testuser1.save()

        test_thing = Anime.objects.create(name='kimitsu', owner=testuser1, desc="nezuko is the cutest demon")
        test_thing.save()

    def test_animes_model(self):
        animeing = Anime.objects.get(id=1)
        actual_owner= str(animeing.owner)
        actual_name = str(animeing.name)
        actual_desc = str(animeing.desc)
        self.assertEqual(actual_owner,"testuser1")
        self.assertEqual(actual_name,"kimitsu")
        self.assertEqual(actual_desc,"nezuko is the cutest demon")