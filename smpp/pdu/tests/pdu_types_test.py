import unittest
from smpp.pdu.pdu_types import *

class EsmClassTest(unittest.TestCase):

    def test_equality_with_array_and_set(self):
        e1 = EsmClass(EsmClassMode.DATAGRAM, EsmClassType.DEFAULT, set([EsmClassGsmFeatures.SET_REPLY_PATH]))
        e2 = EsmClass(EsmClassMode.DATAGRAM, EsmClassType.DEFAULT, [EsmClassGsmFeatures.SET_REPLY_PATH])
        self.assertEquals(e1, e2)
    
    def test_equality_with_different_array_order(self):
        e1 = EsmClass(EsmClassMode.DATAGRAM, EsmClassType.DEFAULT, [EsmClassGsmFeatures.SET_REPLY_PATH, EsmClassGsmFeatures.UDHI_INDICATOR_SET])
        e2 = EsmClass(EsmClassMode.DATAGRAM, EsmClassType.DEFAULT, [EsmClassGsmFeatures.UDHI_INDICATOR_SET, EsmClassGsmFeatures.SET_REPLY_PATH])
        self.assertEquals(e1, e2)
        
    def test_equality_with_array_duplicates(self):
        e1 = EsmClass(EsmClassMode.DATAGRAM, EsmClassType.DEFAULT, [EsmClassGsmFeatures.SET_REPLY_PATH, EsmClassGsmFeatures.SET_REPLY_PATH])
        e2 = EsmClass(EsmClassMode.DATAGRAM, EsmClassType.DEFAULT, [EsmClassGsmFeatures.SET_REPLY_PATH])
        self.assertEquals(e1, e2)    

class RegisteredDeliveryTest(unittest.TestCase):

    def test_equality_with_array_and_set(self):
        r1 = RegisteredDelivery(RegisteredDeliveryReceipt.SMSC_DELIVERY_RECEIPT_REQUESTED, set([RegisteredDeliverySmeOriginatedAcks.SME_DELIVERY_ACK_REQUESTED]))
        r2 = RegisteredDelivery(RegisteredDeliveryReceipt.SMSC_DELIVERY_RECEIPT_REQUESTED, [RegisteredDeliverySmeOriginatedAcks.SME_DELIVERY_ACK_REQUESTED])
        self.assertEquals(r1, r2)
    
    def test_equality_with_different_array_order(self):
        r1 = RegisteredDelivery(RegisteredDeliveryReceipt.SMSC_DELIVERY_RECEIPT_REQUESTED, [RegisteredDeliverySmeOriginatedAcks.SME_MANUAL_ACK_REQUESTED, RegisteredDeliverySmeOriginatedAcks.SME_DELIVERY_ACK_REQUESTED])
        r2 = RegisteredDelivery(RegisteredDeliveryReceipt.SMSC_DELIVERY_RECEIPT_REQUESTED, [RegisteredDeliverySmeOriginatedAcks.SME_DELIVERY_ACK_REQUESTED, RegisteredDeliverySmeOriginatedAcks.SME_MANUAL_ACK_REQUESTED])
        self.assertEquals(r1, r2)
        
    def test_equality_with_array_duplicates(self):
        r1 = RegisteredDelivery(RegisteredDeliveryReceipt.SMSC_DELIVERY_RECEIPT_REQUESTED, [RegisteredDeliverySmeOriginatedAcks.SME_MANUAL_ACK_REQUESTED, RegisteredDeliverySmeOriginatedAcks.SME_MANUAL_ACK_REQUESTED])
        r2 = RegisteredDelivery(RegisteredDeliveryReceipt.SMSC_DELIVERY_RECEIPT_REQUESTED, [RegisteredDeliverySmeOriginatedAcks.SME_MANUAL_ACK_REQUESTED])
        self.assertEquals(r1, r2)    

        
if __name__ == '__main__':
    unittest.main()