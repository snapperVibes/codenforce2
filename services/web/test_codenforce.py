# Todo: Continous Integration
import pytest

from codenforce import parse


class TestParse:
    def test_address(self):
        addr = parse.address("123 example street")
        assert addr == {
            "number": "123",
            "street": "EXAMPLE",
            "suffix_full": "STREET",
            "suffix": "ST",
        }
        # Make sure spaces are discarded
        addr = parse.address(" 123  example   street   ")
        assert addr == {
            "number": "123",
            "street": "EXAMPLE",
            "suffix_full": "STREET",
            "suffix": "ST",
        }
        # Make sure suffixes are alright
        addr = parse.address("123 example st")
        assert addr == {
            "number": "123",
            "street": "EXAMPLE",
            "suffix_full": None,
            "suffix": "ST",
        }
        addr = parse.address("123 example st.")
        assert addr == {
            "number": "123",
            "street": "EXAMPLE",
            "suffix_full": None,
            "suffix": "ST",
        }


if __name__ == "__main__":
    pytest.main()
