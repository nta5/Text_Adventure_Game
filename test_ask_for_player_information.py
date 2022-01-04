import io
from unittest import TestCase
from game import ask_for_player_information as player_information
from unittest.mock import patch


class Test(TestCase):
    @patch('time.sleep', return_value=None)
    @patch('builtins.input', side_effect=['Noname'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_ask_for_player_information_capitalized_first_letter(self, mock_output,  __, _):
        test_character = player_information()
        mock_output.getvalue()
        expected_name = 'Noname'
        self.assertEqual(test_character['Name'], expected_name)

    @patch('time.sleep', return_value=None)
    @patch('builtins.input', side_effect=['noname'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_ask_for_player_information_not_capitalized_first_letter(self, mock_output, __, _):
        test_character = player_information()
        mock_output.getvalue()
        expected_name = 'Noname'
        self.assertEqual(test_character['Name'], expected_name)

    @patch('time.sleep', return_value=None)
    @patch('builtins.input', side_effect=['nOnAmE'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_ask_for_player_information_mix_capitalized_letters(self, mock_output, __, _):
        test_character = player_information()
        mock_output.getvalue()
        expected_name = 'Noname'
        self.assertEqual(test_character['Name'], expected_name)

    @patch('time.sleep', return_value=None)
    @patch('builtins.input', side_effect=['123noname'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_ask_for_player_information_number_as_initial(self, mock_output, __, _):
        test_character = player_information()
        mock_output.getvalue()
        expected_name = '123Noname'
        self.assertEqual(test_character['Name'], expected_name)

    @patch('time.sleep', return_value=None)
    @patch('builtins.input', side_effect=['123'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_ask_for_player_information_all_numbers(self, mock_output, __, _):
        test_character = player_information()
        mock_output.getvalue()
        expected_name = '123'
        self.assertEqual(test_character['Name'], expected_name)

    @patch('time.sleep', return_value=None)
    @patch('builtins.input', side_effect=['Noname'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_ask_for_player_information_character_dictionary(self, mock_output, __, _):
        test_character = player_information()
        mock_output.getvalue()
        expected_key_value_pairs = 6
        self.assertEqual(len(test_character), expected_key_value_pairs)
