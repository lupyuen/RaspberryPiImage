# -*- coding: utf-8 -*-

###############################################################################
#
# Delete
# Permanently deletes the profile from Mixpanel, along with all of its properties.
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

class Delete(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Delete Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(Delete, self).__init__(temboo_session, '/Library/Mixpanel/Profiles/Delete')


    def new_input_set(self):
        return DeleteInputSet()

    def _make_result_set(self, result, path):
        return DeleteResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteChoreographyExecution(session, exec_id, path)

class DeleteInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Delete
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_DistinctID(self, value):
        """
        Set the value of the DistinctID input for this Choreo. ((required, string) Used to uniquely identify the profile you want to update.)
        """
        super(DeleteInputSet, self)._set_input('DistinctID', value)
    def set_Token(self, value):
        """
        Set the value of the Token input for this Choreo. ((required, string) The token provided by Mixpanel. You can find your Mixpanel token in the project settings dialog in the Mixpanel app.)
        """
        super(DeleteInputSet, self)._set_input('Token', value)
    def set_Verbose(self, value):
        """
        Set the value of the Verbose input for this Choreo. ((optional, boolean) When set to 1, the response will contain more information describing the success or failure of the tracking call.)
        """
        super(DeleteInputSet, self)._set_input('Verbose', value)

class DeleteResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Delete Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Mixpanel.)
        """
        return self._output.get('Response', None)

class DeleteChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return DeleteResultSet(response, path)
