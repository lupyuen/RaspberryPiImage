# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteObject
# Deletes objects in the graph with a given id or path.
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

class DeleteObject(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteObject Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(DeleteObject, self).__init__(temboo_session, '/Library/Facebook/Deleting/DeleteObject')


    def new_input_set(self):
        return DeleteObjectInputSet()

    def _make_result_set(self, result, path):
        return DeleteObjectResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteObjectChoreographyExecution(session, exec_id, path)

class DeleteObjectInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteObject
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved from the final step of the OAuth process.)
        """
        super(DeleteObjectInputSet, self)._set_input('AccessToken', value)
    def set_ObjectID(self, value):
        """
        Set the value of the ObjectID input for this Choreo. ((required, string) The id or path to an object to delete.)
        """
        super(DeleteObjectInputSet, self)._set_input('ObjectID', value)

class DeleteObjectResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteObject Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((boolean) The response from Facebook. Returns "true" on success.)
        """
        return self._output.get('Response', None)

class DeleteObjectChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return DeleteObjectResultSet(response, path)
