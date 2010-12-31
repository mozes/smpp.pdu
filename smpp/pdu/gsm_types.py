from enum import Enum
from smpp.pdu.namedtuple import namedtuple
from smpp.pdu import gsm_constants

InformationElementIdentifier = Enum(*gsm_constants.information_element_identifier_name_map.keys())

InformationElement = namedtuple('InformationElement', 'identifier, data')

IEConcatenatedSM = namedtuple('IEConcatenatedSM', 'referenceNum, maximumNum, sequenceNum')
