# -*- coding: utf-8 -*-

###############################################################################
#
# SendEmail
# Sends an email using a specified email server.
#
# Python versions 2.6, 2.7, 3.x
#
# Copyright 2014, Temboo Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
#
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class SendEmail(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SendEmail Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(SendEmail, self).__init__(temboo_session, '/Library/Utilities/Email/SendEmail')


    def new_input_set(self):
        return SendEmailInputSet()

    def _make_result_set(self, result, path):
        return SendEmailResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SendEmailChoreographyExecution(session, exec_id, path)

class SendEmailInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SendEmail
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AttachmentName(self, value):
        """
        Set the value of the AttachmentName input for this Choreo. ((optional, string) The name of the file to attach to the email.)
        """
        super(SendEmailInputSet, self)._set_input('AttachmentName', value)
    def set_AttachmentURL(self, value):
        """
        Set the value of the AttachmentURL input for this Choreo. ((optional, string) URL of a hosted file that you wish to add as an attachment.  Use this instead of a normal Attachment.)
        """
        super(SendEmailInputSet, self)._set_input('AttachmentURL', value)
    def set_Attachment(self, value):
        """
        Set the value of the Attachment input for this Choreo. ((optional, string) The Base64 encoded contents of the file to attach to the email.  Use this instead of AttachmentURL.)
        """
        super(SendEmailInputSet, self)._set_input('Attachment', value)
    def set_BCC(self, value):
        """
        Set the value of the BCC input for this Choreo. ((optional, string) An email address to BCC on the email you're sending. Can be a comma separated list of email addresses.)
        """
        super(SendEmailInputSet, self)._set_input('BCC', value)
    def set_CC(self, value):
        """
        Set the value of the CC input for this Choreo. ((optional, string) An email address to CC on the email you're sending. Can be a comma separated list of email addresses.)
        """
        super(SendEmailInputSet, self)._set_input('CC', value)
    def set_FromAddress(self, value):
        """
        Set the value of the FromAddress input for this Choreo. ((conditional, string) The name and email address that the message is being sent from.)
        """
        super(SendEmailInputSet, self)._set_input('FromAddress', value)
    def set_MessageBody(self, value):
        """
        Set the value of the MessageBody input for this Choreo. ((required, string) The message body for the email.)
        """
        super(SendEmailInputSet, self)._set_input('MessageBody', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) The password for your email account.)
        """
        super(SendEmailInputSet, self)._set_input('Password', value)
    def set_Port(self, value):
        """
        Set the value of the Port input for this Choreo. ((required, integer) Specify the port number (i.e. 25 or 465).)
        """
        super(SendEmailInputSet, self)._set_input('Port', value)
    def set_Server(self, value):
        """
        Set the value of the Server input for this Choreo. ((required, string) The name or IP address of the email server.)
        """
        super(SendEmailInputSet, self)._set_input('Server', value)
    def set_Subject(self, value):
        """
        Set the value of the Subject input for this Choreo. ((required, string) The subject line of the email.)
        """
        super(SendEmailInputSet, self)._set_input('Subject', value)
    def set_ToAddress(self, value):
        """
        Set the value of the ToAddress input for this Choreo. ((required, string) The email address that you want to send an email to. Can be a comma separated list of email addresses.)
        """
        super(SendEmailInputSet, self)._set_input('ToAddress', value)
    def set_UseSSL(self, value):
        """
        Set the value of the UseSSL input for this Choreo. ((optional, boolean) Set to 1 to connect over SSL. Set to 0 for no SSL. Defaults to 1.)
        """
        super(SendEmailInputSet, self)._set_input('UseSSL', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) Your username for your email account.)
        """
        super(SendEmailInputSet, self)._set_input('Username', value)

class SendEmailResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SendEmail Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Success(self):
        """
        Retrieve the value for the "Success" output from this Choreo execution. ((boolean) Indicates the result of the SMTP operation. The value will be "true" for a successful request.)
        """
        return self._output.get('Success', None)

class SendEmailChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return SendEmailResultSet(response, path)
