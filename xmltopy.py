import xmltodict

with open("xml_example.xml") as data:
    xml_sample = data.read()

xml_dict = xmltodict.parse(xml_sample)

xml_dict["device"]["IP"] = "192.168.55.3"

with open("xml_example.xml", "w") as data:
    data.write(xmltodict.unparse(xml_dict, pretty=True))

print(xml_dict)

