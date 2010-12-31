from smpp.pdu import pdu_types
from smpp.pdu.error import PDUCorruptError

class IEncoder(object):

    def encode(self, value):
        """Takes an object representing the type and returns a byte string"""
        raise NotImplementedError()

    def decode(self, file):
        """Takes file stream in and returns an object representing the type"""
        raise NotImplementedError()
        
    def read(self, file, size):
        bytesRead = file.read(size)
        length = len(bytesRead)
        if length == 0:
            raise PDUCorruptError("Unexpected EOF", pdu_types.CommandStatus.ESME_RINVMSGLEN)
        if length != size:
            raise PDUCorruptError("Length mismatch. Expecting %d bytes. Read %d" % (size, length), pdu_types.CommandStatus.ESME_RINVMSGLEN)
        return bytesRead