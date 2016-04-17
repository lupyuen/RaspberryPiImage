# -*- coding: utf-8 -*-

###############################################################################
#
# GetBookmark
# Retrieves one or more bookmarked links posted on a single day.
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

class GetBookmark(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetBookmark Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetBookmark, self).__init__(temboo_session, '/Library/Delicious/GetBookmark')


    def new_input_set(self):
        return GetBookmarkInputSet()

    def _make_result_set(self, result, path):
        return GetBookmarkResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetBookmarkChoreographyExecution(session, exec_id, path)

class GetBookmarkInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetBookmark
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_ChangeSignature(self, value):
        """
        Set the value of the ChangeSignature input for this Choreo. ((optional, string) Return only bookmarks with the URL MD5 signatures you enter, regardless of posting date. Separate multiple signatures with spaces.)
        """
        super(GetBookmarkInputSet, self)._set_input('ChangeSignature', value)
    def set_Date(self, value):
        """
        Set the value of the Date input for this Choreo. ((optional, date) Return only bookmarks posted on a date specified here. Enter in YYYY-MM-DDThh:mm:ssZ format. Defaults to the most recent date.)
        """
        super(GetBookmarkInputSet, self)._set_input('Date', value)
    def set_Meta(self, value):
        """
        Set the value of the Meta input for this Choreo. ((optional, string) Specify "1" to include a change-detection signature for each item returned. Defaults to "0", or no meta attributes retained.)
        """
        super(GetBookmarkInputSet, self)._set_input('Meta', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) The password that corresponds to the specified Delicious account username.)
        """
        super(GetBookmarkInputSet, self)._set_input('Password', value)
    def set_Tag(self, value):
        """
        Set the value of the Tag input for this Choreo. ((optional, string) Return only items tagged with the specified keyword. Separate multiple tags with spaces.)
        """
        super(GetBookmarkInputSet, self)._set_input('Tag', value)
    def set_URL(self, value):
        """
        Set the value of the URL input for this Choreo. ((optional, string) Return only items with the specified URL, regardless of posting date.)
        """
        super(GetBookmarkInputSet, self)._set_input('URL', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) A valid Delicious account username.)
        """
        super(GetBookmarkInputSet, self)._set_input('Username', value)

class GetBookmarkResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetBookmark Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response returned from Delicious.)
        """
        return self._output.get('Response', None)

class GetBookmarkChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetBookmarkResultSet(response, path)
