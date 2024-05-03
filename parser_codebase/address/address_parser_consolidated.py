import csv
import xml.etree.ElementTree as ET

# Load and parse the XML file
tree = ET.parse("source_documents/sdn_advanced.xml")
root = tree.getroot()

# Namespace
ns = {"ns": "http://www.un.org/sanctions/1.0"}

# MCOR == Multiple columns one row
# Define CSV file header and path
csv_file_path = "parser_codebase/address/address_consolidated_MCOR.csv"
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
    "City (Non-Latin)",
    "State/ Province",
    "State/ Province (Non-Latin)",
    "Postal Code",
    "Postal Code (Non-Latin)",
]

# Write header to CSV file
with open(csv_file_path, "w", newline="", encoding="utf-8-sig") as csvfile:
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
        "City (Non-Latin)": "",
        "State/ Province": "",
        "State/ Province (Non-Latin)": "",
        "Postal Code": "",
        "Postal Code (Non-Latin)": "",
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

    # Extract Address, City, State, Postal Code, and non-Latin script values from LocationPart
    for part in location.findall(".//ns:LocationPart", ns):
        part_type_id = part.attrib["LocPartTypeID"]
        non_latin_values = []
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

            if comment:
                non_latin_values.append(f"{comment}: {value}")
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

        if non_latin_values:
            if part_type_id == "1454":  # City
                data["City (Non-Latin)"] = " | ".join(non_latin_values)
            elif part_type_id == "1455":  # State/ Province
                data["State/ Province (Non-Latin)"] = " | ".join(non_latin_values)
            elif part_type_id == "1456":  # Postal Code
                data["Postal Code (Non-Latin)"] = " | ".join(non_latin_values)

    # Extract FeatureVersionID from FeatureVersionReference
    feature_version = location.find(".//ns:FeatureVersionReference", ns)
    if feature_version is not None:
        data["FeatureVersionID"] = feature_version.attrib["FeatureVersionID"]

    # Write data to CSV
    with open(csv_file_path, "a", newline="", encoding="utf-8-sig") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(data)
