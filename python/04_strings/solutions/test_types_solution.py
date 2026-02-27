from . import types


def create_types_test_class(module):
    """Create a test class that runs types assertions against the given module."""

    class TestTypes:
        def test_check_isalpha(self):
            assert module.check_isalpha("letters") is True

        def test_check_isalnum(self):
            assert module.check_isalnum("abc246") is True

        def test_check_isdigit(self):
            assert module.check_isdigit("468") is True

        def test_check_isnumeric(self):
            assert module.check_isnumeric("½¾") is True

        def test_check_islower(self):
            assert module.check_islower("lowercase") is True

        def test_check_isupper(self):
            assert module.check_isupper("UPPERCASE") is True

        def test_check_istitle(self):
            assert module.check_istitle("Title Case") is True

        def test_check_isspace(self):
            assert module.check_isspace("   ") is True

    return TestTypes


TestTypesSolution = create_types_test_class(types)
