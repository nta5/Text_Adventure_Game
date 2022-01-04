import io
from unittest import TestCase
from game import foe_run_away as foe_run_away
from unittest.mock import patch


class Test(TestCase):
    @patch('random.randint', return_value=1)
    def test_foe_run_away_foe_run(self, _):
        test_opponent = {'Name': 'Test Opponent'}
        actual = foe_run_away(test_opponent)
        self.assertTrue(actual)

    @patch('random.randint', return_value=1)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_foe_run_away_notification(self, mock_output, _):
        test_opponent = {'Name': 'Test Opponent'}
        foe_run_away(test_opponent)
        actual = mock_output.getvalue()
        expected = "Test Opponent runs away."
        self.assertIn(expected, actual)

    @patch('random.randint', return_value=2)
    def test_foe_run_away_foe_not_run(self, _):
        test_opponent = {'Name': 'Test Opponent'}
        actual = foe_run_away(test_opponent)
        self.assertFalse(actual)
