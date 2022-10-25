from src.Identifier import validateIdentifier

class TestInputValues:
    def test_ValueNull(self):
        assert validateIdentifier(" ") == False

    def test_OneCharacterAndLetter(self):
        assert validateIdentifier("C") == True

    def test_MaximumCharactersLimit(self):
        assert validateIdentifier("C54674") == True

    def test_ExeedingMaximumCharacterLimit(self):
        assert validateIdentifier("C865654") == False

    def test_OneCharacterAndNumber(self):
        assert validateIdentifier("7") == False

    def test_SpecialCharactersIncluded(self):
        assert validateIdentifier("C65*%a") == False