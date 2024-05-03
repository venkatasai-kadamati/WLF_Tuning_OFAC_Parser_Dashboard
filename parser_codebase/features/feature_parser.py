import csv
import xml.etree.ElementTree as ET

tree = ET.parse("source_documents/sdn_advanced.xml")
root = tree.getroot()

ns = {"ns": "http://www.un.org/sanctions/1.0"}

# mapping from FeatureType ID to FeatureType value
feature_type_mapping = {}
feature_type_values = root.find(".//ns:FeatureTypeValues", ns)
for feature_type in feature_type_values.findall(".//ns:FeatureType", ns):
    feature_type_id = feature_type.attrib["ID"]
    feature_type_value = feature_type.text
    feature_type_mapping[feature_type_id] = feature_type_value

csv_file_path = "parser_codebase/features/output_features.csv"
fieldnames = ["FixedRef", "FeatureType", "Value"]


with open(csv_file_path, "w", newline="", encoding="utf-8-sig") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()


distinct_parties = root.findall(".//ns:DistinctParty", ns)
for party in distinct_parties:
    fixed_ref = party.attrib["FixedRef"]

    features = party.findall(".//ns:Feature", ns)
    for feature in features:
        feature_type_id = feature.attrib["FeatureTypeID"]
        feature_type = feature_type_mapping.get(feature_type_id, "")

        data = {
            "FixedRef": fixed_ref,
            "FeatureType": feature_type_id,
            "Value": feature_type,
        }

        with open(csv_file_path, "a", newline="", encoding="utf-8-sig") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(data)
