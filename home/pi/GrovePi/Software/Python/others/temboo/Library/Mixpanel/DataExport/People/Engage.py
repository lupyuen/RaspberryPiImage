# -*- coding: utf-8 -*-

###############################################################################
#
# Engage
# Queries Mixpanel for data about people.
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

class Engage(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Engage Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(Engage, self).__init__(temboo_session, '/Library/Mixpanel/DataExport/People/Engage')


    def new_input_set(self):
        return EngageInputSet()

    def _make_result_set(self, result, path):
        return EngageResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return EngageChoreographyExecution(session, exec_id, path)

class EngageInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Engage
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided my Mixpanel. You can find your Mixpanel API Key in the project settings dialog in the Mixpanel app.)
        """
        super(EngageInputSet, self)._set_input('APIKey', value)
    def set_APISecret(self, value):
        """
        Set the value of the APISecret input for this Choreo. ((required, string) The API Secret provided by Mixpanel. You can find your Mixpanel API Secret in the project settings dialog in the Mixpanel app.)
        """
        super(EngageInputSet, self)._set_input('APISecret', value)
    def set_Expire(self, value):
        """
        Set the value of the Expire input for this Choreo. ((optional, integer) The amount of minutes past NOW() before the request will expire. Defaults to 1.)
        """
        super(EngageInputSet, self)._set_input('Expire', value)
    def set_Page(self, value):
        """
        Set the value of the Page input for this Choreo. ((optional, integer) Which page of the results to retrieve. Pages start at zero. If the "page" parameter is provided, the session_id parameter must also be provided.)
        """
        super(EngageInputSet, self)._set_input('Page', value)
    def set_SessionID(self, value):
        """
        Set the value of the SessionID input for this Choreo. ((optional, string) A string id provided in the results of a previous query. Using a session_id speeds up api response, and allows paging through results.)
        """
        super(EngageInputSet, self)._set_input('SessionID', value)
    def set_Where(self, value):
        """
        Set the value of the Where input for this Choreo. ((optional, string) An expression to filter people by (e.g., properties["time"]). See Choreo description for examples.)
        """
        super(EngageInputSet, self)._set_input('Where', value)

class EngageResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Engage Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Mixpanel.)
        """
        return self._output.get('Response', None)

class EngageChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return EngageResultSet(response, path)
