import csv
import xml.etree.ElementTree as ET

# Load and parse the XML file
tree = ET.parse("C:/Users/kadam/OneDrive/Documents/GitHub/WLF_Tuning_OFAC_Parser_Dashboard/source_documents/sdn_advanced.xml")
root = tree.getroot()

# Load and parse the countryvalues.xml file
# country_tree = ET.parse("C:/Users/kadam/OneDrive/Documents/GitHub/WLF_Tuning_OFAC_Parser_Dashboard/parser_codebase/address/countryvalues.txt")
# country_root = country_tree.getroot()

# Namespace
ns = {"ns": "http://www.un.org/sanctions/1.0"}


# Create a dictionary to map Country ID to Country Name
country_map = {
    "11029": "Afghanistan",
    "11030": "Albania",
    "11031": "Algeria",
    "11033": "Angola",
    "11034": "Antigua and Barbuda",
    "11035": "Argentina",
    "11036": "Armenia",
    "11037": "Australia",
    "11038": "Austria",
    "11039": "Azerbaijan",
    "11040": "Bahamas, The",
    "11041": "Bahrain",
    "11042": "Bangladesh",
    "11043": "Barbados",
    "11044": "Belarus",
    "11045": "Belgium",
    "11046": "Belize",
    "11047": "Benin",
    "11049": "Bolivia",
    "11050": "Bosnia and Herzegovina",
    "11052": "Brazil",
    "11053": "Brunei",
    "11054": "Bulgaria",
    "11055": "Burkina Faso",
    "11056": "Burma",
    "11058": "Cambodia",
    "11060": "Canada",
    "11061": "Cabo Verde",
    "11062": "Central African Republic",
    "11064": "Chile",
    "11065": "China",
    "11066": "Colombia",
    "11067": "Comoros",
    "11068": "Congo, Republic of the",
    "11069": "Congo, Democratic Republic of the",
    "11070": "Costa Rica",
    "11071": "Cote d Ivoire",
    "11072": "Croatia",
    "11073": "Cuba",
    "11074": "Cyprus",
    "11075": "Czech Republic",
    "11076": "Denmark",
    "11077": "Djibouti",
    "11078": "Dominica",
    "11079": "Dominican Republic",
    "11081": "Ecuador",
    "11082": "Egypt",
    "11083": "El Salvador",
    "11084": "Equatorial Guinea",
    "11085": "Eritrea",
    "11086": "Estonia",
    "11087": "Ethiopia",
    "11089": "Finland",
    "11090": "France",
    "11092": "The Gambia",
    "11093": "Georgia",
    "11094": "Germany",
    "11095": "Ghana",
    "11096": "Greece",
    "11098": "Guatemala",
    "11099": "Guinea",
    "11100": "Guinea-Bissau",
    "11101": "Guyana",
    "11102": "Haiti",
    "11104": "Honduras",
    "11105": "Hungary",
    "11107": "India",
    "11108": "Indonesia",
    "11109": "Iran",
    "11110": "Iraq",
    "11111": "Ireland",
    "11112": "Israel",
    "11113": "Italy",
    "11114": "Jamaica",
    "11115": "Japan",
    "11116": "Jordan",
    "11117": "Kazakhstan",
    "11118": "Kenya",
    "11120": "Korea, North",
    "11121": "Korea, South",
    "11122": "Kuwait",
    "11123": "Kyrgyzstan",
    "11124": "Laos",
    "11125": "Latvia",
    "11126": "Lebanon",
    "11128": "Liberia",
    "11129": "Libya",
    "11130": "Liechtenstein",
    "11132": "Luxembourg",
    "11133": "North Macedonia, The Republic of",
    "11136": "Malaysia",
    "11137": "Maldives",
    "11138": "Mali",
    "11139": "Malta",
    "11140": "Marshall Islands",
    "11141": "Mauritania",
    "11143": "Mexico",
    "11145": "Moldova",
    "11146": "Monaco",
    "11147": "Mongolia",
    "11148": "Morocco",
    "11149": "Mozambique",
    "11150": "Namibia",
    "11153": "Netherlands",
    "11154": "New Zealand",
    "11155": "Nicaragua",
    "11156": "Niger",
    "11157": "Nigeria",
    "11158": "Norway",
    "11159": "Oman",
    "11160": "Pakistan",
    "11161": "Palau",
    "11162": "Panama",
    "11164": "Paraguay",
    "11165": "Peru",
    "11166": "Philippines",
    "11167": "Poland",
    "11168": "Portugal",
    "11169": "Qatar",
    "11170": "Romania",
    "11171": "Russia",
    "11172": "Rwanda",
    "11173": "Saint Kitts and Nevis",
    "11175": "Saint Vincent and the Grenadines",
    "11176": "Samoa",
    "11177": "San Marino",
    "11179": "Saudi Arabia",
    "11180": "Senegal",
    "11181": "Serbia",
    "11182": "Seychelles",
    "11183": "Sierra Leone",
    "11184": "Singapore",
    "11185": "Slovakia",
    "11186": "Slovenia",
    "11188": "Somalia",
    "11189": "South Africa",
    "11190": "Spain",
    "11191": "Sri Lanka",
    "11192": "Sudan",
    "11195": "Sweden",
    "11196": "Switzerland",
    "11197": "Syria",
    "11198": "Tajikistan",
    "11199": "Tanzania",
    "11200": "Thailand",
    "11203": "Trinidad and Tobago",
    "11204": "Tunisia",
    "11205": "Turkey",
    "11206": "Turkmenistan",
    "11208": "Uganda",
    "11209": "Ukraine",
    "11210": "United Arab Emirates",
    "11211": "United Kingdom",
    "11212": "United States",
    "11213": "Uruguay",
    "11214": "Uzbekistan",
    "11215": "Vanuatu",
    "11216": "Venezuela",
    "11217": "Vietnam",
    "11218": "Yemen",
    "11219": "Zambia",
    "11220": "Zimbabwe",
    "11223": "Aruba",
    "11226": "Bermuda",
    "11230": "Cayman Islands",
    "11241": "Gibraltar",
    "11247": "Hong Kong",
    "11250": "Jersey",
    "11253": "Macau",
    "11254": "Man, Isle of",
    "11260": "Netherlands Antilles",
    "11278": "Virgin Islands, British",
    "11291": "undetermined",
    "11292": "West Bank",
    "11391": "Taiwan",
    "91021": "Palestinian",
    "91116": "Kosovo",
    "91192": "Montenegro",
    "91434": "Region: Northern Mali",
    "91501": "South Sudan",
    "91704": "Region: Gaza"
}

