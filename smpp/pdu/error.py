from smpp.pdu import constants

class SMPPError(Exception):
    """Base class for SMPP errors
    """

class SMPPClientError(SMPPError):
    """Raised for client-side errors
    """

class SMPPClientConnectionCorruptedError(SMPPClientError):
    """Raised when operations are attempted after the client has received corrupt data
    """

class SMPPClientSessionStateError(SMPPClientError):
    """Raised when illegal operations are attempted for the client's session state
    """
    
class SMPPTransactionError(SMPPError):
    """Raised for transaction errors
    """
    def __init__(self, response, request=None):
        self.response = response
        self.request = request
        SMPPError.__init__(self, self.getErrorStr())
        
    def getErrorStr(self):
        errCodeName = str(self.response.status)
        errCodeVal = constants.command_status_name_map[errCodeName]
        errCodeDesc = constants.command_status_value_map[errCodeVal]
        return '%s (%s)' % (errCodeName, errCodeDesc)

class SMPPGenericNackTransactionError(SMPPTransactionError):
    """Raised for transaction errors that return generic_nack
    """

class SMPPRequestTimoutError(SMPPError):
    """Raised for timeout waiting waiting for response
    """

class SMPPSessionInitTimoutError(SMPPRequestTimoutError):
    """Raised for timeout waiting waiting for response
    """

class SMPPProtocolError(SMPPError):
    """Raised for SMPP protocol errors
    """
    def __init__(self, errStr, commandStatus):
        self.status = commandStatus
        SMPPError.__init__(self, "%s: %s" % (self.getStatusDescription(), errStr))

    def getStatusDescription(self):
        intVal = constants.command_status_name_map[str(self.status)]
        return constants.command_status_value_map[intVal]['description']

class SessionStateError(SMPPProtocolError):
    """Raise when illegal operations are received for the given session state
    """

class PDUParseError(SMPPProtocolError):
    """Parent class for PDU parsing errors
    """

class PDUCorruptError(PDUParseError):
    """Raised when a complete PDU cannot be read from the network
    """
