# -*- coding: utf-8 -*-

###############################################################################
#
# VenueHistory
# Returns a list of all venues visited by the specified user, along with how many visits and when they were last there. 
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

class VenueHistory(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the VenueHistory Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(VenueHistory, self).__init__(temboo_session, '/Library/Foursquare/Users/VenueHistory')


    def new_input_set(self):
        return VenueHistoryInputSet()

    def _make_result_set(self, result, path):
        return VenueHistoryResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return VenueHistoryChoreographyExecution(session, exec_id, path)

class VenueHistoryInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the VenueHistory
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AfterTimeStamp(self, value):
        """
        Set the value of the AfterTimeStamp input for this Choreo. ((optional, date) Retrieve the first results after the seconds entered since epoch time.)
        """
        super(VenueHistoryInputSet, self)._set_input('AfterTimeStamp', value)
    def set_BeforeTimeStamp(self, value):
        """
        Set the value of the BeforeTimeStamp input for this Choreo. ((optional, date) Retrieve the first results prior to the seconds specified. Useful for paging backward in time.)
        """
        super(VenueHistoryInputSet, self)._set_input('BeforeTimeStamp', value)
    def set_CategoryID(self, value):
        """
        Set the value of the CategoryID input for this Choreo. ((optional, string) Limits returned venues to those in this category. If specifying a top-level category, all sub-categories will also match the query.)
        """
        super(VenueHistoryInputSet, self)._set_input('CategoryID', value)
    def set_OauthToken(self, value):
        """
        Set the value of the OauthToken input for this Choreo. ((required, string) The Foursquare API OAuth token string.)
        """
        super(VenueHistoryInputSet, self)._set_input('OauthToken', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        super(VenueHistoryInputSet, self)._set_input('ResponseFormat', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((optional, string) Only 'self' is supported at this moment by the Foursquare API. Defaults to: self.)
        """
        super(VenueHistoryInputSet, self)._set_input('UserID', value)

class VenueHistoryResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the VenueHistory Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        return self._output.get('Response', None)

class VenueHistoryChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return VenueHistoryResultSet(response, path)
