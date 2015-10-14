# -*- coding: utf-8 -*-

###############################################################################
#
# ListComments
# Retrieves comments for a specified gist.
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

class ListComments(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListComments Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ListComments, self).__init__(temboo_session, '/Library/GitHub/GistsAPI/Comments/ListComments')


    def new_input_set(self):
        return ListCommentsInputSet()

    def _make_result_set(self, result, path):
        return ListCommentsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListCommentsChoreographyExecution(session, exec_id, path)

class ListCommentsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListComments
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_ID(self, value):
        """
        Set the value of the ID input for this Choreo. ((required, string) The id of the gist to fetch comments for.)
        """
        super(ListCommentsInputSet, self)._set_input('ID', value)
    def set_Page(self, value):
        """
        Set the value of the Page input for this Choreo. ((optional, integer) Indicates the page index that you want to retrieve. Defaults to 1.)
        """
        super(ListCommentsInputSet, self)._set_input('Page', value)
    def set_PerPage(self, value):
        """
        Set the value of the PerPage input for this Choreo. ((optional, integer) The number of results to return per page.)
        """
        super(ListCommentsInputSet, self)._set_input('PerPage', value)

class ListCommentsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListComments Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from GitHub.)
        """
        return self._output.get('Response', None)
    def get_FirstPage(self):
        """
        Retrieve the value for the "FirstPage" output from this Choreo execution. ((integer) The index for the first page of results.)
        """
        return self._output.get('FirstPage', None)
    def get_LastPage(self):
        """
        Retrieve the value for the "LastPage" output from this Choreo execution. ((integer) The index for the first page of results.)
        """
        return self._output.get('LastPage', None)
    def get_Limit(self):
        """
        Retrieve the value for the "Limit" output from this Choreo execution. ((integer) The available rate limit for your account. This is returned in the GitHub response header.)
        """
        return self._output.get('Limit', None)
    def get_NextPage(self):
        """
        Retrieve the value for the "NextPage" output from this Choreo execution. ((integer) The index for the next page of results.)
        """
        return self._output.get('NextPage', None)
    def get_PreviousPage(self):
        """
        Retrieve the value for the "PreviousPage" output from this Choreo execution. ((integer) The index for the previous page of results.)
        """
        return self._output.get('PreviousPage', None)
    def get_Remaining(self):
        """
        Retrieve the value for the "Remaining" output from this Choreo execution. ((integer) The remaining number of API requests available to you. This is returned in the GitHub response header.)
        """
        return self._output.get('Remaining', None)

class ListCommentsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ListCommentsResultSet(response, path)
