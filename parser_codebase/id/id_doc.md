3. IDs
    a. A row for each identification associated with a sanctioned list entry
    b. The following data attributes should be included:
        i. FixedRef (to relate address back to list entry)
        ii. Document type [<IDRegDocTypeValues>]
        iii. Issued By
        iv. Issue date
        v. Expiration Date
        vi. Value
________________________________

** Tested on:

##### Test 1: Multiple entries with same identityID/ fixedRef but with no expiration and issue dates
<IDRegDocument ID="4950" IDRegDocTypeID="1600" IdentityID="724" IssuedBy-CountryID="11143" ValidityID="1">
<Comment />
<IDRegistrationNo>ZANT690617MSLMBR01</IDRegistrationNo>
<IssuingAuthority />
<DocumentedNameReference DocumentedNameID="724" />
</IDRegDocument>
<IDRegDocument ID="4951" IDRegDocTypeID="1573" IdentityID="724" IssuedBy-CountryID="11143" ValidityID="1">
<Comment />
<IDRegistrationNo>ZANT-690617-B73</IDRegistrationNo>
<IssuingAuthority />
<DocumentedNameReference DocumentedNameID="724" />
</IDRegDocument>
<IDRegDocument ID="4952" IDRegDocTypeID="1571" IdentityID="724" IssuedBy-CountryID="11143" ValidityID="1">
<Comment />
<IDRegistrationNo>97040021870</IDRegistrationNo>
<IssuingAuthority />
<DocumentedNameReference DocumentedNameID="724" />
</IDRegDocument>

--> Above are tested on fixedRef = 10359 with corresponding identityID = 724

##### Test 2: Multiple entries with same identityID/ fixedRef but with  expiration and issue dates

--> Above are tested on fixedRef = 13057 and 13058 and 13061


_______________________________
1. ask what does issued by refer? is it issuing country or issuing authority
  ### ASK : ALEX --- resolved 
2. Test the authority values 
   - 33862,1619

3. Test FixedRef
    - 1008,1571,,1979-7-30,,P-537849

4. ask how the time format is working in the start itself we have from-to and end from-to
    ### ASK : ALEX

