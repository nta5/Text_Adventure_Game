import io
from unittest import TestCase
from game import introduction as introduction
from unittest.mock import patch


class Test(TestCase):
    @patch('time.sleep', return_value=None)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_introduction_start(self, mock_output, _):
        introduction()
        actual = mock_output.getvalue()
        expected = "\n****************************************\n\nThe sudden light makes you squint.\n"
        self.assertIn(expected, actual)

    @patch('time.sleep', return_value=None)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_introduction_middle(self, mock_output, _):
        introduction()
        actual = mock_output.getvalue()
        expected = "You hear some murmurs: 'It must be him, the hero in the prophecy...'"
        self.assertIn(expected, actual)

    @patch('time.sleep', return_value=None)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_introduction_end(self, mock_output, _):
        introduction()
        actual = mock_output.getvalue()
        expected = "Juliana asks: 'May I ask for your name, adventurer?'"
        self.assertIn(expected, actual)
