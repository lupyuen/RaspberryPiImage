# -*- coding: utf-8 -*-

###############################################################################
#
# GetAllBookmarks
# Returns all links posted to a Delicious account.
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

class GetAllBookmarks(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetAllBookmarks Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetAllBookmarks, self).__init__(temboo_session, '/Library/Delicious/GetAllBookmarks')


    def new_input_set(self):
        return GetAllBookmarksInputSet()

    def _make_result_set(self, result, path):
        return GetAllBookmarksResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetAllBookmarksChoreographyExecution(session, exec_id, path)

class GetAllBookmarksInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetAllBookmarks
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Count(self, value):
        """
        Set the value of the Count input for this Choreo. ((optional, integer) The number of bookmarks to return. Defaults to 15.)
        """
        super(GetAllBookmarksInputSet, self)._set_input('Count', value)
    def set_FromDate(self, value):
        """
        Set the value of the FromDate input for this Choreo. ((optional, date) Return only bookmarks posted on this date and later. Enter in YYYY-MM-DDThh:mm:ssZ format.)
        """
        super(GetAllBookmarksInputSet, self)._set_input('FromDate', value)
    def set_Meta(self, value):
        """
        Set the value of the Meta input for this Choreo. ((optional, string) Specify "1" to include a change-detection signature for each item returned. Defaults to "0", or no meta attributes retained.)
        """
        super(GetAllBookmarksInputSet, self)._set_input('Meta', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) The password that corresponds to the specified Delicious account username.)
        """
        super(GetAllBookmarksInputSet, self)._set_input('Password', value)
    def set_Tag(self, value):
        """
        Set the value of the Tag input for this Choreo. ((optional, string) Return only bookmrks tagged with this keyword.)
        """
        super(GetAllBookmarksInputSet, self)._set_input('Tag', value)
    def set_ToDate(self, value):
        """
        Set the value of the ToDate input for this Choreo. ((optional, date) Return only bookmarks posted on this date and earlier. Enter in YYYY-MM-DDThh:mm:ssZ format.)
        """
        super(GetAllBookmarksInputSet, self)._set_input('ToDate', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) A valid Delicious account username.)
        """
        super(GetAllBookmarksInputSet, self)._set_input('Username', value)

class GetAllBookmarksResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetAllBookmarks Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response returned from Delicious.)
        """
        return self._output.get('Response', None)

class GetAllBookmarksChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetAllBookmarksResultSet(response, path)
