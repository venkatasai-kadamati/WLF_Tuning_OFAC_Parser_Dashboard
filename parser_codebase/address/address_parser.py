# TODO
# TODO : Map the country ID values from numeric to textual

import csv
import xml.etree.ElementTree as ET

# Load and parse the XML file
tree = ET.parse("source_documents/sdn_advanced.xml")
root = tree.getroot()

# Namespace
ns = {"ns": "http://www.un.org/sanctions/1.0"}

# Define CSV file header and path
csv_file_path = "parser_codebase/address/address.csv"
fieldnames = [
    "ID",
    "AreaCodeID",
    "CountryID",
    "CountryRelevanceID",
    "FeatureVersionID",
    "Unknown",
    "Region",
    "Address 1",
    "Address 2",
    "Address 3",
    "City",
    "State/ Province",
    "Postal Code",
]

# Write header to CSV file
with open(csv_file_path, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

# Process each Location and write data to CSV
locations = root.findall(".//ns:Location", ns)
for location in locations:
    data = {
        "ID": location.attrib["ID"],
        "AreaCodeID": "",
        "CountryID": "",
        "CountryRelevanceID": "",
        "Unknown": "",
        "Region": "",
        "Address 1": "",
        "Address 2": "",
        "Address 3": "",
        "City": "",
        "State/ Province": "",
        "Postal Code": "",
        "FeatureVersionID": "",
    }

    # Extract AreaCodeID and CountryID from LocationAreaCode and LocationCountry
    area_code = location.find(".//ns:LocationAreaCode", ns)
    if area_code is not None:
        data["AreaCodeID"] = area_code.attrib["AreaCodeID"]

    country = location.find(".//ns:LocationCountry", ns)
    if country is not None:
        data["CountryID"] = country.attrib["CountryID"]
        data["CountryRelevanceID"] = country.attrib["CountryRelevanceID"]

    # Extract Address, City, and State from LocationPart
    for part in location.findall(".//ns:LocationPart", ns):
        part_type_id = part.attrib["LocPartTypeID"]
        part_value = part.find(".//ns:Value", ns)
        if part_value is not None:
            if part_type_id == "1":  # Unknown
                data["Unknown"] = part_value.text
            elif part_type_id == "1450":  # Region
                data["Region"] = part_value.text
            elif part_type_id == "1451":  # Address 1
                data["Address 1"] = part_value.text
            elif part_type_id == "1452":  # Address 2
                data["Address 2"] = part_value.text
            elif part_type_id == "1453":  # Address 3
                data["Address 3"] = part_value.text
            elif part_type_id == "1454":  # City
                data["City"] = part_value.text
            elif part_type_id == "1455":  # State
                data["State/ Province"] = part_value.text
            elif part_type_id == "1456":  # Postal Code
                data["Postal Code"] = part_value.text

    # Extract FeatureVersionID from FeatureVersionReference
    feature_version = location.find(".//ns:FeatureVersionReference", ns)
    if feature_version is not None:
        data["FeatureVersionID"] = feature_version.attrib["FeatureVersionID"]

    # Write data to CSV
    with open(csv_file_path, "a", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(data)
