# -*- coding: utf-8 -*-

###############################################################################
#
# ListYourIssues
# Lists all issues associated with the provided access token.
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

class ListYourIssues(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListYourIssues Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ListYourIssues, self).__init__(temboo_session, '/Library/GitHub/IssuesAPI/Issues/ListYourIssues')


    def new_input_set(self):
        return ListYourIssuesInputSet()

    def _make_result_set(self, result, path):
        return ListYourIssuesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListYourIssuesChoreographyExecution(session, exec_id, path)

class ListYourIssuesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListYourIssues
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        super(ListYourIssuesInputSet, self)._set_input('AccessToken', value)
    def set_Direction(self, value):
        """
        Set the value of the Direction input for this Choreo. ((optional, string) The direction of the sort order. Valid values are: asc or desc (the default).)
        """
        super(ListYourIssuesInputSet, self)._set_input('Direction', value)
    def set_Filter(self, value):
        """
        Set the value of the Filter input for this Choreo. ((optional, string) Filters issues using one of the following strings: assigned (the default), created, mentioned, subscribed.)
        """
        super(ListYourIssuesInputSet, self)._set_input('Filter', value)
    def set_Labels(self, value):
        """
        Set the value of the Labels input for this Choreo. ((optional, string) A comma separated list of label names (i.e. bug, ui, etc).)
        """
        super(ListYourIssuesInputSet, self)._set_input('Labels', value)
    def set_Page(self, value):
        """
        Set the value of the Page input for this Choreo. ((optional, integer) Indicates the page index that you want to retrieve. This is used to page through many results. Defaults to 1.)
        """
        super(ListYourIssuesInputSet, self)._set_input('Page', value)
    def set_PerPage(self, value):
        """
        Set the value of the PerPage input for this Choreo. ((optional, integer) The number of results to return per page.)
        """
        super(ListYourIssuesInputSet, self)._set_input('PerPage', value)
    def set_Since(self, value):
        """
        Set the value of the Since input for this Choreo. ((optional, date) A timestamp in ISO 8601 format (YYYY-MM-DDTHH:MM:SSZ). Returns issues since this date.)
        """
        super(ListYourIssuesInputSet, self)._set_input('Since', value)
    def set_Sort(self, value):
        """
        Set the value of the Sort input for this Choreo. ((optional, string) Indicates how the issues will be sorted in the response. Valid sort options are: created (the default), updated, comments.)
        """
        super(ListYourIssuesInputSet, self)._set_input('Sort', value)
    def set_State(self, value):
        """
        Set the value of the State input for this Choreo. ((optional, string) Returns issues with a particular state: open (the default) or closed.)
        """
        super(ListYourIssuesInputSet, self)._set_input('State', value)

class ListYourIssuesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListYourIssues Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from GitHub.)
        """
        return self._output.get('Response', None)
    def get_FirstPage(self):
        """
        Retrieve the value for the "FirstPage" output from this Choreo execution. ((integer) The index for the first page of results.)
        """
        return self._output.get('FirstPage', None)
    def get_LastPage(self):
        """
        Retrieve the value for the "LastPage" output from this Choreo execution. ((integer) The index for the last page of results.)
        """
        return self._output.get('LastPage', None)
    def get_Limit(self):
        """
        Retrieve the value for the "Limit" output from this Choreo execution. ((integer) The available rate limit for your account. This is returned in the GitHub response header.)
        """
        return self._output.get('Limit', None)
    def get_NextPage(self):
        """
        Retrieve the value for the "NextPage" output from this Choreo execution. ((integer) The index for the next page of results.)
        """
        return self._output.get('NextPage', None)
    def get_PreviousPage(self):
        """
        Retrieve the value for the "PreviousPage" output from this Choreo execution. ((integer) The index for the previous page of results.)
        """
        return self._output.get('PreviousPage', None)
    def get_Remaining(self):
        """
        Retrieve the value for the "Remaining" output from this Choreo execution. ((integer) The remaining number of API requests available to you. This is returned in the GitHub response header.)
        """
        return self._output.get('Remaining', None)

class ListYourIssuesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ListYourIssuesResultSet(response, path)
