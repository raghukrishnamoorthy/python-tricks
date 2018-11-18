import json
import pprint

mapping = {
    'a': 23,
    'b': 42,
    'c': 0xc0ffee
}
print(mapping)

print(json.dumps(mapping, indent=4))
pprint.pprint(mapping)