<IDRegDocTypeValues>
      <IDRegDocType ID="1570">Cedula No.</IDRegDocType>
      <IDRegDocType ID="1571">Passport</IDRegDocType>
      <IDRegDocType ID="1572">SSN</IDRegDocType>
      <IDRegDocType ID="1573">R.F.C.</IDRegDocType>
      <IDRegDocType ID="1574">D.N.I.</IDRegDocType>
      <IDRegDocType ID="1575">NIT #</IDRegDocType>
      <IDRegDocType ID="1576">US FEIN</IDRegDocType>
      <IDRegDocType ID="1577">Driver's License No.</IDRegDocType>
      <IDRegDocType ID="1578">RUC #</IDRegDocType>
      <IDRegDocType ID="1579">N.I.E.</IDRegDocType>
      <IDRegDocType ID="1580">C.I.F.</IDRegDocType>
      <IDRegDocType ID="1581">Business Registration Document #</IDRegDocType>
      <IDRegDocType ID="1582">RIF #</IDRegDocType>
      <IDRegDocType ID="1584">National ID No.</IDRegDocType>
      <IDRegDocType ID="1585">Registration ID</IDRegDocType>
      <IDRegDocType ID="1586">LE Number</IDRegDocType>
      <IDRegDocType ID="1587">Bosnian Personal ID No.</IDRegDocType>
      <IDRegDocType ID="1588">Registered Charity No.</IDRegDocType>
      <IDRegDocType ID="1589">V.A.T. Number</IDRegDocType>
      <IDRegDocType ID="1590">Credencial electoral</IDRegDocType>
      <IDRegDocType ID="1591">Kenyan ID No.</IDRegDocType>
      <IDRegDocType ID="1592">Italian Fiscal Code</IDRegDocType>
      <IDRegDocType ID="1593">Serial No.</IDRegDocType>
      <IDRegDocType ID="1594">C.I.N.</IDRegDocType>
      <IDRegDocType ID="1595">C.U.I.T.</IDRegDocType>
      <IDRegDocType ID="1596">Tax ID No.</IDRegDocType>
      <IDRegDocType ID="1597">Moroccan Personal ID No.</IDRegDocType>
      <IDRegDocType ID="1598">Public Security and Immigration No.</IDRegDocType>
      <IDRegDocType ID="1600">C.U.R.P.</IDRegDocType>
      <IDRegDocType ID="1601">British National Overseas Passport</IDRegDocType>
      <IDRegDocType ID="1602">C.R. No.</IDRegDocType>
      <IDRegDocType ID="1603">UK Company Number</IDRegDocType>
      <IDRegDocType ID="1604">Immigration No.</IDRegDocType>
      <IDRegDocType ID="1605">Travel Document Number</IDRegDocType>
      <IDRegDocType ID="1607">Electoral Registry No.</IDRegDocType>
      <IDRegDocType ID="1608">Identification Number</IDRegDocType>
      <IDRegDocType ID="1609">Paraguayan tax identification number</IDRegDocType>
      <IDRegDocType ID="1611">National Foreign ID Number</IDRegDocType>
      <IDRegDocType ID="1612">RFC</IDRegDocType>
      <IDRegDocType ID="1613">Diplomatic Passport</IDRegDocType>
      <IDRegDocType ID="1614">Dubai Chamber of Commerce Membership No.</IDRegDocType>
      <IDRegDocType ID="1615">Trade License No.</IDRegDocType>
      <IDRegDocType ID="1619">Commercial Registry Number</IDRegDocType>
      <IDRegDocType ID="1620">Certificate of Incorporation Number</IDRegDocType>
      <IDRegDocType ID="1621">Tourism License No.</IDRegDocType>
      <IDRegDocType ID="1623">Aircraft Serial Identification</IDRegDocType>
      <IDRegDocType ID="1624">Cartilla de Servicio Militar Nacional</IDRegDocType>
      <IDRegDocType ID="1625">C.U.I.P.</IDRegDocType>
      <IDRegDocType ID="1626">Vessel Registration Identification</IDRegDocType>
      <IDRegDocType ID="1627">Personal ID Card</IDRegDocType>
      <IDRegDocType ID="1629">Registration Certificate Number (Dubai)</IDRegDocType>
      <IDRegDocType ID="1630">VisaNumberID</IDRegDocType>
      <IDRegDocType ID="1631">Matricula Mercantil No</IDRegDocType>
      <IDRegDocType ID="1632">Residency Number</IDRegDocType>
      <IDRegDocType ID="1633">Numero Unico de Identificacao Tributaria (NUIT)</IDRegDocType>
      <IDRegDocType ID="1634">CNP (Personal Numerical Code)</IDRegDocType>
      <IDRegDocType ID="1635">Romanian Permanent Resident</IDRegDocType>
      <IDRegDocType ID="1636">Government Gazette Number</IDRegDocType>
      <IDRegDocType ID="1638">Fiscal Code</IDRegDocType>
      <IDRegDocType ID="1639">Pilot License Number</IDRegDocType>
      <IDRegDocType ID="1642">Romanian C.R.</IDRegDocType>
      <IDRegDocType ID="1643">Folio Mercantil No.</IDRegDocType>
      <IDRegDocType ID="1644">Istanbul Chamber of Comm. No.</IDRegDocType>
      <IDRegDocType ID="1645">Turkish Identification Number</IDRegDocType>
      <IDRegDocType ID="1646">Romanian Tax Registration</IDRegDocType>
      <IDRegDocType ID="1647">Stateless Person Passport</IDRegDocType>
      <IDRegDocType ID="1648">Stateless Person ID Card</IDRegDocType>
      <IDRegDocType ID="1649">Refugee ID Card</IDRegDocType>
      <IDRegDocType ID="91236">Afghan Money Service Provider License Number</IDRegDocType>
      <IDRegDocType ID="91264">MMSI</IDRegDocType>
      <IDRegDocType ID="91412">Company Number</IDRegDocType>
      <IDRegDocType ID="91475">Public Registration Number</IDRegDocType>
      <IDRegDocType ID="91478">N.I.F.</IDRegDocType>
      <IDRegDocType ID="91481">RTN</IDRegDocType>
      <IDRegDocType ID="91482">Numero de Identidad</IDRegDocType>
      <IDRegDocType ID="91484">SRE Permit No.</IDRegDocType>
      <IDRegDocType ID="91492">Tazkira National ID Card</IDRegDocType>
      <IDRegDocType ID="91504">License</IDRegDocType>
      <IDRegDocType ID="91508">Chinese Commercial Code</IDRegDocType>
      <IDRegDocType ID="91712">I.F.E.</IDRegDocType>
      <IDRegDocType ID="91719">Branch Unit Number</IDRegDocType>
      <IDRegDocType ID="91720">Enterprise Number</IDRegDocType>
      <IDRegDocType ID="91721">Organization Code</IDRegDocType>
      <IDRegDocType ID="91739">Citizen's Card Number</IDRegDocType>
      <IDRegDocType ID="91740">UAE Identification</IDRegDocType>
      <IDRegDocType ID="91747">United Social Credit Code Certificate (USCCC)</IDRegDocType>
      <IDRegDocType ID="91751">Chamber of Commerce Number</IDRegDocType>
      <IDRegDocType ID="91752">Legal Entity Number</IDRegDocType>
      <IDRegDocType ID="91753">Business Number</IDRegDocType>
      <IDRegDocType ID="91759">Birth Certificate Number</IDRegDocType>
      <IDRegDocType ID="91760">Business Registration Number</IDRegDocType>
      <IDRegDocType ID="91761">Registration Number</IDRegDocType>
      <IDRegDocType ID="91812">MSB Registration Number</IDRegDocType>
      <IDRegDocType ID="91835">File Number</IDRegDocType>
      <IDRegDocType ID="91854">C.U.I.</IDRegDocType>
      <IDRegDocType ID="91891">Seafarer's Identification Document</IDRegDocType>
      <IDRegDocType ID="92001">Unified Social Credit Code (USCC)</IDRegDocType>
      <IDRegDocType ID="92067">Central Registration System Number</IDRegDocType>
      <IDRegDocType ID="92121">Economic Register Number (CBLS)</IDRegDocType>
      <IDRegDocType ID="92158">Trademark number</IDRegDocType>
      <IDRegDocType ID="92159">Permit Number</IDRegDocType>
      <IDRegDocType ID="92728">Military Registration Number</IDRegDocType>
      <IDRegDocType ID="92772">Russian State Individual Business Registration Number Pattern (OGRNIP)</IDRegDocType>
    </IDRegDocTypeValues>