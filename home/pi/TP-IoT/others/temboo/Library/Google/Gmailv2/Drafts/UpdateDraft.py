# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateDraft
# Updates the content of an existing draft.
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

class UpdateDraft(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateDraft Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(UpdateDraft, self).__init__(temboo_session, '/Library/Google/Gmailv2/Drafts/UpdateDraft')


    def new_input_set(self):
        return UpdateDraftInputSet()

    def _make_result_set(self, result, path):
        return UpdateDraftResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateDraftChoreographyExecution(session, exec_id, path)

class UpdateDraftInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateDraft
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid Access Token retrieved during the OAuth2 process. This is required unless you provide the ClientID, ClientSecret, and RefreshToken to generate a new Access Token.)
        """
        super(UpdateDraftInputSet, self)._set_input('AccessToken', value)
    def set_AttachmentContentType(self, value):
        """
        Set the value of the AttachmentContentType input for this Choreo. ((optional, string) The Content-Type of the attachment. This is required when providing AttachmentFileContent (e.g., image/jpeg, text/plain, etc).)
        """
        super(UpdateDraftInputSet, self)._set_input('AttachmentContentType', value)
    def set_AttachmentFileContent(self, value):
        """
        Set the value of the AttachmentFileContent input for this Choreo. ((optional, string) The Base64 encoded file content for the attachment. You must specify the AttachmentFileContentType when including an attachment.)
        """
        super(UpdateDraftInputSet, self)._set_input('AttachmentFileContent', value)
    def set_AttachmentFileName(self, value):
        """
        Set the value of the AttachmentFileName input for this Choreo. ((optional, string) The file name of the attachment.)
        """
        super(UpdateDraftInputSet, self)._set_input('AttachmentFileName', value)
    def set_BCC(self, value):
        """
        Set the value of the BCC input for this Choreo. ((optional, string) The address and name (optional) that should be bcc'd e.g., Dan <dan@temboo.com>.)
        """
        super(UpdateDraftInputSet, self)._set_input('BCC', value)
    def set_CC(self, value):
        """
        Set the value of the CC input for this Choreo. ((optional, string) The address and name (optional) that should be cc'd e.g., Dan <dan@temboo.com>.)
        """
        super(UpdateDraftInputSet, self)._set_input('CC', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by Google. Required unless providing a valid AccessToken.)
        """
        super(UpdateDraftInputSet, self)._set_input('ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The Client Secret provided by Google. Required unless providing a valid AccessToken.)
        """
        super(UpdateDraftInputSet, self)._set_input('ClientSecret', value)
    def set_DraftID(self, value):
        """
        Set the value of the DraftID input for this Choreo. ((required, string) The ID of the draft to update.)
        """
        super(UpdateDraftInputSet, self)._set_input('DraftID', value)
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, string) Used to specify fields to include in a partial response. This can be used to reduce the amount of data returned. See Choreo notes for syntax rules.)
        """
        super(UpdateDraftInputSet, self)._set_input('Fields', value)
    def set_From(self, value):
        """
        Set the value of the From input for this Choreo. ((conditional, string) The address and name (optional) that the email is being sent from e.g., Dan <dan@temboo.com>.)
        """
        super(UpdateDraftInputSet, self)._set_input('From', value)
    def set_MessageBodyContentType(self, value):
        """
        Set the value of the MessageBodyContentType input for this Choreo. ((optional, string) The Content-Type of the message body. Defaults to "text/plain; charset=UTF-8".)
        """
        super(UpdateDraftInputSet, self)._set_input('MessageBodyContentType', value)
    def set_MessageBody(self, value):
        """
        Set the value of the MessageBody input for this Choreo. ((conditional, string) The text for the message body of the email.)
        """
        super(UpdateDraftInputSet, self)._set_input('MessageBody', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((conditional, string) An OAuth Refresh Token used to generate a new Access Token when the original token is expired. Required unless providing a valid AccessToken.)
        """
        super(UpdateDraftInputSet, self)._set_input('RefreshToken', value)
    def set_ReplyTo(self, value):
        """
        Set the value of the ReplyTo input for this Choreo. ((optional, string) An email address to set as the Reply-To address.)
        """
        super(UpdateDraftInputSet, self)._set_input('ReplyTo', value)
    def set_Subject(self, value):
        """
        Set the value of the Subject input for this Choreo. ((conditional, string) The email subject.)
        """
        super(UpdateDraftInputSet, self)._set_input('Subject', value)
    def set_ThreadID(self, value):
        """
        Set the value of the ThreadID input for this Choreo. ((optional, string) The ID of the thread the message belongs to.)
        """
        super(UpdateDraftInputSet, self)._set_input('ThreadID', value)
    def set_To(self, value):
        """
        Set the value of the To input for this Choreo. ((conditional, string) The address and name (optional) that the email is being sent to e.g., Dan <dan@temboo.com>.)
        """
        super(UpdateDraftInputSet, self)._set_input('To', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((optional, string) The ID of the acting user. Defaults to "me" indicating the user associated with the Access Token or Refresh Token provided.)
        """
        super(UpdateDraftInputSet, self)._set_input('UserID', value)

class UpdateDraftResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateDraft Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Google.)
        """
        return self._output.get('Response', None)
    def get_NewAccessToken(self):
        """
        Retrieve the value for the "NewAccessToken" output from this Choreo execution. ((string) Contains a new AccessToken when the RefreshToken is provided.)
        """
        return self._output.get('NewAccessToken', None)

class UpdateDraftChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UpdateDraftResultSet(response, path)