# Define CSV file header and path
csv_file_path = "C:/Users/kadam/OneDrive/Documents/GitHub/WLF_Tuning_OFAC_Parser_Dashboard/parser_codebase/address/output_address_demo.csv"
fieldnames = [
    "ID",
    "AreaCodeID",
    "Country",
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
    country_name = country_map.get(country_id, "")
    country_name = country_map.get(country_id, "")
    feature_version_ref = location.find(".//ns:FeatureVersionReference", ns)
    feature_version_id = (
        feature_version_ref.attrib["FeatureVersionID"]
        if feature_version_ref is not None
        else ""
    )

    # Write the Latin script values in one row
    data = {
        "ID": location_id,
        "AreaCodeID": area_code_id,
        "Country": f"{country_name} ({country_id})" if country_name else country_id,
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

            if not comment:
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

    # Write the non-Latin script values in separate rows
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

            if comment:
                data = {
                    "ID": location_id,
                    "AreaCodeID": area_code_id,
                    "Country": f"{country_name} ({country_id})" if country_name else country_id,
                    "FeatureVersionID": feature_version_id,
                    "Unknown": "",
                    "Region": "",
                    "Address 1": "",
                    "Address 2": "",
                    "Address 3": "",
                    "City": "",
                    "State/ Province": "",
                    "Postal Code": "",
                    "Script Type": comment,
                    "Comment": value,
                }

                if part_type_id == "1454":  # City
                    data["City"] = value
                elif part_type_id == "1455":  # State
                    data["State/ Province"] = value
                elif part_type_id == "1456":  # Postal Code
                    data["Postal Code"] = value

                with open(csv_file_path, "a", newline="", encoding="utf-8-sig") as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writerow(data)