# Use this file for reference in future for full implementation of the parser logic as per alex mail. creates 4 csv files for names, addresses, ids and features

import csv
import xml.etree.ElementTree as ET


def parse_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    def get_text(element, tag):
        value = element.find(f".//{{{ns}}}{tag}")
        return value.text if value is not None else ""

    def get_list_text(element, tag):
        values = element.findall(f".//{{{ns}}}{tag}/{{{ns}}}{tag}Value", namespaces=ns)
        return [value.text for value in values]

    def parse_names(distinct_party):
        data = []
        for profile in distinct_party.findall(f".//{{{ns}}}Profile", namespaces=ns):
            for identity in profile.findall(f".//{{{ns}}}Identity", namespaces=ns):
                for alias in identity.findall(f".//{{{ns}}}Alias", namespaces=ns):
                    for documented_name in alias.findall(
                        f".//{{{ns}}}DocumentedName", namespaces=ns
                    ):
                        row = {
                            "FixedRef": distinct_party.get("FixedRef"),
                            "DocumentedNameID": documented_name.get("ID"),
                            "List": ", ".join(get_list_text(distinct_party, "List")),
                            "SanctionsTypeProgram": ", ".join(
                                get_list_text(distinct_party, "SanctionsType")
                                + get_list_text(distinct_party, "SanctionsProgram")
                            ),
                            "Designation": get_text(profile, "PartyType")
                            + ", "
                            + get_text(profile, "PartySubType"),
                            "PrimaryEntry": alias.get("Primary"),
                            "AliasType": alias.get("AliasTypeID"),
                            "LowQuality": alias.get("LowQuality"),
                            "Acronym": documented_name.get("Acronym"),
                            "Script": documented_name.get("ScriptID"),
                        }

                        name_parts = []
                        for name_part in documented_name.findall(
                            f".//{{{ns}}}DocumentedNamePart/{{{ns}}}NamePartValue",
                            namespaces=ns,
                        ):
                            name_parts.append(name_part.text)

                        row["Name"] = ", ".join(name_parts)
                        data.append(row)

        return data

    def parse_addresses(distinct_party):
        data = []
        for profile in distinct_party.findall(f".//{{{ns}}}Profile", namespaces=ns):
            for feature in profile.findall(f".//{{{ns}}}Feature", namespaces=ns):
                if feature.get("FeatureTypeID") == "9":
                    for location in feature.findall(
                        f".//{{{ns}}}Location/{{{ns}}}LocationPart", namespaces=ns
                    ):
                        row = {
                            "FixedRef": distinct_party.get("FixedRef"),
                            location.get("LocPartTypeID"): location.text,
                        }
                        data.append(row)

        return data

    def parse_ids(distinct_party):
        data = []
        for profile in distinct_party.findall(f".//{{{ns}}}Profile", namespaces=ns):
            for feature in profile.findall(f".//{{{ns}}}Feature", namespaces=ns):
                if feature.get("FeatureTypeID") == "10":
                    for id_reg_doc in feature.findall(
                        f".//{{{ns}}}IDRegDoc", namespaces=ns
                    ):
                        row = {
                            "FixedRef": distinct_party.get("FixedRef"),
                            "DocumentType": id_reg_doc.get("IDRegDocTypeID"),
                            "IssuedBy": id_reg_doc.get("IssuedBy"),
                            "IssueDate": id_reg_doc.get("IssueDate"),
                            "ExpirationDate": id_reg_doc.get("ExpirationDate"),
                            "Value": id_reg_doc.get("IDRegDocValue"),
                        }
                        data.append(row)

        return data

    def parse_features(distinct_party):
        data = []
        for profile in distinct_party.findall(f".//{{{ns}}}Profile", namespaces=ns):
            for feature in profile.findall(f".//{{{ns}}}Feature", namespaces=ns):
                row = {
                    "FixedRef": distinct_party.get("FixedRef"),
                    "FeatureType": feature.get("FeatureTypeID"),
                    "Value": feature.get("Value"),
                }
                data.append(row)

        return data

    ns = {"ns": "http://www.un.org/sanctions/1.0"}

    names = []
    addresses = []
    ids = []
    features = []

    for distinct_party in root.findall(f".//{{{ns}}}DistinctParty", namespaces=ns):
        names.extend(parse_names(distinct_party))
        addresses.extend(parse_addresses(distinct_party))
        ids.extend(parse_ids(distinct_party))
        features.extend(parse_features(distinct_party))

    with open("names.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=names[0].keys())
        writer.writeheader()
        writer.writerows(names)

    with open("addresses.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=addresses[0].keys())
        writer.writeheader()
        writer.writerows(addresses)

    with open("ids.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=ids[0].keys())
        writer.writeheader()
        writer.writerows(ids)

    with open("features.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=features[0].keys())
        writer.writeheader()
        writer.writerows(features)


# if \_\_name\_\_ == "\_\_main\_\_":
#     xml\_file = "path/to/your/xml/file.xml"
#     parse\_xml(xml\_file)
