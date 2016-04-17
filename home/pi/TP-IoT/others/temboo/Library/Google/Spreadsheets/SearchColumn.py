# -*- coding: utf-8 -*-

###############################################################################
#
# SearchColumn
# Searches a column for a specified value.
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

class SearchColumn(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SearchColumn Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(SearchColumn, self).__init__(temboo_session, '/Library/Google/Spreadsheets/SearchColumn')


    def new_input_set(self):
        return SearchColumnInputSet()

    def _make_result_set(self, result, path):
        return SearchColumnResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchColumnChoreographyExecution(session, exec_id, path)

class SearchColumnInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SearchColumn
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid Access Token retrieved during the OAuth process. This is required unless you provide the ClientID, ClientSecret, and RefreshToken to generate a new Access Token.)
        """
        super(SearchColumnInputSet, self)._set_input('AccessToken', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by Google. Required unless providing a valid AccessToken.)
        """
        super(SearchColumnInputSet, self)._set_input('ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The Client Secret provided by Google. Required unless providing a valid AccessToken.)
        """
        super(SearchColumnInputSet, self)._set_input('ClientSecret', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((optional, password) Deprecated (retained for backward compatibility only).)
        """
        super(SearchColumnInputSet, self)._set_input('Password', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((conditional, string) An OAuth Refresh Token used to generate a new Access Token when the original token is expired. Required unless providing a valid AccessToken.)
        """
        super(SearchColumnInputSet, self)._set_input('RefreshToken', value)
    def set_ReturnMatches(self, value):
        """
        Set the value of the ReturnMatches input for this Choreo. ((optional, boolean) Set to true to return all matches of the query. When set to true, an array of cell values that meet the query criteria is returned in the Results output. Defaults to true.)
        """
        super(SearchColumnInputSet, self)._set_input('ReturnMatches', value)
    def set_SearchColumn(self, value):
        """
        Set the value of the SearchColumn input for this Choreo. ((required, string) The name of the column to search. This should be the value in row 1 of the column you wish to search.)
        """
        super(SearchColumnInputSet, self)._set_input('SearchColumn', value)
    def set_SearchOperator(self, value):
        """
        Set the value of the SearchOperator input for this Choreo. ((required, string) The operator to use in the query. Allowed operators are: >, <, >=, >=, =, contains, and starts_with.)
        """
        super(SearchColumnInputSet, self)._set_input('SearchOperator', value)
    def set_SearchValue(self, value):
        """
        Set the value of the SearchValue input for this Choreo. ((required, any) The value to search for in the specified column.)
        """
        super(SearchColumnInputSet, self)._set_input('SearchValue', value)
    def set_SpreadsheetKey(self, value):
        """
        Set the value of the SpreadsheetKey input for this Choreo. ((conditional, string) The unique key of the spreadsheet to query. Required unless SpreadsheetName and WorksheetName are supplied.)
        """
        super(SearchColumnInputSet, self)._set_input('SpreadsheetKey', value)
    def set_SpreadsheetName(self, value):
        """
        Set the value of the SpreadsheetName input for this Choreo. ((optional, string) The name of the spreadsheet to query. This and WorksheetName can be used as an alternative to SpreadsheetKey and WorksheetId to lookup spreadsheet details by name.)
        """
        super(SearchColumnInputSet, self)._set_input('SpreadsheetName', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((optional, string) Deprecated (retained for backward compatibility only).)
        """
        super(SearchColumnInputSet, self)._set_input('Username', value)
    def set_WorksheetId(self, value):
        """
        Set the value of the WorksheetId input for this Choreo. ((conditional, string) The unique ID of the worksheet to query. Required unless SpreadsheetName and WorksheetName are supplied.)
        """
        super(SearchColumnInputSet, self)._set_input('WorksheetId', value)
    def set_WorksheetName(self, value):
        """
        Set the value of the WorksheetName input for this Choreo. ((optional, string) The name of the worksheet to query. This and SpreadsheetName can be used as an alternative to SpreadsheetKey and WorksheetId to lookup the spreadsheet details by name.)
        """
        super(SearchColumnInputSet, self)._set_input('WorksheetName', value)

class SearchColumnResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SearchColumn Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_MatchFound(self):
        """
        Retrieve the value for the "MatchFound" output from this Choreo execution. ((boolean) Whether or not a matched result was found.)
        """
        return self._output.get('MatchFound', None)
    def get_Count(self):
        """
        Retrieve the value for the "Count" output from this Choreo execution. ((integer) The count of matched results. This is only returned when ReturnMatches is set to true.)
        """
        return self._output.get('Count', None)
    def get_NewAccessToken(self):
        """
        Retrieve the value for the "NewAccessToken" output from this Choreo execution. ((string) Contains a new AccessToken when the RefreshToken is provided.)
        """
        return self._output.get('NewAccessToken', None)
    def get_Results(self):
        """
        Retrieve the value for the "Results" output from this Choreo execution. ((json) Contains an array of the matched cell values. This is only returned when ReturnMatches is set to true.)
        """
        return self._output.get('Results', None)

class SearchColumnChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return SearchColumnResultSet(response, path)
