import json

def parse_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    print("Interface Status")
    print("================================================================================")
    print("DN                                                 Description           Speed    MTU   ")
    print("-------------------------------------------------- --------------------  ------  ------")

    for interface in data['interfaces']:
        dn = interface['dn']
        description = interface['description']
        speed = interface['speed']
        mtu = interface['mtu']

        print(f"{dn:<50} {description:<20} {speed:<6} {mtu:<6}")

parse_json('sample-data.json')