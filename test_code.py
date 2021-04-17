import find_invalid_entries
import unittest
from unittest import mock

data_item = [
{"name":"iViennnia","address":"test address","zip":"17565","id":"ea0c2"},
{"name":"Viennia Sturm","address":"","zip":"17565","id":"ea0c4"},
{"name":"","address":"test address","zip":"17565","id":"ea0c3"},
{"name":"","address":"test address1","zip":"17543","id":"ea0c3"},
{"name":"iViennnia","address":"test address","zip":"0000","id":"ea0c1"},
{"name":"iViennnia","address":"test address","zip":"00000","id":"ea0c15"},
{"name":"iViennnia","address":"test address","zip":"00abc","id":"ea0c16"},
{"name":"iViennnia","address":"test address","zip":"00abc9999","id":"ea0c17"}
]

expected_invalids = ["ea0c4", "ea0c3", "ea0c3", "ea0c1", "ea0c15", "ea0c16", "ea0c17"]

@mock.patch('find_invalid_entries.json')
def test_main(json_mock):
    json_mock.load.return_value = data_item
    items = find_invalid_entries.main()
    assert items ==  expected_invalids

if __name__ == "__main__":
    test_main()
    print("test passed!")
