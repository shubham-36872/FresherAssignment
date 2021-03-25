import pandas
from xml.dom import minidom
import os
import logging

log_format = '%(asctime)s : %(message)s'
logging.basicConfig(filename='C:\\Users\\nikamak\\Desktop\\Task1\\Logger.log', level=logging.DEBUG
                    , format=log_format)
logger = logging.getLogger()

logger.debug("Extract data from CSV file")

result = pandas.read_csv('C:\\Users\\nikamak\\Desktop\\Task1\\sample_Input.csv')
mavenir_list = [list(i) for i in result.values]

if len(mavenir_list) != 0:
    logger.debug("Successfully read data from CSV File")

list_subsciber = []


def unique_subscriber():
    logger.debug("Searching for unique Audit subscriber")
    for i in mavenir_list:
        mob_no = i[0]
        flag = True
        for j in list_subsciber:
            flag = True
            if j[0] == i[0]:
                flag = False
                break
        if flag:
            list_subsciber.append(i[:3])

    for i in list_subsciber:
        print (i)

    logger.debug("Successfully Searched all unique Audit subscriber")


# Task set 1-B
def filter_service_indication():
    logger.debug("Search for Audit Subscribers on the basis of service indication")
    val = raw_input("Enter service indication: ")
    val = str(val)
    # print (val)

    list_service = []
    for i in mavenir_list:
        service_indi = i[2]
        if service_indi == val:
            list_service.append(i)

    print(list_service)
    logger.debug("Successfully Searched for Audit Subscriber")


##########################################################################
def single_audit_sub_xml():
    root = minidom.Document()

    xml = root.createElement('Audit')
    xml.setAttribute('xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance')
    xml.setAttribute('xsi:noNamespaceSchemaLocation', 'schema.xsd')
    root.appendChild(xml)

    audit_subsciber = root.createElement('auditSubscribers')
    xml.appendChild(audit_subsciber)

    msidn = root.createElement('MSIDN')
    msidn.appendChild(root.createTextNode(str(list_subsciber[0][0])))
    audit_subsciber.appendChild(msidn)

    operation_type = root.createElement('OperationType')
    operation_type.appendChild(root.createTextNode(str(list_subsciber[0][1])))
    audit_subsciber.appendChild(operation_type)

    service_indication = root.createElement('ServiceIndication')
    service_indication.appendChild(root.createTextNode(str(list_subsciber[0][2])))
    audit_subsciber.appendChild(service_indication)

    xml_str = root.toprettyxml(indent="\t")

    save_path_file = "C:\\Users\\nikamak\\Desktop\\Task1\\AuditSubcriber.xml"

    with open(save_path_file, "w") as f:
        f.write(xml_str)

    logger.debug("Xml created for single audit subscriber ")


######################################################################################################################

def multiple_audit_sub_xml():
    root = minidom.Document()

    xml = root.createElement('Audit')
    xml.setAttribute('xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance')
    xml.setAttribute('xsi:noNamespaceSchemaLocation', 'schema.xsd')
    root.appendChild(xml)

    for i in list_subsciber:
        audit_subsciber = root.createElement('auditSubscribers')
        xml.appendChild(audit_subsciber)
        msidn = root.createElement('MSIDN')
        msidn.appendChild(root.createTextNode(str(i[0])))
        audit_subsciber.appendChild(msidn)

        operation_type = root.createElement('OperationType')
        operation_type.appendChild(root.createTextNode(str(i[1])))
        audit_subsciber.appendChild(operation_type)

        service_indication = root.createElement('ServiceIndication')
        service_indication.appendChild(root.createTextNode(str(i[2])))
        audit_subsciber.appendChild(service_indication)

    xml_str = root.toprettyxml(indent="\t")

    save_path_file = "C:\\Users\\nikamak\\Desktop\\Task1\\AuditSubcribers.xml"

    with open(save_path_file, "w") as f:
        f.write(xml_str)

    logger.debug("Xml created for multiple audit subscriber ")


unique_subscriber()
filter_service_indication()
single_audit_sub_xml()
multiple_audit_sub_xml()
