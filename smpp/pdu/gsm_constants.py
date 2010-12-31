#http://www.3gpp.org/ftp/Specs/html-info/23040.htm
#http://www.3gpp.org/ftp/Specs/archive/23_series/23.040/23040-100.zip
#only defining SMS control constants (only some of those for that matter)
#assuming that only non-repeatable parameters can be mutually exclusive
information_element_identifier_full_value_map = {
    0x00: {
        'name': 'CONCATENATED_SM_8BIT_REF_NUM',
        'repeatable': False,
        'excludes': ['CONCATENATED_SM_16BIT_REF_NUM'],
    },
    0x01: {
        'name': 'SPECIAL_SMS_MESSAGE_INDICATION',
        'repeatable': True,
    },
    0x04: {
        'name': 'APPLICATION_PORT_ADDRESSING_SCHEME_8BIT',
        'repeatable': False,
        'excludes': ['APPLICATION_PORT_ADDRESSING_SCHEME_16BIT'],
    },
    0x05: {
        'name': 'APPLICATION_PORT_ADDRESSING_SCHEME_16BIT',
        'repeatable': False,
        'excludes': ['APPLICATION_PORT_ADDRESSING_SCHEME_8BIT'],
    },
    0x06: {
        'name': 'SMSC_CONTROL_PARAMETERS',
        'repeatable': False,
        'excludes': [],
    },
    0x07: {
        'name': 'UDH_SOURCE_INDICATOR',
        'repeatable': True,
    },
    0x08: {
        'name': 'CONCATENATED_SM_16BIT_REF_NUM',
        'repeatable': False,
        'excludes': ['CONCATENATED_SM_8BIT_REF_NUM'],
    },
    0x09: {
        'name': 'WIRELESS_CONTROL_MESSAGE_PROTOCOL',
        'repeatable': False,
        'excludes': [],
    },
    0x20: {
        'name': 'RFC_822_EMAIL_HEADER',
        'repeatable': False,
        'excludes': [],
    },
    0x21: {
        'name': 'HYPERLINK_FORMAT_ELEMENT',
        'repeatable': True,
        'excludes': [],
    },
    0x22: {
        'name': 'REPLY_ADDRESS_ELEMENT',
        'repeatable': False,
        'excludes': [],
    },
    0x23: {
        'name': 'ENHANCED_VOICE_MAIL_INFORMATION',
        'repeatable': False,
        'excludes': [],
    },
    0x24: {
        'name': 'NATIONAL_LANGUAGE_SINGLE_SHIFT',
        'repeatable': False,
        'excludes': [],
    },
    0x25: {
        'name': 'NATIONAL_LANGUAGE_LOCKING_SHIFT',
        'repeatable': False,
        'excludes': [],
    },
}
information_element_identifier_name_map = dict([(val['name'], key) for (key, val) in information_element_identifier_full_value_map.items()])
information_element_identifier_value_map = dict([(val, key) for (key, val) in information_element_identifier_name_map.items()])
