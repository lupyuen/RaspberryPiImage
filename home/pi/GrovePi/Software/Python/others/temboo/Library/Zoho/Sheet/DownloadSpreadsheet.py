# -*- coding: utf-8 -*-

###############################################################################
#
# DownloadSpreadsheet
# Downloads a specified spreadsheet in a user's Zoho Sheet Account.
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

class DownloadSpreadsheet(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DownloadSpreadsheet Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(DownloadSpreadsheet, self).__init__(temboo_session, '/Library/Zoho/Sheet/DownloadSpreadsheet')


    def new_input_set(self):
        return DownloadSpreadsheetInputSet()

    def _make_result_set(self, result, path):
        return DownloadSpreadsheetResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DownloadSpreadsheetChoreographyExecution(session, exec_id, path)

class DownloadSpreadsheetInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DownloadSpreadsheet
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Zoho)
        """
        super(DownloadSpreadsheetInputSet, self)._set_input('APIKey', value)
    def set_BookId(self, value):
        """
        Set the value of the BookId input for this Choreo. ((required, integer) Specifies the unique spreadsheet id to download.)
        """
        super(DownloadSpreadsheetInputSet, self)._set_input('BookId', value)
    def set_DownloadFormat(self, value):
        """
        Set the value of the DownloadFormat input for this Choreo. ((required, string) Specifies the file format in which the documents need to be downloaded. Possible values for documents: xls, xlsx, ods, sxc, pdf, html, csv, tsv.)
        """
        super(DownloadSpreadsheetInputSet, self)._set_input('DownloadFormat', value)
    def set_LoginID(self, value):
        """
        Set the value of the LoginID input for this Choreo. ((required, string) Your Zoho username (or login id))
        """
        super(DownloadSpreadsheetInputSet, self)._set_input('LoginID', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Zoho password)
        """
        super(DownloadSpreadsheetInputSet, self)._set_input('Password', value)

class DownloadSpreadsheetResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DownloadSpreadsheet Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Zoho. Corresponds to the DownloadFormat input.)
        """
        return self._output.get('Response', None)

class DownloadSpreadsheetChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return DownloadSpreadsheetResultSet(response, path)
