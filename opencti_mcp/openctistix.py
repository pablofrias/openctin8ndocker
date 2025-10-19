from pycti import OpenCTIApiClient
import json

stix_json = '''
{
    "type": "bundle",
    "id": "bundle--12345678-1234-5678-1234-567812345678",
    "objects": [
        {
            "type": "indicator",
            "spec_version": "2.1",
            "id": "indicator--87654321-4321-8765-4321-876543218765",
            "created": "2023-01-01T12:00:00.000Z",
            "modified": "2023-01-01T12:00:00.000Z",
            "name": "Test Indicator",
            "description": "This is a test indicator",
            "pattern": "[file:hashes.'SHA-256' = 'd41d8cd98f00b204e9800998ecf8427e']",
            "pattern_type": "stix",
            "valid_from": "2023-01-01T12:00:00.000Z"
        }
    ]
}
'''

client = OpenCTIApiClient("http://localhost:8080", "3a5de77a-7a21-11f0-add4-dfa602df585b")

stix_dict = json.loads(stix_json)

try:
    result = client.stix2.import_bundle(stix_dict, update=True)  # Pass parsed dict
    print("response: " + str(result))
except Exception as e:
    print("error: " + str(e))