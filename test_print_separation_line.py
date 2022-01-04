import io
from unittest import TestCase
from game import print_separation_line as print_line
from unittest.mock import patch


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_separation_line(self, mock_output):
        print_line()
        actual = mock_output.getvalue()
        expected = "****************************************"
        self.assertIn(expected, actual)
