from django.test import TestCase

from App1.forms import blogForms, AvatarFormulario
import django 
# Import the Django model you want to test
from App1.forms import AvatarFormulario
import unittest
# Import the Django test framework
from django.test import TestCase

# Write your unit test(s)
from django.test import TestCase

from App1.forms import blogForms, AvatarFormulario
import django 
# Import the Django model you want to test
from App1.forms import AvatarFormulario
import unittest
# Import the Django test framework
from django.test import TestCase

# Write your unit test(s)
class blogFormularioTest(TestCase):
    def test_valid_form(self):
        form_data = {'id': 1, 'titulo': 'mi primer blog', 'subtitulo': 'nose', 'contenido': 'aca va el contenido', 'autor': 'bresciani1'}
        form = blogForms(data=form_data)
        print(form)
        #print(self.assertTrue(form.is_valid()))

    def test_invalid_form(self):
        form_data = {'id': 1, 'titulo': 'mi primer blog', 'subtitulo': 'nose', 'email': None, 'autor': 'bresciani1'}
        form = blogForms(data=form_data)
        print(form)
        #print(self.assertFalse(form.is_valid()))

# Run your unit test(s) with a test runner
if __name__ == '__main__':
    django.setup()
    unittest.main()
# Create your tests here.
