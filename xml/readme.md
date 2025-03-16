[[_TOC_]]

# XML Schema

## What was I trying ?

sipmle XML document validation using a referenced schema

```xml
<?xml version="1.0" encoding="UTF-8"?>
<addressBook>
    <card>
        <name weight="11">123</name>
        can you do time validation
        <email>djd</email>
        <age>kddk</age>
    </card>
</addressBook>
```

## How do you reference a schema ?

VS Code appears to pick up the .RNG file automatically!

## Which extension ?
Redhat XML

##  Reference

https://developers.redhat.com/articles/2022/11/29/new-vscode-xml-extension-improves-developer-experience#1__relaxng_support

https://github.com/redhat-developer/vscode-xml/blob/main/docs/Features/RelaxNGFeatures.md#relaxng-features


## What did I learn ?

- There is a .RNG format
- Relax NG schema
- Not very hard

## XSD vs RNG

Among the XML schema languages, **XSD (XML Schema Definition)** is the most popular and widely used³. XSD is preferred because it provides more powerful and flexible ways to define the structure and data types of XML documents compared to DTD (Document Type Definition) and RNG (RELAX NG). 

Here are some reasons for XSD's popularity:
- **Namespace Support**: XSD supports XML namespaces, which is crucial for avoiding element name conflicts in complex XML documents.
- **Data Types**: XSD allows for defining data types and constraints on element and attribute values, making it more robust for data validation.
- **Extensibility**: XSD schemas can be extended and reused, which is beneficial for large and evolving XML applications.
- **Tool Support**: There is extensive tool support for XSD in various XML parsers and editors, making it easier to work with.

DTD is still used, especially for simpler XML documents, due to its simplicity and historical presence³. RELAX NG is appreciated for its simplicity and flexibility, but it is less commonly used compared to XSD⁴.

Do you have a specific project or use case in mind where you need to choose an XML schema language?

Source: Conversation with Copilot, 21/09/2024
(1) XML schema - Wikipedia. https://en.wikipedia.org/wiki/XML_schema.
(2) RELAX NG - Wikipedia. https://en.wikipedia.org/wiki/RELAX_NG.
(3) xsd - Equivalence of DTDs and XMLSchemas - Stack Overflow. https://stackoverflow.com/questions/724374/equivalence-of-dtds-and-xmlschemas.
(4) BITS: Book Interchange Tag Set - Journal Article Tag Suite. https://jats.nlm.nih.gov/extensions/bits/.
(5) NISO STS DTDs, XSDs, & RNGs for Download. https://www.niso-sts.org/DTDs-XSDs-RNGs.html.
(6) undefined. http://www.w3.org/2001/XMLSchema.
(7) undefined. https://jats.nlm.nih.gov/extensions/bits/tag-library/.
(8) undefined. https://public.nlm.nih.gov/projects/jats/extensions/bits/.
(9) undefined. http://www.mulberrytech.com/JATS/JATS-List/index.html.


# XSD Schema

https://www.w3schools.com/xml/schema_example.asp

## I added a discount element to the schema

Notice the `maxOccurs` and `minOccurs` attributes in the `discount` element of the Schema:

```xml
<xs:complexType name="itemtype">
  <xs:sequence>
    <xs:element name="title" type="stringtype"/>
    <xs:element name="note" type="stringtype" minOccurs="0"/>
    <xs:element name="quantity" type="inttype"/>
    <xs:element name="discount" type="xs:decimal" minOccurs="0" maxOccurs="1"/>
    <xs:element name="price" type="dectype"/>
  </xs:sequence>
</xs:complexType>

```

Sample XML fragment:
```xml
  <item>
    <title>Empire Burlesque</title>
    <note>Special Edition</note>
    <quantity>11</quantity>
    <discount>123</discount>
    <price>10.90</price>
  </item>
  <item>
    <title>Hide your heart</title>
    <quantity>1</quantity>
    <price>9.90</price>
  </item>

```

## Simple regex validation for hh:mm

### xs:pattern  to validate timeofdaytype
I added the `timeofdaytype` element definition to the schema. 

```xml
<xs:simpleType name="timeofdaytype">
  <xs:restriction base="xs:string">
    <xs:pattern value="[0-2]{1}\d:[0-5]{1}\d"></xs:pattern>
  </xs:restriction>
</xs:simpleType>

```

### Referencing the new element type timeofdaytype
The `timeofdaytype` is referenced in the `starttime` element of the `itemtype`  definition

```xml
<xs:complexType name="itemtype">
  <xs:sequence>
    <xs:element name="title" type="stringtype"/>
    <xs:element name="note" type="stringtype" minOccurs="0"/>
    <xs:element name="quantity" type="inttype"/>
    <xs:element name="discount" type="xs:decimal" minOccurs="0" maxOccurs="1"/>
    <xs:element name="price" type="dectype"/>
    <xs:element name="starttime" type="timeofdaytype" minOccurs="0" maxOccurs="1" ></xs:element>
  </xs:sequence>
</xs:complexType>

```

### Creating a new element in the XML

```xml
  <item>
    <title>Empire Burlesque</title>
    <note>Special Edition</note>
    <quantity>11</quantity>
    <discount>123</discount>
    <price>10.90</price>
    <starttime>22:30</starttime>
  </item>
```