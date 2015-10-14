# -*- coding: utf-8 -*-

###############################################################################
#
# IDLookup
# Looks up the entity ID based on an ID from a different data set. Currently Influence Explorer provides a mapping from the ID schemes used by Center for Reponsive Politics (CRP) and the National Institute for Money in State Politics (NIMSP).
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

class IDLookup(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the IDLookup Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(IDLookup, self).__init__(temboo_session, '/Library/InfluenceExplorer/IDLookup')


    def new_input_set(self):
        return IDLookupInputSet()

    def _make_result_set(self, result, path):
        return IDLookupResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return IDLookupChoreographyExecution(session, exec_id, path)

class IDLookupInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the IDLookup
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API key provided by Sunlight Data Services.)
        """
        super(IDLookupInputSet, self)._set_input('APIKey', value)
    def set_ID(self, value):
        """
        Set the value of the ID input for this Choreo. ((required, string) The ID of the Entity in the given namespace.)
        """
        super(IDLookupInputSet, self)._set_input('ID', value)
    def set_Namespace(self, value):
        """
        Set the value of the Namespace input for this Choreo. ((required, string) The dataset and data type of the ID. Accepted values are: urn:crp:individual, urn:crp:organization, urn:crp:recipient, urn:nimsp:organization, urn:nimsp:recipient. See documentation for more details.)
        """
        super(IDLookupInputSet, self)._set_input('Namespace', value)

class IDLookupResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the IDLookup Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Influence Explorer.)
        """
        return self._output.get('Response', None)

class IDLookupChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return IDLookupResultSet(response, path)
