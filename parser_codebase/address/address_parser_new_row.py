import csv
import xml.etree.ElementTree as ET

# Load and parse the XML file
tree = ET.parse("source_documents/sdn_advanced.xml")
root = tree.getroot()

# Namespace
ns = {"ns": "http://www.un.org/sanctions/1.0"}

# Define CSV file header and path
csv_file_path = "parser_codebase/address/address_new_row.csv"
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
    "Script Type",
    "Comment",
]

# Write header to CSV file
with open(csv_file_path, "w", newline="", encoding="utf-8-sig") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

# Process each Location and write data to CSV
locations = root.findall(".//ns:Location", ns)
for location in locations:
    location_id = location.attrib["ID"]
    area_code_id = location.find(".//ns:LocationAreaCode", ns)
    area_code_id = area_code_id.attrib["AreaCodeID"] if area_code_id is not None else ""
    country = location.find(".//ns:LocationCountry", ns)
    country_id = country.attrib["CountryID"] if country is not None else ""
    country_relevance_id = (
        country.attrib["CountryRelevanceID"] if country is not None else ""
    )
    feature_version_ref = location.find(".//ns:FeatureVersionReference", ns)
    feature_version_id = (
        feature_version_ref.attrib["FeatureVersionID"]
        if feature_version_ref is not None
        else ""
    )

    for part in location.findall(".//ns:LocationPart", ns):
        part_type_id = part.attrib["LocPartTypeID"]
        for part_value in part.findall(".//ns:LocationPartValue", ns):
            value = (
                part_value.find(".//ns:Value", ns).text
                if part_value.find(".//ns:Value", ns) is not None
                else ""
            )
            comment = (
                part_value.find(".//ns:Comment", ns).text
                if part_value.find(".//ns:Comment", ns) is not None
                else ""
            )

            data = {
                "ID": location_id,
                "AreaCodeID": area_code_id,
                "CountryID": country_id,
                "CountryRelevanceID": country_relevance_id,
                "FeatureVersionID": feature_version_id,
                "Unknown": "",
                "Region": "",
                "Address 1": "",
                "Address 2": "",
                "Address 3": "",
                "City": "",
                "State/ Province": "",
                "Postal Code": "",
                "Script Type": "",
                "Comment": "",
            }

            if comment:
                data["Script Type"] = comment
                data["Comment"] = value
            else:
                if part_type_id == "1":  # Unknown
                    data["Unknown"] = value
                elif part_type_id == "1450":  # Region
                    data["Region"] = value
                elif part_type_id == "1451":  # Address 1
                    data["Address 1"] = value
                elif part_type_id == "1452":  # Address 2
                    data["Address 2"] = value
                elif part_type_id == "1453":  # Address 3
                    data["Address 3"] = value
                elif part_type_id == "1454":  # City
                    data["City"] = value
                elif part_type_id == "1455":  # State
                    data["State/ Province"] = value
                elif part_type_id == "1456":  # Postal Code
                    data["Postal Code"] = value

            with open(csv_file_path, "a", newline="", encoding="utf-8-sig") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow(data)
