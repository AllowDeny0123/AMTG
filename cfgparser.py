import json

def parse_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            if 'ports' in data and 'ips' in data:
                ports = data['ports']
                ips = data['ips']
                return (ips, ports)
            else:
                print("Invalid JSON")
    except FileNotFoundError:
        print(f"File not found")
    except json.JSONDecodeError:
        print(f"Cant read file.")
    except Exception as e:
        print(f"Error")