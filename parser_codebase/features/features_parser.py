import csv
import xml.etree.ElementTree as ET

# Parse the XML file
tree = ET.parse("source_documents/sdn_advanced.xml")
root = tree.getroot()

# Define the namespace
ns = {"ns": "http://www.un.org/sanctions/1.0"}

# Mapping from FeatureType ID to FeatureType value
feature_type_mapping = {}
feature_type_values = root.find(".//ns:FeatureTypeValues", ns)
for feature_type in feature_type_values.findall(".//ns:FeatureType", ns):
    feature_type_id = feature_type.attrib["ID"]
    feature_type_value = feature_type.text
    feature_type_mapping[feature_type_id] = feature_type_value

# Mapping from Reliability ID to Reliability value
reliability_mapping = {
    "1560": "Confirmed",
    "1561": "False",
    "91479": "Reported",
    "1": "Unknown",
}

# Define the CSV file path and fieldnames
csv_file_path = "parser_codebase/features/output_features.csv"
fieldnames = [
    "FixedRef",
    "FeatureType",
    "Value",
    "ReliabilityID",
    "ReliabilityValue",
    "Comment",
    "LocationID",
]

# Open the CSV file for writing
with open(csv_file_path, "w", newline="", encoding="utf-8-sig") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Find all DistinctParty elements
    distinct_parties = root.findall(".//ns:DistinctParty", ns)
    for party in distinct_parties:
        fixed_ref = party.attrib["FixedRef"]

        # Find all Feature elements within each DistinctParty
        features = party.findall(".//ns:Feature", ns)
        for feature in features:
            feature_type_id = feature.attrib["FeatureTypeID"]
            feature_type = feature_type_mapping.get(feature_type_id, "")

            # Extract the VersionDetail text if available
            version_detail = feature.find(".//ns:VersionDetail", ns)
            value = version_detail.text if version_detail is not None else ""

            # Extract additional details
            feature_version = feature.find(".//ns:FeatureVersion", ns)
            reliability_id = feature_version.attrib.get("ReliabilityID", "")
            reliability_value = reliability_mapping.get(reliability_id, "Unknown")
            comment = (
                feature_version.find(".//ns:Comment", ns).text
                if feature_version.find(".//ns:Comment", ns) is not None
                else ""
            )
            location_id = (
                feature_version.find(".//ns:VersionLocation", ns).attrib.get(
                    "LocationID", ""
                )
                if feature_version.find(".//ns:VersionLocation", ns) is not None
                else ""
            )

            # Prepare the data dictionary
            data = {
                "FixedRef": fixed_ref,
                "FeatureType": feature_type,
                "Value": value,
                "ReliabilityID": reliability_id,
                "ReliabilityValue": reliability_value,
                "Comment": comment,
                "LocationID": location_id,
            }

            # Write the data to the CSV file
            writer.writerow(data)
