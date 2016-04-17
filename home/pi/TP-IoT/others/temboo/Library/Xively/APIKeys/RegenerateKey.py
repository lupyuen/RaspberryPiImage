# -*- coding: utf-8 -*-

###############################################################################
#
# RegenerateKey
# Allows you to regenerate a new key with the same attributes and permissions as a previous key.
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

class RegenerateKey(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RegenerateKey Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(RegenerateKey, self).__init__(temboo_session, '/Library/Xively/APIKeys/RegenerateKey')


    def new_input_set(self):
        return RegenerateKeyInputSet()

    def _make_result_set(self, result, path):
        return RegenerateKeyResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RegenerateKeyChoreographyExecution(session, exec_id, path)

class RegenerateKeyInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RegenerateKey
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key you would like to regenerate. On successful regeneration, this API Key will no longer be valid.)
        """
        super(RegenerateKeyInputSet, self)._set_input('APIKey', value)
    def set_MasterAPIKey(self, value):
        """
        Set the value of the MasterAPIKey input for this Choreo. ((optional, string) Specify a MasterAPIKey with sufficient permissions if the APIKey you would like to regenerate does not have the permissions to do so.)
        """
        super(RegenerateKeyInputSet, self)._set_input('MasterAPIKey', value)

class RegenerateKeyResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RegenerateKey Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_APIKeyLocation(self):
        """
        Retrieve the value for the "APIKeyLocation" output from this Choreo execution. ((string) The URL of the newly regenerated APIKey.)
        """
        return self._output.get('APIKeyLocation', None)
    def get_NewAPIKey(self):
        """
        Retrieve the value for the "NewAPIKey" output from this Choreo execution. ((string) The regenerated APIKey obtained from the APIKeyLocation returned by this Choreo.)
        """
        return self._output.get('NewAPIKey', None)

class RegenerateKeyChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return RegenerateKeyResultSet(response, path)
