# -*- coding: utf-8 -*-

###############################################################################
#
# RecentCheckins
# Returns a list of recent friends' check-ins.
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

class RecentCheckins(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RecentCheckins Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(RecentCheckins, self).__init__(temboo_session, '/Library/Foursquare/Checkins/RecentCheckins')


    def new_input_set(self):
        return RecentCheckinsInputSet()

    def _make_result_set(self, result, path):
        return RecentCheckinsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RecentCheckinsChoreographyExecution(session, exec_id, path)

class RecentCheckinsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RecentCheckins
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AfterTimeStamp(self, value):
        """
        Set the value of the AfterTimeStamp input for this Choreo. ((optional, integer) Seconds after which to look for check-ins, e.g. for looking for new check-ins since the last fetch.)
        """
        super(RecentCheckinsInputSet, self)._set_input('AfterTimeStamp', value)
    def set_Latitude(self, value):
        """
        Set the value of the Latitude input for this Choreo. ((optional, decimal) The latitude point of the user's location.)
        """
        super(RecentCheckinsInputSet, self)._set_input('Latitude', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) Number of results to return, up to 100.)
        """
        super(RecentCheckinsInputSet, self)._set_input('Limit', value)
    def set_Longitude(self, value):
        """
        Set the value of the Longitude input for this Choreo. ((optional, decimal) The longitude point of the user's location.)
        """
        super(RecentCheckinsInputSet, self)._set_input('Longitude', value)
    def set_OauthToken(self, value):
        """
        Set the value of the OauthToken input for this Choreo. ((required, string) The FourSquare API Oauth token string.)
        """
        super(RecentCheckinsInputSet, self)._set_input('OauthToken', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        super(RecentCheckinsInputSet, self)._set_input('ResponseFormat', value)

class RecentCheckinsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RecentCheckins Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        return self._output.get('Response', None)

class RecentCheckinsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return RecentCheckinsResultSet(response, path)
