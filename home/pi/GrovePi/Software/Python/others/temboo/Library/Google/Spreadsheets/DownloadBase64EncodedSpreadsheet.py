# -*- coding: utf-8 -*-

###############################################################################
#
# DownloadBase64EncodedSpreadsheet
# Downloads a document with the title you specify, and returns the content as Base64 encoded data.
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

class DownloadBase64EncodedSpreadsheet(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DownloadBase64EncodedSpreadsheet Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(DownloadBase64EncodedSpreadsheet, self).__init__(temboo_session, '/Library/Google/Spreadsheets/DownloadBase64EncodedSpreadsheet')


    def new_input_set(self):
        return DownloadBase64EncodedSpreadsheetInputSet()

    def _make_result_set(self, result, path):
        return DownloadBase64EncodedSpreadsheetResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DownloadBase64EncodedSpreadsheetChoreographyExecution(session, exec_id, path)

class DownloadBase64EncodedSpreadsheetInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DownloadBase64EncodedSpreadsheet
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid Access Token retrieved during the OAuth process. This is required unless you provide the ClientID, ClientSecret, and RefreshToken to generate a new Access Token.)
        """
        super(DownloadBase64EncodedSpreadsheetInputSet, self)._set_input('AccessToken', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by Google. Required unless providing a valid AccessToken.)
        """
        super(DownloadBase64EncodedSpreadsheetInputSet, self)._set_input('ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The Client Secret provided by Google. Required unless providing a valid AccessToken.)
        """
        super(DownloadBase64EncodedSpreadsheetInputSet, self)._set_input('ClientSecret', value)
    def set_Format(self, value):
        """
        Set the value of the Format input for this Choreo. ((conditional, string) The format you want to export the spreadsheet to, such as "csv" or "pdf".)
        """
        super(DownloadBase64EncodedSpreadsheetInputSet, self)._set_input('Format', value)
    def set_Link(self, value):
        """
        Set the value of the Link input for this Choreo. ((optional, string) A file's exportLink. Required unless specifying the Title. See Choreo notes for more details about where this property can be found.)
        """
        super(DownloadBase64EncodedSpreadsheetInputSet, self)._set_input('Link', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((optional, password) Deprecated (retained for backward compatibility only).)
        """
        super(DownloadBase64EncodedSpreadsheetInputSet, self)._set_input('Password', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((conditional, string) An OAuth Refresh Token used to generate a new Access Token when the original token is expired. Required unless providing a valid AccessToken.)
        """
        super(DownloadBase64EncodedSpreadsheetInputSet, self)._set_input('RefreshToken', value)
    def set_Title(self, value):
        """
        Set the value of the Title input for this Choreo. ((conditional, string) The title of the document to download. Required if the source Link is not specifed.)
        """
        super(DownloadBase64EncodedSpreadsheetInputSet, self)._set_input('Title', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((optional, string) Deprecated (retained for backward compatibility only).)
        """
        super(DownloadBase64EncodedSpreadsheetInputSet, self)._set_input('Username', value)

class DownloadBase64EncodedSpreadsheetResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DownloadBase64EncodedSpreadsheet Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_FileContents(self):
        """
        Retrieve the value for the "FileContents" output from this Choreo execution. ((string) The Base64 encoded file content of the downloaded file.)
        """
        return self._output.get('FileContents', None)
    def get_NewAccessToken(self):
        """
        Retrieve the value for the "NewAccessToken" output from this Choreo execution. ((string) Contains a new AccessToken when the RefreshToken is provided.)
        """
        return self._output.get('NewAccessToken', None)

class DownloadBase64EncodedSpreadsheetChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return DownloadBase64EncodedSpreadsheetResultSet(response, path)
