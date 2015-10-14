# -*- coding: utf-8 -*-

###############################################################################
#
# GetRecentBookmarks
# Retrieve a list of the most recently posted bookmarks.
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

class GetRecentBookmarks(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetRecentBookmarks Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetRecentBookmarks, self).__init__(temboo_session, '/Library/Delicious/GetRecentBookmarks')


    def new_input_set(self):
        return GetRecentBookmarksInputSet()

    def _make_result_set(self, result, path):
        return GetRecentBookmarksResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetRecentBookmarksChoreographyExecution(session, exec_id, path)

class GetRecentBookmarksInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetRecentBookmarks
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Count(self, value):
        """
        Set the value of the Count input for this Choreo. ((optional, integer) Specify the number of bookmarks to retrieve, up the maximum of 100. The default is 15.)
        """
        super(GetRecentBookmarksInputSet, self)._set_input('Count', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) The password that corresponds to the specified Delicious account username.)
        """
        super(GetRecentBookmarksInputSet, self)._set_input('Password', value)
    def set_Tags(self, value):
        """
        Set the value of the Tags input for this Choreo. ((optional, string) Return only items tagged with the specified keyword.)
        """
        super(GetRecentBookmarksInputSet, self)._set_input('Tags', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) A valid Delicious account username.)
        """
        super(GetRecentBookmarksInputSet, self)._set_input('Username', value)

class GetRecentBookmarksResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetRecentBookmarks Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response returned from Delicious.)
        """
        return self._output.get('Response', None)

class GetRecentBookmarksChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetRecentBookmarksResultSet(response, path)
