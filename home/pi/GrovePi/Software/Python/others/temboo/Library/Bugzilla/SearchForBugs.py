# -*- coding: utf-8 -*-

###############################################################################
#
# SearchForBugs
# Searches bugs by Mozilla product name.
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

class SearchForBugs(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SearchForBugs Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(SearchForBugs, self).__init__(temboo_session, '/Library/Bugzilla/SearchForBugs')


    def new_input_set(self):
        return SearchForBugsInputSet()

    def _make_result_set(self, result, path):
        return SearchForBugsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchForBugsChoreographyExecution(session, exec_id, path)

class SearchForBugsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SearchForBugs
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_BugChangeDate(self, value):
        """
        Set the value of the BugChangeDate input for this Choreo. ((optional, string) Retrieve bugs that were changed within a certain date range. For example: 25d will return all bugs changed from 25 days ago untill today.  Or: 3h, to return all bugs entered with 3 hours.)
        """
        super(SearchForBugsInputSet, self)._set_input('BugChangeDate', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((optional, password) Your Bugzilla password.)
        """
        super(SearchForBugsInputSet, self)._set_input('Password', value)
    def set_Priority(self, value):
        """
        Set the value of the Priority input for this Choreo. ((optional, integer) Filter results by priority: For example: enter P1, to get Priority 1 bugs assoicated with a Product.)
        """
        super(SearchForBugsInputSet, self)._set_input('Priority', value)
    def set_Product(self, value):
        """
        Set the value of the Product input for this Choreo. ((required, string) Enter the Mozilla product for which bugs will be retrieved. For example: Bugzilla)
        """
        super(SearchForBugsInputSet, self)._set_input('Product', value)
    def set_Server(self, value):
        """
        Set the value of the Server input for this Choreo. ((optional, string) The base URL for the Bugzilla server to access. Defaults to https://api-dev.bugzilla.mozilla.org/latest. To access the test server, set to https://api-dev.bugzilla.mozilla.org/test/latest.)
        """
        super(SearchForBugsInputSet, self)._set_input('Server', value)
    def set_Severity(self, value):
        """
        Set the value of the Severity input for this Choreo. ((optional, string) Filter results by severity. For example: blocker)
        """
        super(SearchForBugsInputSet, self)._set_input('Severity', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) Your Bugzilla username.)
        """
        super(SearchForBugsInputSet, self)._set_input('Username', value)

class SearchForBugsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SearchForBugs Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Bugzilla.)
        """
        return self._output.get('Response', None)

class SearchForBugsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return SearchForBugsResultSet(response, path)
