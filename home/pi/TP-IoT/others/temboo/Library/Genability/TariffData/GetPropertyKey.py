# -*- coding: utf-8 -*-

###############################################################################
#
# GetPropertyKey
# Returns an individual Property Key using a given key name.
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

class GetPropertyKey(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetPropertyKey Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetPropertyKey, self).__init__(temboo_session, '/Library/Genability/TariffData/GetPropertyKey')


    def new_input_set(self):
        return GetPropertyKeyInputSet()

    def _make_result_set(self, result, path):
        return GetPropertyKeyResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetPropertyKeyChoreographyExecution(session, exec_id, path)

class GetPropertyKeyInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetPropertyKey
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AppID(self, value):
        """
        Set the value of the AppID input for this Choreo. ((conditional, string) The App ID provided by Genability.)
        """
        super(GetPropertyKeyInputSet, self)._set_input('AppID', value)
    def set_AppKey(self, value):
        """
        Set the value of the AppKey input for this Choreo. ((required, string) The App Key provided by Genability.)
        """
        super(GetPropertyKeyInputSet, self)._set_input('AppKey', value)
    def set_KeyName(self, value):
        """
        Set the value of the KeyName input for this Choreo. ((required, string) The key name for the property key you want to return.)
        """
        super(GetPropertyKeyInputSet, self)._set_input('KeyName', value)

class GetPropertyKeyResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetPropertyKey Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Genability.)
        """
        return self._output.get('Response', None)

class GetPropertyKeyChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetPropertyKeyResultSet(response, path)
