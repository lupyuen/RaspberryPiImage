# -*- coding: utf-8 -*-

###############################################################################
#
# Paginate
# Retrieves the next or previous page of results.
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

class Paginate(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Paginate Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(Paginate, self).__init__(temboo_session, '/Library/Facebook/Reading/Paginate')


    def new_input_set(self):
        return PaginateInputSet()

    def _make_result_set(self, result, path):
        return PaginateResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PaginateChoreographyExecution(session, exec_id, path)

class PaginateInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Paginate
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to json.)
        """
        super(PaginateInputSet, self)._set_input('ResponseFormat', value)
    def set_URL(self, value):
        """
        Set the value of the URL input for this Choreo. ((required, string) A "next" or "previous" URL associated with another page of results to retrieve.)
        """
        super(PaginateInputSet, self)._set_input('URL', value)

class PaginateResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Paginate Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Facebook.)
        """
        return self._output.get('Response', None)
    def get_Next(self):
        """
        Retrieve the value for the "Next" output from this Choreo execution. ((string) The URL to use to retrieve the next page of the results.)
        """
        return self._output.get('Next', None)
    def get_Previous(self):
        """
        Retrieve the value for the "Previous" output from this Choreo execution. ((string) The URL to use to retrieve the previous page of results.)
        """
        return self._output.get('Previous', None)

class PaginateChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return PaginateResultSet(response, path)
