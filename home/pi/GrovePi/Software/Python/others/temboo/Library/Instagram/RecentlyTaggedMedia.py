# -*- coding: utf-8 -*-

###############################################################################
#
# RecentlyTaggedMedia
# Retrieves a list of recently tagged media.
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

class RecentlyTaggedMedia(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RecentlyTaggedMedia Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(RecentlyTaggedMedia, self).__init__(temboo_session, '/Library/Instagram/RecentlyTaggedMedia')


    def new_input_set(self):
        return RecentlyTaggedMediaInputSet()

    def _make_result_set(self, result, path):
        return RecentlyTaggedMediaResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RecentlyTaggedMediaChoreographyExecution(session, exec_id, path)

class RecentlyTaggedMediaInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RecentlyTaggedMedia
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((conditional, string) The access token retrieved during the OAuth 2.0 process. Required unless you provide the ClientID.)
        """
        super(RecentlyTaggedMediaInputSet, self)._set_input('AccessToken', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by Instagram after registering your application. Required unless you provide the AccessToken.)
        """
        super(RecentlyTaggedMediaInputSet, self)._set_input('ClientID', value)
    def set_Count(self, value):
        """
        Set the value of the Count input for this Choreo. ((optional, integer) The number of results to return.)
        """
        super(RecentlyTaggedMediaInputSet, self)._set_input('Count', value)
    def set_MaxID(self, value):
        """
        Set the value of the MaxID input for this Choreo. ((optional, integer) Returns media tagged earlier than this max_tag_id. Used to paginate through results.)
        """
        super(RecentlyTaggedMediaInputSet, self)._set_input('MaxID', value)
    def set_MinID(self, value):
        """
        Set the value of the MinID input for this Choreo. ((optional, integer) Returns media tagged later than this max_tag_id. Used to paginate through results.)
        """
        super(RecentlyTaggedMediaInputSet, self)._set_input('MinID', value)
    def set_TagName(self, value):
        """
        Set the value of the TagName input for this Choreo. ((required, string) Enter a valid tag identifier, such as: nofliter)
        """
        super(RecentlyTaggedMediaInputSet, self)._set_input('TagName', value)

class RecentlyTaggedMediaResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RecentlyTaggedMedia Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Instagram.)
        """
        return self._output.get('Response', None)

class RecentlyTaggedMediaChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return RecentlyTaggedMediaResultSet(response, path)
