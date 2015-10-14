# -*- coding: utf-8 -*-

###############################################################################
#
# DownloadDocument
# Downloads a specified document in a user's Zoho Writer Account.
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

class DownloadDocument(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DownloadDocument Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(DownloadDocument, self).__init__(temboo_session, '/Library/Zoho/Writer/DownloadDocument')


    def new_input_set(self):
        return DownloadDocumentInputSet()

    def _make_result_set(self, result, path):
        return DownloadDocumentResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DownloadDocumentChoreographyExecution(session, exec_id, path)

class DownloadDocumentInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DownloadDocument
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Zoho)
        """
        super(DownloadDocumentInputSet, self)._set_input('APIKey', value)
    def set_DocumentId(self, value):
        """
        Set the value of the DocumentId input for this Choreo. ((required, integer) Specifies the unique document id to download.)
        """
        super(DownloadDocumentInputSet, self)._set_input('DocumentId', value)
    def set_DownloadFormat(self, value):
        """
        Set the value of the DownloadFormat input for this Choreo. ((required, string) Specifies the file format in which the documents need to be downloaded. Possible values for documents: doc, docx, pdf, html, sxw, odt, rtf.)
        """
        super(DownloadDocumentInputSet, self)._set_input('DownloadFormat', value)
    def set_LoginID(self, value):
        """
        Set the value of the LoginID input for this Choreo. ((required, string) Your Zoho username (or login id))
        """
        super(DownloadDocumentInputSet, self)._set_input('LoginID', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Zoho password)
        """
        super(DownloadDocumentInputSet, self)._set_input('Password', value)

class DownloadDocumentResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DownloadDocument Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Zoho. Corresponds to the DownloadFormat input.)
        """
        return self._output.get('Response', None)

class DownloadDocumentChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return DownloadDocumentResultSet(response, path)
