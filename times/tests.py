from django.test import TestCase
from .logic.helper import getSessionTagFromNotes
# Create your tests here.

class Test_Helper(TestCase):
    def test_Get_Tag_From_Notes_Valid(self):
        self.assertEqual(getSessionTagFromNotes('#st "Tag"'), "Tag")

    def test_Get_Tag_From_Notes_Not_Valid_No_st(self):
        self.assertEqual(getSessionTagFromNotes('hello'), None)

    def test_Get_Tag_From_Notes_Not_Valid_st_With_Space(self):
        self.assertEqual(getSessionTagFromNotes('# st "Tag"'), None)

    def test_Get_Tag_From_Notes_Returns_None_With_Multiple_st(self):
        self.assertEqual(getSessionTagFromNotes('#st "Tag" #st "Tag"'), None)

