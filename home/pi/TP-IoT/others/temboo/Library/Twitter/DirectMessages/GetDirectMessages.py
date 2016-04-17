# -*- coding: utf-8 -*-

###############################################################################
#
# GetDirectMessages
# Retrieves the 20 most recent direct messages sent to the authenticating user.
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

class GetDirectMessages(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetDirectMessages Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetDirectMessages, self).__init__(temboo_session, '/Library/Twitter/DirectMessages/GetDirectMessages')


    def new_input_set(self):
        return GetDirectMessagesInputSet()

    def _make_result_set(self, result, path):
        return GetDirectMessagesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetDirectMessagesChoreographyExecution(session, exec_id, path)

class GetDirectMessagesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetDirectMessages
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret provided by Twitter or retrieved during the OAuth process.)
        """
        super(GetDirectMessagesInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token provided by Twitter or retrieved during the OAuth process.)
        """
        super(GetDirectMessagesInputSet, self)._set_input('AccessToken', value)
    def set_ConsumerKey(self, value):
        """
        Set the value of the ConsumerKey input for this Choreo. ((required, string) The API Key (or Consumer Key) provided by Twitter.)
        """
        super(GetDirectMessagesInputSet, self)._set_input('ConsumerKey', value)
    def set_ConsumerSecret(self, value):
        """
        Set the value of the ConsumerSecret input for this Choreo. ((required, string) The API Secret (or Consumer Secret) provided by Twitter.)
        """
        super(GetDirectMessagesInputSet, self)._set_input('ConsumerSecret', value)
    def set_Count(self, value):
        """
        Set the value of the Count input for this Choreo. ((optional, integer) Specifies the number of records to retrieve up to a maximum of 200.)
        """
        super(GetDirectMessagesInputSet, self)._set_input('Count', value)
    def set_IncludeEntities(self, value):
        """
        Set the value of the IncludeEntities input for this Choreo. ((optional, boolean) The "entities" node containing extra metadata will not be included when set to false.)
        """
        super(GetDirectMessagesInputSet, self)._set_input('IncludeEntities', value)
    def set_MaxID(self, value):
        """
        Set the value of the MaxID input for this Choreo. ((optional, string) Returns results with an ID less than (older than) or equal to the specified ID.)
        """
        super(GetDirectMessagesInputSet, self)._set_input('MaxID', value)
    def set_Page(self, value):
        """
        Set the value of the Page input for this Choreo. ((optional, integer) Specifies the page of results to retrieve.)
        """
        super(GetDirectMessagesInputSet, self)._set_input('Page', value)
    def set_SinceID(self, value):
        """
        Set the value of the SinceID input for this Choreo. ((optional, string) Returns results with an ID greater than (more recent than) the specified ID.)
        """
        super(GetDirectMessagesInputSet, self)._set_input('SinceID', value)
    def set_SkipStatus(self, value):
        """
        Set the value of the SkipStatus input for this Choreo. ((optional, boolean) When set to true, statuses will not be included in the returned user objects.)
        """
        super(GetDirectMessagesInputSet, self)._set_input('SkipStatus', value)

class GetDirectMessagesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetDirectMessages Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Twitter.)
        """
        return self._output.get('Response', None)
    def get_Limit(self):
        """
        Retrieve the value for the "Limit" output from this Choreo execution. ((integer) The rate limit ceiling for this particular request.)
        """
        return self._output.get('Limit', None)
    def get_Remaining(self):
        """
        Retrieve the value for the "Remaining" output from this Choreo execution. ((integer) The number of requests left for the 15 minute window.)
        """
        return self._output.get('Remaining', None)
    def get_Reset(self):
        """
        Retrieve the value for the "Reset" output from this Choreo execution. ((date) The remaining window before the rate limit resets in UTC epoch seconds.)
        """
        return self._output.get('Reset', None)

class GetDirectMessagesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetDirectMessagesResultSet(response, path)
