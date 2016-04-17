# -*- coding: utf-8 -*-

###############################################################################
#
# ListForums
# Retrieve a list of forums owned by the specified user.
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

class ListForums(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListForums Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ListForums, self).__init__(temboo_session, '/Library/Disqus/Users/ListForums')


    def new_input_set(self):
        return ListForumsInputSet()

    def _make_result_set(self, result, path):
        return ListForumsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListForumsChoreographyExecution(session, exec_id, path)

class ListForumsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListForums
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Cursor(self, value):
        """
        Set the value of the Cursor input for this Choreo. ((optional, string) Default is set to null.)
        """
        super(ListForumsInputSet, self)._set_input('Cursor', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) The number of records to return. Defaults to 25.)
        """
        super(ListForumsInputSet, self)._set_input('Limit', value)
    def set_Order(self, value):
        """
        Set the value of the Order input for this Choreo. ((optional, string) The sort order for the results. Valid vaues are: asc or desc. Default is set to: asc.)
        """
        super(ListForumsInputSet, self)._set_input('Order', value)
    def set_PublicKey(self, value):
        """
        Set the value of the PublicKey input for this Choreo. ((required, string) The Public Key provided by Disqus (AKA the API Key).)
        """
        super(ListForumsInputSet, self)._set_input('PublicKey', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default), jsonp, or rss.)
        """
        super(ListForumsInputSet, self)._set_input('ResponseFormat', value)
    def set_SinceID(self, value):
        """
        Set the value of the SinceID input for this Choreo. ((optional, string) A Unix timestamp to obtain results from. Default is set to null.)
        """
        super(ListForumsInputSet, self)._set_input('SinceID', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((conditional, string) The Disqus User ID, for which active forum information will be retrieved.  If UserID is set, then Username must be null.)
        """
        super(ListForumsInputSet, self)._set_input('UserID', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((conditional, string) A Disqus username.  If Username is being set, then UserID must be null.)
        """
        super(ListForumsInputSet, self)._set_input('Username', value)

class ListForumsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListForums Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Disqus.)
        """
        return self._output.get('Response', None)

class ListForumsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ListForumsResultSet(response, path)
