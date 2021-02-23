# # Todo: Continous Integration
# import pytest
#
# from codenforce import parse
#
#
#
#
# class TestParse:
#     # We COULD use db.table_mapper, but it being explicit help keeps things clear.
#     def _new_address(
#         self,
#         id = None,
#         crossstreet = None,
#         number = None,
#         prefixdirection = None,
#         street = None,
#         suffix = None,
#         suffix_full = None,
#         suffixdirection = None,
#         type = None
#     ):
#         return {
#             'id': id,
#             'crossstreet': crossstreet,
#             'number': number,
#             'prefixdirection': prefixdirection,
#             'street': street,
#             'suffix': suffix,
#             'suffix_full': suffix_full,
#             'suffixdirection': suffixdirection,
#             'type': type
#         }
#
#     def test_address(self):
#         addr = parse.address("123 example street")
#         assert addr == self._new_address(
#             number = "123",
#             street = "EXAMPLE",
#             suffix_full="STREET",
#             suffix = "ST",
#         )
#         # Make sure spaces are discarded
#         addr = parse.address(" 123  example   street   ")
#         assert addr == self._new_address(
#             number = "123",
#             street = "EXAMPLE",
#             suffix_full="STREET",
#             suffix = "ST",
#         )
#         # Make sure suffixes are alright
#         addr = parse.address("123 example st")
#         assert addr == self._new_address(
#             number = "123",
#             street = "EXAMPLE",
#             suffix = "ST",
#         )
#         addr = parse.address("123 example st.")
#         assert addr == self._new_address(
#             number = "123",
#             street = "EXAMPLE",
#             suffix = "ST",
#         )
#
#     def test_weird_addresses(self):
#         addr = parse.address("456 Alpine Lane, Twin P")
#
#
#
#
# if __name__ == "__main__":
#     pytest.main()
