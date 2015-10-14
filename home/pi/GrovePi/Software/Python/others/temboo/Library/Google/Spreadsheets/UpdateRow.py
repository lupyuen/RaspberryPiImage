# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateRow
# Allows you to update a row by providing the row number and comma-separated data.
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

class UpdateRow(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateRow Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(UpdateRow, self).__init__(temboo_session, '/Library/Google/Spreadsheets/UpdateRow')


    def new_input_set(self):
        return UpdateRowInputSet()

    def _make_result_set(self, result, path):
        return UpdateRowResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateRowChoreographyExecution(session, exec_id, path)

class UpdateRowInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateRow
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_RowData(self, value):
        """
        Set the value of the RowData input for this Choreo. ((required, string) The updated row data formatted as a comma-separated string.)
        """
        super(UpdateRowInputSet, self)._set_input('RowData', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid Access Token retrieved during the OAuth process. This is required unless you provide the ClientID, ClientSecret, and RefreshToken to generate a new Access Token.)
        """
        super(UpdateRowInputSet, self)._set_input('AccessToken', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by Google. Required unless providing a valid AccessToken.)
        """
        super(UpdateRowInputSet, self)._set_input('ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The Client Secret provided by Google. Required unless providing a valid AccessToken.)
        """
        super(UpdateRowInputSet, self)._set_input('ClientSecret', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((optional, password) Deprecated (retained for backward compatibility only).)
        """
        super(UpdateRowInputSet, self)._set_input('Password', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((conditional, string) An OAuth Refresh Token used to generate a new Access Token when the original token is expired. Required unless providing a valid AccessToken.)
        """
        super(UpdateRowInputSet, self)._set_input('RefreshToken', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: xml (the default) and json.)
        """
        super(UpdateRowInputSet, self)._set_input('ResponseFormat', value)
    def set_Row(self, value):
        """
        Set the value of the Row input for this Choreo. ((conditional, integer) The number of the row to update. Note that row 1 (the column header row) can not be updated. Also, the row that is being updated must exist already. To add new rows, see AppendRow.)
        """
        super(UpdateRowInputSet, self)._set_input('Row', value)
    def set_SpreadsheetKey(self, value):
        """
        Set the value of the SpreadsheetKey input for this Choreo. ((required, string) The unique key of the spreadsheet associated with the row you want to update. This can be found in the URL when viewing the spreadsheet. Required unless SpreadsheetName and WorksheetName are supplied.)
        """
        super(UpdateRowInputSet, self)._set_input('SpreadsheetKey', value)
    def set_SpreadsheetName(self, value):
        """
        Set the value of the SpreadsheetName input for this Choreo. ((optional, string) The name of the spreadsheet to update. This and WorksheetName can be used as an alternative to SpreadsheetKey and WorksheetId to lookup spreadsheet details by name.)
        """
        super(UpdateRowInputSet, self)._set_input('SpreadsheetName', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((optional, string) Deprecated (retained for backward compatibility only).)
        """
        super(UpdateRowInputSet, self)._set_input('Username', value)
    def set_WorksheetId(self, value):
        """
        Set the value of the WorksheetId input for this Choreo. ((required, string) The unique ID of the worksheet that you want to udpate. Typically, Sheet1 has the id of "od6". Required unless SpreadsheetName and WorksheetName are supplied.)
        """
        super(UpdateRowInputSet, self)._set_input('WorksheetId', value)
    def set_WorksheetName(self, value):
        """
        Set the value of the WorksheetName input for this Choreo. ((optional, string) The name of the worksheet to update. This and SpreadsheetName can be used as an alternative to SpreadsheetKey and WorksheetId to lookup spreadsheet details by name.)
        """
        super(UpdateRowInputSet, self)._set_input('WorksheetName', value)

class UpdateRowResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateRow Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Google.)
        """
        return self._output.get('Response', None)
    def get_NewAccessToken(self):
        """
        Retrieve the value for the "NewAccessToken" output from this Choreo execution. ((string) Contains a new AccessToken when the RefreshToken is provided.)
        """
        return self._output.get('NewAccessToken', None)

class UpdateRowChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UpdateRowResultSet(response, path)
