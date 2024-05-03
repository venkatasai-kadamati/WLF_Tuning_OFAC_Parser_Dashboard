import csv
import xml.etree.ElementTree as ET

tree = ET.parse("source_documents/sdn_advanced.xml")
root = tree.getroot()

ns = {"ns": "http://www.un.org/sanctions/1.0"}

with open(
    "parser_codebase/id/new_fixedREF_idregdocuments.csv",
    "w",
    newline="",
    encoding="utf-8-sig",
) as csvfile:
    fieldnames = [
        "FixedRef",
        "Document_Type",
        "Issued_By",
        "Issue_Date",
        "Expiration_Date",
        "Value",
    ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for idregdocument in root.findall(".//ns:IDRegDocument", ns):
        identity_id = idregdocument.attrib["IdentityID"]
        distinct_party = root.find(
            f".//ns:DistinctParty/ns:Profile/ns:Identity[@ID='{identity_id}']", ns
        )

        if distinct_party is not None:
            fixed_ref = distinct_party.attrib["FixedRef"]
            data = {
                "FixedRef": fixed_ref,
                "Document_Type": idregdocument.attrib["IDRegDocTypeID"],
                "Issued_By": idregdocument.find(".//ns:IssuingAuthority", ns).text,
                "Issue_Date": "",
                "Expiration_Date": "",
                "Value": idregdocument.find(".//ns:IDRegistrationNo", ns).text,
            }

            documentdate = idregdocument.find(".//ns:DocumentDate", ns)
            if documentdate is not None:
                idregdocdatetypeid = documentdate.attrib["IDRegDocDateTypeID"]
                dateperiod = documentdate.find(".//ns:DatePeriod", ns)
                if dateperiod is not None:
                    start = dateperiod.find(".//ns:Start", ns)
                    if start is not None:
                        issue_date = (
                            f"{start.find('.//ns:Year', ns).text}-"
                            f"{start.find('.//ns:Month', ns).text}-"
                            f"{start.find('.//ns:Day', ns).text}"
                        )
                        if idregdocdatetypeid == "1480":
                            data["Issue_Date"] = issue_date

                    end = dateperiod.find(".//ns:End", ns)
                    if end is not None:
                        expiration_date = (
                            f"{end.find('.//ns:Year', ns).text}-"
                            f"{end.find('.//ns:Month', ns).text}-"
                            f"{end.find('.//ns:Day', ns).text}"
                        )
                        if idregdocdatetypeid == "1481":
                            data["Expiration_Date"] = expiration_date

            writer.writerow(data)
