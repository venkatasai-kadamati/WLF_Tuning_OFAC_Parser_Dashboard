import csv
import xml.etree.ElementTree as ET

# Define the file paths
xml_fp = r"C:\Users\kadam\OneDrive\Documents\GitHub\WLF_Tuning_OFAC_Parser_Dashboard\source_documents\sdn_advanced.xml"
output_fp = "C:/Users/kadam/OneDrive/Documents/GitHub/WLF_Tuning_OFAC_Parser_Dashboard/parser_codebase/id/output_id_with_countryvalues.csv"
country_values_fp = "C:/Users/kadam/OneDrive/Documents/GitHub/WLF_Tuning_OFAC_Parser_Dashboard/parser_codebase/id/countryvalues.txt"  # Assuming this file contains the <CountryValues> XML data
doc_type_values_fp = "C:/Users/kadam/OneDrive/Documents/GitHub/WLF_Tuning_OFAC_Parser_Dashboard/parser_codebase/id/doctypevalues.txt"  # Assuming this file contains the <IDRegDocTypeValues> XML data

# Parse the XML document for country values
country_tree = ET.parse(country_values_fp)
country_root = country_tree.getroot()

# Create a mapping from Country ID to Country Name
country_mapping = {}
for country in country_root.findall(".//Country"):
    country_id = country.attrib["ID"]
    country_name = country.text
    country_mapping[country_id] = country_name

# Parse the XML document for document type values
doc_type_tree = ET.parse(doc_type_values_fp)
doc_type_root = doc_type_tree.getroot()

# Create a mapping from Document Type ID to Document Type Name
doc_type_mapping = {}
for doc_type in doc_type_root.findall(".//IDRegDocType"):
    doc_type_id = doc_type.attrib["ID"]
    doc_type_name = doc_type.text
    doc_type_mapping[doc_type_id] = doc_type_name

# Parse the main XML document
tree = ET.parse(xml_fp)
root = tree.getroot()

# Define the namespace
ns = {"ns": "http://www.un.org/sanctions/1.0"}

# Open the CSV file for writing
with open(output_fp, "w", newline="", encoding="utf-8-sig") as csvfile:
    fieldnames = [
        "FixedRef",
        "Document_Type_ID",
        "Document_Type_Name",
        "Issued_By",
        "Issuing_Country_ID",
        "Issuing_Country_Name",
        "Issue_Date",
        "Expiration_Date",
        "Value",
    ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Iterate over each IDRegDocument element
    for idregdocument in root.findall(".//ns:IDRegDocument", ns):
        identity_id = idregdocument.attrib["IdentityID"]
        distinct_party = root.find(
            f".//ns:DistinctParty/ns:Profile/ns:Identity[@ID='{identity_id}']", ns
        )

        if distinct_party is not None:
            fixed_ref = distinct_party.attrib["FixedRef"]
            document_type_id = idregdocument.attrib["IDRegDocTypeID"]
            document_type_name = doc_type_mapping.get(document_type_id, "Unknown Document Type")
            issued_by = idregdocument.find(".//ns:IssuingAuthority", ns).text if idregdocument.find(".//ns:IssuingAuthority", ns) is not None else ""
            issued_by_country_id = idregdocument.attrib.get("IssuedBy-CountryID", "")
            issued_by_country_name = country_mapping.get(issued_by_country_id, "Unknown Country")
            value = idregdocument.find(".//ns:IDRegistrationNo", ns).text if idregdocument.find(".//ns:IDRegistrationNo", ns) is not None else ""

            # Initialize date variables
            issue_date = ""
            expiration_date = ""

            # Find all DocumentDate elements related to the IDRegDocument
            # Find all DocumentDate elements related to the IDRegDocument
            for documentdate in idregdocument.findall(".//ns:DocumentDate", ns):
                idregdocdatetypeid = documentdate.attrib["IDRegDocDateTypeID"]
                dateperiod = documentdate.find(".//ns:DatePeriod", ns)
                if dateperiod is not None:
                    # Extract the start date
                    start = dateperiod.find(".//ns:Start", ns)
                    if start is not None:
                        start_year = start.find(".//ns:Year", ns).text if start.find(".//ns:Year", ns) is not None else ""
                        start_month = start.find(".//ns:Month", ns).text if start.find(".//ns:Month", ns) is not None else ""
                        start_day = start.find(".//ns:Day", ns).text if start.find(".//ns:Day", ns) is not None else ""
                        issue_date = f"{start_year}-{start_month}-{start_day}"

                    # Extract the end date
                    end = dateperiod.find(".//ns:End", ns)
                    if end is not None:
                        end_year = end.find(".//ns:Year", ns).text if end.find(".//ns:Year", ns) is not None else ""
                        end_month = end.find(".//ns:Month", ns).text if end.find(".//ns:Month", ns) is not None else ""
                        end_day = end.find(".//ns:Day", ns).text if end.find(".//ns:Day", ns) is not None else ""
                        expiration_date = f"{end_year}-{end_month}-{end_day}"

                # Assign dates based on the IDRegDocDateTypeID
                if idregdocdatetypeid == "1480":
                    data["Issue_Date"] = issue_date
                elif idregdocdatetypeid == "1481":
                    data["Expiration_Date"] = expiration_date

            # Write the data to the CSV file
            data = {
                "FixedRef": fixed_ref,
                "Document_Type_ID": document_type_id,
                "Document_Type_Name": document_type_name,
                "Issued_By": issued_by,
                "Issuing_Country_ID": issued_by_country_id,
                "Issuing_Country_Name": issued_by_country_name,
                "Issue_Date": issue_date,
                "Expiration_Date": expiration_date,
                "Value": value,
            }
            writer.writerow(data)
#%%
