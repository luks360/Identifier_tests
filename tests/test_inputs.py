import pytest
from src.Identifier import Identifier

class TestInputValues:

    @pytest.fixture(scope='module')
    def setUp(self):
        obj = Identifier()
        return obj

    def test_ValueNull(self, setUp):
        print("Testing the case ValueNull")
        expected_result = False
        result_obtained = setUp.validateIdentifier(" ")

        assert result_obtained == expected_result

    def test_OneCharacterAndLetter(self, setUp):
        print("Testing the case OneCharacterAndLetter")
        expected_result = True
        result_obtained = setUp.validateIdentifier("C") 

        assert result_obtained == expected_result

    def test_MaximumCharactersLimit(self, setUp):
        print("Testing the case MaximumCharactersLimit")
        expected_result = True
        result_obtained = setUp.validateIdentifier("C54674")

        assert result_obtained == expected_result

    def test_ExeedingMaximumCharacterLimit(self, setUp):
        print("Testing the case ExeedingMaximumCharacterLimit")
        expected_result = False
        result_obtained = setUp.validateIdentifier("C865654")

        assert result_obtained == expected_result

    def test_OneCharacterAndNumber(self, setUp):
        print("Testing the case OneCharacterAndNumber")
        expected_result = False
        result_obtained = setUp.validateIdentifier("7")

        assert result_obtained == expected_result

    def test_SpecialCharactersIncluded(self, setUp):
        print("Testing the case SpecialCharactersIncluded")
        expected_result = False
        result_obtained = setUp.validateIdentifier("C65*%a")

        assert result_obtained == expected_result