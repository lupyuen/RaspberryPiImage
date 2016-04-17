# -*- coding: utf-8 -*-

###############################################################################
#
# TopEvents
# Gets the top events for today, with their counts and the normalized percent change from yesterday.
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

class TopEvents(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the TopEvents Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(TopEvents, self).__init__(temboo_session, '/Library/Mixpanel/DataExport/Events/TopEvents')


    def new_input_set(self):
        return TopEventsInputSet()

    def _make_result_set(self, result, path):
        return TopEventsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return TopEventsChoreographyExecution(session, exec_id, path)

class TopEventsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the TopEvents
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided my Mixpanel. You can find your Mixpanel API Key in the project settings dialog in the Mixpanel app.)
        """
        super(TopEventsInputSet, self)._set_input('APIKey', value)
    def set_APISecret(self, value):
        """
        Set the value of the APISecret input for this Choreo. ((required, string) The API Secret provided by Mixpanel. You can find your Mixpanel API Secret in the project settings dialog in the Mixpanel app.)
        """
        super(TopEventsInputSet, self)._set_input('APISecret', value)
    def set_Expire(self, value):
        """
        Set the value of the Expire input for this Choreo. ((optional, integer) The amount of minutes past NOW() before the request will expire. Defaults to 1.)
        """
        super(TopEventsInputSet, self)._set_input('Expire', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) The maximum number of events to return. Defaults to 100 (the max the limit).)
        """
        super(TopEventsInputSet, self)._set_input('Limit', value)
    def set_Type(self, value):
        """
        Set the value of the Type input for this Choreo. ((required, string) The analysis type you would like to get data for. Valid values are: general, unique, or average)
        """
        super(TopEventsInputSet, self)._set_input('Type', value)

class TopEventsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the TopEvents Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Mixpanel.)
        """
        return self._output.get('Response', None)

class TopEventsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return TopEventsResultSet(response, path)
