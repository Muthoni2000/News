import unittest
from app.models import NewsSource

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the NewsSource class
    '''

    def setUp(self):
        '''
        Set up method that runs before every Test
        '''

        self.new_source = NewsSource('Python Must Be Crazy','A thrilling new Python Series','/khsjha27hbs',"8.5,129993")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,NewsSource))

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_source.id,"Python Must Be Crazy")
        self.assertEqual(self.new_source.name,'A thrilling new Python Series')
        self.assertEqual(self.new_source.description,'/khsjha27hbs')
        self.assertEqual(self.new_source.url,"8.5,129993")
