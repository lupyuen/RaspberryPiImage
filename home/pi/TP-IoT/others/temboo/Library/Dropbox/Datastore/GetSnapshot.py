# -*- coding: utf-8 -*-

###############################################################################
#
# GetSnapshot
# Returns a full snapshot of a datastore.
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

class GetSnapshot(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetSnapshot Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetSnapshot, self).__init__(temboo_session, '/Library/Dropbox/Datastore/GetSnapshot')


    def new_input_set(self):
        return GetSnapshotInputSet()

    def _make_result_set(self, result, path):
        return GetSnapshotResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetSnapshotChoreographyExecution(session, exec_id, path)

class GetSnapshotInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetSnapshot
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        super(GetSnapshotInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        super(GetSnapshotInputSet, self)._set_input('AccessToken', value)
    def set_AppKey(self, value):
        """
        Set the value of the AppKey input for this Choreo. ((required, string) The App Key provided by Dropbox (AKA the OAuth Consumer Key).)
        """
        super(GetSnapshotInputSet, self)._set_input('AppKey', value)
    def set_AppSecret(self, value):
        """
        Set the value of the AppSecret input for this Choreo. ((required, string) The App Secret provided by Dropbox (AKA the OAuth Consumer Secret).)
        """
        super(GetSnapshotInputSet, self)._set_input('AppSecret', value)
    def set_Handle(self, value):
        """
        Set the value of the Handle input for this Choreo. ((required, string) The handle of an existing datastore.)
        """
        super(GetSnapshotInputSet, self)._set_input('Handle', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to json.)
        """
        super(GetSnapshotInputSet, self)._set_input('ResponseFormat', value)

class GetSnapshotResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetSnapshot Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Dropbox. Corresponds to the ResponseFormat input. Defaults to json.)
        """
        return self._output.get('Response', None)

class GetSnapshotChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetSnapshotResultSet(response, path)
