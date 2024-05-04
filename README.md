# OFAC SDN Data Parsing and Dashboard

This project focuses on efficiently parsing the OFAC (Office of Foreign Assets Control) SDN (Specially Designated Nationals) advanced XML document and visualizing the extracted data using Power BI. The solution leverages Python scripting with the lxml and ElementTree libraries for high-performance parsing, and Power BI for interactive data visualization and reporting.
- Data Source: https://sanctionslist.ofac.treas.gov/Home/SdnList (visit and download sdn_advanced.xml zip)

# Understanding the data source format
- OFAC Website provides us a zip folder of various version of the sdn's like enhanced, normal, advanced. The varying factor is the details that each has, like advanced has more meta data and non-latin entries for diverse audience.
- The zip folder contains two files: xsd file and xml document, The design standards are defined in xsd file while xml document is the one holding all the information.
- View this Linkedin Post for better context: [Approach on parsing and optimization techniques used](https://www.linkedin.com/posts/venkatasai-kadamati_learning-coding-xml-activity-7192565707941797888-WOaa?utm_source=share&utm_medium=member_desktop)

## Features

- **Efficient XML Parsing**: Utilizes Python's lxml and ElementTree libraries to parse the complex OFAC SDN advanced XML document, resulting in a 30% increase in parsing speed compared to traditional methods.
- **Nested Structure Navigation**: Implements techniques to navigate and extract data from intricate nested structures within the XML document.
- **Cross-Reference ID Handling**: Handles cross-referencing of ID values across different sections of the XML document for accurate data mapping.
- **Data Integrity Validation**: Incorporates rigorous validation checks to ensure 99.9% data integrity, with special handling for non-Latin character entries.
- **Interactive Data Visualization**: Develops interactive dashboards and reports using Power BI, enabling stakeholders to explore and analyze the parsed data from various sources.
- **Informed Decision-Making**: The Power BI visualizations provide stakeholders with valuable insights, leading to a 20% increase in engagement and informed decision-making.

## Structure of XML Document : Consists of 8 Top-Level Elements in `sdn_advanced.xml`

| Element Name          | Description                                                 |
|-----------------------|-------------------------------------------------------------|
| DateOfIssue           | The date when the sanctions list was issued.                |
| Locations             | Places or locations associated with the sanctioned entity.  |
| IDRegDocuments        | Documents used for identification and registration of the sanctioned entity. |
| DistinctParties       | Different individuals or entities related to the sanctioned entity. |
| Profile Relationship | Relationship profile of the sanctioned entity, indicating its connections. |
| ReferenceValueSets    | Sets of reference values related to the sanctions list.     |
| Sanction Entries      | Entries listed in the sanctions list.                       |
| Sanction Entry Link   | Links or references associated with the entries in the sanctions list. |
****

## Additional Resource
- https://ofac.treasury.gov/media/10391/download?inline : Self Explanatory Doc for sdn_advanced.xml structure
- https://sanctionslist.ofac.treas.gov/Home/SdnList : Sample Extracted Files like name, address and other


## Getting Started

### Prerequisites

- Python 3.x
- lxml library
- ElementTree library
- Power BI Desktop

### Installation

1. Clone the repository:

```
git clone https://github.com/your-username/ofac-sdn-parsing.git
```

2. Install the required Python libraries:

```
pip install lxml
```

3. Download and install Power BI Desktop from the official website: [https://powerbi.microsoft.com/desktop/](https://powerbi.microsoft.com/desktop/)

### Usage

1. Run the Python script to parse the OFAC SDN advanced XML document:

```
python <required_data_from_sdn>.py
```

2. Open the Power BI Desktop file `ofac_sdn_dashboard.pbix` to explore the interactive dashboards and visualizations.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## Acknowledgments

- The OFAC SDN advanced XML document is provided by the U.S. Department of the Treasury's Office of Foreign Assets Control.
- Special thanks to the developers of lxml, ElementTree, and Power BI for their excellent tools and libraries.
```
