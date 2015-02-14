from csq2fix import csq2fix
import json
import unittest


class TestSingleQuestion(unittest.TestCase):

    def setUp(self):
        single_question = "\n\n:\nHere is a question.\n"
        self.result = csq2fix(single_question, "Aaron")

    def test_returns_valid_json_list(self):
        result = json.loads(self.result)
        assert isinstance(result, list)

    def test_numbers_from_one(self):
        result = json.loads(self.result)
        assert result[0]["pk"] == 1

    def test_username_is_entered(self):
        result = json.loads(self.result)
        assert result[0]["fields"]["user"] == "Aaron"

    def test_question_text_is_entered(self):
        result = json.loads(self.result)
        print(result)
        assert "Here is a question." in result[0]["fields"]["text"]

if __name__ == '__main__':
    unittest.main()
