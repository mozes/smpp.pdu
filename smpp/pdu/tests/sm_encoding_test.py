"""
Copyright 2009-2010 Mozes, Inc.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""
import unittest, binascii, StringIO
from smpp.pdu.sm_encoding import SMStringEncoder
from smpp.pdu.pdu_types import *
from smpp.pdu.gsm_types import *
from smpp.pdu.pdu_encoding import PDUEncoder

class SMDecoderTest(unittest.TestCase):

    def getPDU(self, hexStr):
        return PDUEncoder().decode(StringIO.StringIO(binascii.a2b_hex(hexStr)))

    def test_decode_UCS2(self):
        pduHex = '000000480000000500000000dfd03a56415753424400010131363530383638343135320001013137373338323834303730000000000000000008000c00f10075014400ed00fc0073'
        pdu = self.getPDU(pduHex)
        smStr = SMStringEncoder().decodeSM(pdu)
        self.assertEquals('\x00\xf1\x00u\x01D\x00\xed\x00\xfc\x00s', smStr.bytes)
        self.assertEquals(u'\xf1u\u0144\xed\xfcs', smStr.unicode)
        self.assertEquals(None, smStr.udh)

    def test_decode_default_alphabet(self):
        #'T- Mobile flip phone \xa7 \xa8 N random special charcters'
        pduHex = '0000006f00000005000000005d3fe724544d4f4249000101313635303238333339323600010131373733383238343037300000000000000000000033542d204d6f62696c6520666c69702070686f6e6520a720a8204e2072616e646f6d207370656369616c20636861726374657273'
        # pduHex = '00000085000000050000000046e4983200010136313435303037393434350001013134303436363533343130000000000000000000004e49276d204361646574204a617272796420526564696e67657220204254572e20616e642049276d206e6f7420736f6d65206372617a79206f766572206f627365737365642066616e2e204c6f6c2e'
        # pduHex = '000000480000000500000000ed7527330001013434373534383932373631300001013134303436363533343130000000000000000000001057686f2069732074686973203f207878'
        # pduHex = '0000006f0000000500000000d2f5d8500001013439313736363634363134303500010131343034363635333431300000000000000000000036486179206a757374696e212049276d20612066616e2066726f6d206765726d616e792e2049206c6f766520796f7521204d6720706c73'
        pdu = self.getPDU(pduHex)
        self.assertRaises(UnicodeDecodeError, SMStringEncoder().decodeSM, pdu)
    
    def test_decode_latin1(self):
        pduHex = '0000004200000005000000002a603d56415753424400010131363530383638343135320001013137373338323834303730000000000000000003000645737061f161'
        # pduHex = '000000490000000500000000b9b7e456544d4f424900010131323533383836333438370001013134303436363533343130000000000000000000000d49206c7576206a757374696e21'
        # pduHex = '0000005600000005000000006e1c8745535052494e000101313635303831343532353200010131373733383238343037300000000000000000030014537072696e74204d6f746f5120657370615f6f6c020400020642'
        pdu = self.getPDU(pduHex)
        smStr = SMStringEncoder().decodeSM(pdu)
        self.assertEquals('Espa\xf1a', smStr.bytes)
        self.assertEquals(u'Espa\xf1a', smStr.unicode)
        self.assertEquals(None, smStr.udh)

    def test_decode_ascii(self):
        pduHex = '00000054000000050000000008c72a4154454c4550000101313232383231363236363200010131343034363635333431300000ff010000000001000e49732074686973206a757374696e0201000100020d000101'
        pdu = self.getPDU(pduHex)
        smStr = SMStringEncoder().decodeSM(pdu)
        self.assertEquals('Is this justin', smStr.bytes)
        self.assertEquals('Is this justin', smStr.unicode)
        self.assertEquals(None, smStr.udh)

    def test_decode_octet_unspecified_common(self):
        # pduHex = '0000009e00000005000000007ea4fa4142454c4c4d0001013135303634343038313336000101313430343636353334313000000000000000000400454849204a555354494e2c2049204c4f564520594f5520494d20594f555220424947474553542046414e212e0d4c6f76652c0d44616b6f74612066726f6d2043616e6164612e020400021caf02010001000381000e0102013530363434303831333600'
        pduHex = '000000a900000005000000003cf78935415753424400010131363134333132343337320001013134303436363533343130004000000000000004006d06050423f40000424547494e3a56434152440d0a56455253494f4e3a322e310d0a4e3b434841525345543d5554462d383a4269656265723b4a757374696e0d0a54454c3b564f4943453b434841525345543d5554462d383a343034363635333431300d0a454e443a5643415244'
        pdu = self.getPDU(pduHex)
        self.assertRaises(NotImplementedError, SMStringEncoder().decodeSM, pdu)
        
    def test_decode_default_alphabet_with_udh(self):
        pduHex = '000000db0000000500000000da4b62474652414e4300010133333632383631353033380001013134303436363533343130004000000000000000009f0500032403016869206a757374696e20686f772061726520796f753f204d79206e616d65206973204e616a65742069276d206672656e636820616e6420692077616e74656420746f2074656c6c20796f7520686f77206d7563682069206c6f766520796f752c20796f75206b6e6f7720796f75207361766564206d79206c69666520616e642069207265616c6c79207468616e6b20796f7520666f72207468'
        pdu = self.getPDU(pduHex)
        smStr = SMStringEncoder().decodeSM(pdu)
        self.assertEquals("\x05\x00\x03$\x03\x01hi justin how are you? My name is Najet i'm french and i wanted to tell you how much i love you, you know you saved my life and i really thank you for th", smStr.bytes)
        self.assertEquals("hi justin how are you? My name is Najet i'm french and i wanted to tell you how much i love you, you know you saved my life and i really thank you for th", smStr.unicode)
        self.assertEquals([InformationElement(InformationElementIdentifier.CONCATENATED_SM_8BIT_REF_NUM, IEConcatenatedSM(0x24, 0x03, 0x01))], smStr.udh)
        
    def test_isConcatenatedSM_true(self):
        pduHex = '000000db0000000500000000da4b62474652414e4300010133333632383631353033380001013134303436363533343130004000000000000000009f0500032403016869206a757374696e20686f772061726520796f753f204d79206e616d65206973204e616a65742069276d206672656e636820616e6420692077616e74656420746f2074656c6c20796f7520686f77206d7563682069206c6f766520796f752c20796f75206b6e6f7720796f75207361766564206d79206c69666520616e642069207265616c6c79207468616e6b20796f7520666f72207468'
        pdu = self.getPDU(pduHex)
        self.assertTrue(SMStringEncoder().isConcatenatedSM(pdu))
        iElem = SMStringEncoder().getConcatenatedSMInfoElement(pdu)
        self.assertEquals(InformationElement(InformationElementIdentifier.CONCATENATED_SM_8BIT_REF_NUM, IEConcatenatedSM(0x24, 0x03, 0x01)), iElem)
        
    def test_isConcatenatedSM_false(self):
        pduHex = '000000490000000500000000b9b7e456544d4f424900010131323533383836333438370001013134303436363533343130000000000000000000000d49206c7576206a757374696e21'
        pdu = self.getPDU(pduHex)
        self.assertFalse(SMStringEncoder().isConcatenatedSM(pdu))
        iElem = SMStringEncoder().getConcatenatedSMInfoElement(pdu)
        self.assertEquals(None, iElem)
    
            
if __name__ == '__main__':
    unittest.main()