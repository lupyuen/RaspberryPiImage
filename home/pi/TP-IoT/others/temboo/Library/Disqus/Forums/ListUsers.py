# -*- coding: utf-8 -*-

###############################################################################
#
# ListUsers
# Retrieve a list of active users within a forum.
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

class ListUsers(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListUsers Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ListUsers, self).__init__(temboo_session, '/Library/Disqus/Forums/ListUsers')


    def new_input_set(self):
        return ListUsersInputSet()

    def _make_result_set(self, result, path):
        return ListUsersResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListUsersChoreographyExecution(session, exec_id, path)

class ListUsersInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListUsers
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid OAuth 2.0 access token.)
        """
        super(ListUsersInputSet, self)._set_input('AccessToken', value)
    def set_Cursor(self, value):
        """
        Set the value of the Cursor input for this Choreo. ((optional, string) Default is set to null.)
        """
        super(ListUsersInputSet, self)._set_input('Cursor', value)
    def set_Forum(self, value):
        """
        Set the value of the Forum input for this Choreo. ((required, string) Forum Short Name (i.e., the subdomain of the Disqus Site URL).  Displays all users contained in that  forum.  If null, users from all forums moderated by the authenticating user will be retrieved.)
        """
        super(ListUsersInputSet, self)._set_input('Forum', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) The number of records to return. Defaults to 25.)
        """
        super(ListUsersInputSet, self)._set_input('Limit', value)
    def set_Order(self, value):
        """
        Set the value of the Order input for this Choreo. ((optional, string) The sort order of the results. Valid values are: asc or desc. Default is set to: asc.)
        """
        super(ListUsersInputSet, self)._set_input('Order', value)
    def set_PublicKey(self, value):
        """
        Set the value of the PublicKey input for this Choreo. ((required, string) The Public Key provided by Disqus (AKA the API Key).)
        """
        super(ListUsersInputSet, self)._set_input('PublicKey', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default), jsonp, or rss.)
        """
        super(ListUsersInputSet, self)._set_input('ResponseFormat', value)
    def set_SinceID(self, value):
        """
        Set the value of the SinceID input for this Choreo. ((optional, string) A Unix timestamp (or ISO datetime standard) to obtain results from. (e.g. 2014-02-02T01:01:00Z) Default is set to null.)
        """
        super(ListUsersInputSet, self)._set_input('SinceID', value)

class ListUsersResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListUsers Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Disqus.)
        """
        return self._output.get('Response', None)

class ListUsersChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ListUsersResultSet(response, path)
