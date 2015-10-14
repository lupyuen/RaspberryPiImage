# -*- coding: utf-8 -*-

###############################################################################
#
# UploadAttachment
# Uploads a file to be used as an attachment to a ticket.
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

class UploadAttachment(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UploadAttachment Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(UploadAttachment, self).__init__(temboo_session, '/Library/Zendesk/Attachments/UploadAttachment')


    def new_input_set(self):
        return UploadAttachmentInputSet()

    def _make_result_set(self, result, path):
        return UploadAttachmentResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UploadAttachmentChoreographyExecution(session, exec_id, path)

class UploadAttachmentInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UploadAttachment
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Email(self, value):
        """
        Set the value of the Email input for this Choreo. ((required, string) The email address you use to login to your Zendesk account.)
        """
        super(UploadAttachmentInputSet, self)._set_input('Email', value)
    def set_ExistingToken(self, value):
        """
        Set the value of the ExistingToken input for this Choreo. ((optional, string) Allows you to pass in an existing token when uploading multiple attachments to associate with a ticket.)
        """
        super(UploadAttachmentInputSet, self)._set_input('ExistingToken', value)
    def set_FileContents(self, value):
        """
        Set the value of the FileContents input for this Choreo. ((required, string) The Base64 encoded file contents of the attachment you want to upload.)
        """
        super(UploadAttachmentInputSet, self)._set_input('FileContents', value)
    def set_FileName(self, value):
        """
        Set the value of the FileName input for this Choreo. ((required, string) The file name of the attachment.)
        """
        super(UploadAttachmentInputSet, self)._set_input('FileName', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Zendesk password.)
        """
        super(UploadAttachmentInputSet, self)._set_input('Password', value)
    def set_Server(self, value):
        """
        Set the value of the Server input for this Choreo. ((required, string) Your Zendesk domain and subdomain (e.g., temboocare.zendesk.com).)
        """
        super(UploadAttachmentInputSet, self)._set_input('Server', value)


class UploadAttachmentResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UploadAttachment Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Zendesk.)
        """
        return self._output.get('Response', None)
    def get_Token(self):
        """
        Retrieve the value for the "Token" output from this Choreo execution. ((string) The token returned from Zendesk for the upload. This can be passed to the ExistingToken input when associating  multiple attachments to the same upload token.)
        """
        return self._output.get('Token', None)

class UploadAttachmentChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UploadAttachmentResultSet(response, path)
