# -*- coding: utf-8 -*-

###############################################################################
#
# Done
# Returns an array of users have done this tip.
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

class Done(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Done Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(Done, self).__init__(temboo_session, '/Library/Foursquare/Tips/Done')


    def new_input_set(self):
        return DoneInputSet()

    def _make_result_set(self, result, path):
        return DoneResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DoneChoreographyExecution(session, exec_id, path)

class DoneInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Done
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) Number of results to return, up to 200.)
        """
        super(DoneInputSet, self)._set_input('Limit', value)
    def set_OauthToken(self, value):
        """
        Set the value of the OauthToken input for this Choreo. ((required, string) The Foursquare API OAuth token string.)
        """
        super(DoneInputSet, self)._set_input('OauthToken', value)
    def set_Offset(self, value):
        """
        Set the value of the Offset input for this Choreo. ((optional, integer) Used to page through results.)
        """
        super(DoneInputSet, self)._set_input('Offset', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        super(DoneInputSet, self)._set_input('ResponseFormat', value)
    def set_TipID(self, value):
        """
        Set the value of the TipID input for this Choreo. ((required, string) The id of a tip to get users who have marked the tip as done.)
        """
        super(DoneInputSet, self)._set_input('TipID', value)

class DoneResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Done Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        return self._output.get('Response', None)

class DoneChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return DoneResultSet(response, path)
