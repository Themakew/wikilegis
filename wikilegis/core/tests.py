from django.test import TestCase
from model_mommy import mommy
from wikilegis.core.models import BillSegment
from wikilegis.core.models import CitizenAmendment
from wikilegis.core.models import Proposition
from wikilegis.core.models import UpDownVote


# Create your tests here.
class Core(TestCase):

    def coreTest(self):
        pass


class TestModels(TestCase):

    def setUp(self):
        self.citizen_amendment = CitizenAmendment()
        self.bill_segment = BillSegment()
        self.proposition = Proposition()
        self.up_down_vote = UpDownVote()

    def test_unicode_from_proposition_class(self):
        mock = mommy.make(Proposition)
        self.assertTrue(isinstance(mock, Proposition))
        self.assertEqual(mock.__unicode__(), mock.number)

    def test_unicode_from_up_down_vote_class(self):
        mock = mommy.make(UpDownVote)
        self.assertTrue(isinstance(mock, UpDownVote))
        self.assertEqual(mock.__unicode__(), mock.user)
