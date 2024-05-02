import csv
from lxml import etree


def parse_xml(xml_file):
    ns = {"ns": "http://www.un.org/sanctions/1.0"}

    tree = etree.parse(xml_file)
    root = tree.getroot()

    data = []

    for distinct_party in root.findall(".//ns:DistinctParty", namespaces=ns):
        fixed_ref = distinct_party.get("FixedRef")

        for alias in distinct_party.findall(".//ns:Alias", namespaces=ns):
            documented_name = alias.find(".//ns:DocumentedName", namespaces=ns)
            if documented_name is not None:
                name_parts = {
                    "last_name": "",
                    "first_name": "",
                    "middle_name": "",
                    "prefix": "",
                    "suffix": "",
                    "nickname": "",
                    "maiden_name": "",
                    "aircraft_name": "",
                    "entity_name": "",
                    "vessel_name": "",
                }

                for name_part in documented_name.findall(
                    ".//ns:DocumentedNamePart/ns:NamePartValue", namespaces=ns
                ):
                    part_value = name_part.text
                    part_group_id = name_part.get("NamePartGroupID")

                    if part_group_id == "1520":  # Last Name
                        name_parts["last_name"] = part_value
                    elif part_group_id == "1521":  # First Name
                        name_parts["first_name"] = part_value
                    elif part_group_id == "1522":  # Middle Name
                        name_parts["middle_name"] = part_value
                    elif part_group_id in ["91708", "91709"]:  # Prefix
                        name_parts["prefix"] = part_value
                    elif part_group_id == "1523":  # Maiden Name
                        name_parts["maiden_name"] = part_value
                    elif part_group_id == "1524":  # Aircraft Name
                        name_parts["aircraft_name"] = part_value
                    elif part_group_id == "1525":  # Entity Name
                        name_parts["entity_name"] = part_value
                    elif part_group_id == "1526":  # Vessel Name
                        name_parts["vessel_name"] = part_value
                    elif part_group_id == "1528":  # Nickname
                        name_parts["nickname"] = part_value

                # Format the full name based on the provided formats
                if name_parts["nickname"]:
                    full_name = name_parts["nickname"]
                elif name_parts["aircraft_name"]:
                    full_name = name_parts["aircraft_name"]
                elif name_parts["entity_name"]:
                    full_name = name_parts["entity_name"]
                elif name_parts["vessel_name"]:
                    full_name = name_parts["vessel_name"]
                else:
                    full_name = f"{name_parts['prefix']} {name_parts['last_name']}, {name_parts['first_name']} {name_parts['middle_name']} {name_parts['maiden_name']}".strip()

                # Only add to data if full_name is not empty
                if full_name:
                    data.append({"FixedRef": fixed_ref, "FullName": full_name})

    return data


def write_csv(data, csv_file):
    with open(csv_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["FixedRef", "FullName"])
        writer.writeheader()
        for row in data:
            writer.writerow(row)


def main():
    xml_file = "sdn_advanced.xml"  # Update this path to your XML file location
    csv_file = "output_parsed_names.csv"

    data = parse_xml(xml_file)
    write_csv(data, csv_file)


if __name__ == "__main__":
    main()
