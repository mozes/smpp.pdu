# smpp.pdu

smpp.pdu is a Python library for parsing Protocol Data Units (PDUs) in SMPP protocol
http://www.nowsms.com/discus/messages/1/24856.html 

[![Tests](https://github.com/DomAmato/smpp.pdu/workflows/Python%20Test/badge.svg)](https://github.com/DomAmato/smpp.pdu/actions)
[![Coverage Status](https://coveralls.io/repos/github/DomAmato/smpp.pdu/badge.svg?branch=master)](https://coveralls.io/github/DomAmato/smpp.pdu?branch=master)

Examples
========

Decoding (parsing) PDUs
--------------------------
    import binascii
    from io import BytesIO
    from smpp.pdu.pdu_encoding import PDUEncoder

    hex = '0000004d00000005000000009f88f12441575342440001013136353035353531323334000101313737333535353430373000000000000000000300117468657265206973206e6f2073706f6f6e'
    binary = binascii.a2b_hex(hex)
    file = BytesIO(binary)

    pdu = PDUEncoder().decode(file)
    print("PDU: %s" % pdu)

    # Prints the following:
    #
    # PDU: PDU [command: deliver_sm, sequence_number: 2676551972, command_status: ESME_ROK
    # service_type: AWSBD
    # source_addr_ton: INTERNATIONAL
    # source_addr_npi: ISDN
    # source_addr: 16505551234
    # dest_addr_ton: INTERNATIONAL
    # dest_addr_npi: ISDN
    # destination_addr: 17735554070
    # esm_class: EsmClass[mode: DEFAULT, type: DEFAULT, gsmFeatures: set([])]
    # protocol_id: 0
    # priority_flag: LEVEL_0
    # schedule_delivery_time: None
    # validity_period: None
    # registered_delivery: RegisteredDelivery[receipt: NO_SMSC_DELIVERY_RECEIPT_REQUESTED, smeOriginatedAcks: set([]), intermediateNotification: False]
    # replace_if_present_flag: DO_NOT_REPLACE
    # data_coding: DataCoding[scheme: DEFAULT, schemeData: LATIN_1]
    # sm_default_msg_id: None
    # short_message: there is no spoon
    # ]

Creating and encoding PDUs
--------------------------
    import binascii
    from smpp.pdu.pdu_types import *
    from smpp.pdu.operations import *
    from smpp.pdu.pdu_encoding import PDUEncoder

    pdu = SubmitSM(9284,
        service_type='',
        source_addr_ton=AddrTon.ALPHANUMERIC,
        source_addr_npi=AddrNpi.UNKNOWN,
        source_addr='mobileway',
        dest_addr_ton=AddrTon.INTERNATIONAL,
        dest_addr_npi=AddrNpi.ISDN,
        destination_addr='1208230',
        esm_class=EsmClass(EsmClassMode.DEFAULT, EsmClassType.DEFAULT),
        protocol_id=0,
        priority_flag=PriorityFlag.LEVEL_0,
        registered_delivery=RegisteredDelivery(RegisteredDeliveryReceipt.SMSC_DELIVERY_RECEIPT_REQUESTED),
        replace_if_present_flag=ReplaceIfPresentFlag.DO_NOT_REPLACE,
        data_coding=DataCoding(DataCodingScheme.GSM_MESSAGE_CLASS, DataCodingGsmMsg(DataCodingGsmMsgCoding.DEFAULT_ALPHABET, DataCodingGsmMsgClass.CLASS_2)),
        short_message='HELLO',
    )
    print("PDU: %s" % pdu)

    binary = PDUEncoder().encode(pdu)
    hexStr = binascii.b2a_hex(binary)
    print("HEX: %s" % hexStr)
    
    # Prints the following:
    #
    # PDU: PDU [command: submit_sm, sequence_number: 9284, command_status: ESME_ROK
    # service_type: 
    # source_addr_ton: ALPHANUMERIC
    # source_addr_npi: UNKNOWN
    # source_addr: mobileway
    # dest_addr_ton: INTERNATIONAL
    # dest_addr_npi: ISDN
    # destination_addr: 1208230
    # esm_class: EsmClass[mode: DEFAULT, type: DEFAULT, gsmFeatures: set([])]
    # protocol_id: 0
    # priority_flag: LEVEL_0
    # schedule_delivery_time: None
    # validity_period: None
    # registered_delivery: RegisteredDelivery[receipt: SMSC_DELIVERY_RECEIPT_REQUESTED, smeOriginatedAcks: set([]), intermediateNotification: False]
    # replace_if_present_flag: DO_NOT_REPLACE
    # data_coding: DataCoding[scheme: GSM_MESSAGE_CLASS, schemeData: DataCodingGsmMsg[msgCoding: DEFAULT_ALPHABET, msgClass: CLASS_2]]
    # sm_default_msg_id: None
    # short_message: HELLO
    # ]
    # HEX: 000000360000000400000000000024440005006d6f62696c65776179000101313230383233300000000000000100f2000548454c4c4f

Credits
=======
* Thanks to [rtrdev](https://github.com/rtrdev) for adding support for 'more_messages_to_send'
* Thanks to [dliappis](https://github.com/dliappis) for a improvements parsing relative time.
* Thanks to [Andrés Reyes Monge](https://github.com/armonge) for bug fixes parsing QuerySMResp.
* Thanks to [Fourat Zouari](https://github.com/fourat) for many bug reports, fixes, and suggestions.
