# -*- coding: utf-8 -*-

###############################################################################
#
# GetCommittee
# Returns details for a committee by id.
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

class GetCommittee(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetCommittee Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetCommittee, self).__init__(temboo_session, '/Library/SunlightLabs/Congress/Committee/GetCommittee')


    def new_input_set(self):
        return GetCommitteeInputSet()

    def _make_result_set(self, result, path):
        return GetCommitteeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetCommitteeChoreographyExecution(session, exec_id, path)

class GetCommitteeInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetCommittee
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Sunlight Labs.)
        """
        super(GetCommitteeInputSet, self)._set_input('APIKey', value)
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, string) A comma-separated list of fields to include in the response.)
        """
        super(GetCommitteeInputSet, self)._set_input('Fields', value)
    def set_ID(self, value):
        """
        Set the value of the ID input for this Choreo. ((required, string) The id of a committee to return.)
        """
        super(GetCommitteeInputSet, self)._set_input('ID', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        super(GetCommitteeInputSet, self)._set_input('ResponseFormat', value)

class GetCommitteeResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetCommittee Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from the Sunlight Congress API.)
        """
        return self._output.get('Response', None)

class GetCommitteeChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetCommitteeResultSet(response, path)
