# -*- coding: utf-8 -*-

###############################################################################
#
# GetContextForFavorite
# Returns next and previous favorites for a photo in a user's favorites.
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

class GetContextForFavorite(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetContextForFavorite Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetContextForFavorite, self).__init__(temboo_session, '/Library/Flickr/Favorites/GetContextForFavorite')


    def new_input_set(self):
        return GetContextForFavoriteInputSet()

    def _make_result_set(self, result, path):
        return GetContextForFavoriteResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetContextForFavoriteChoreographyExecution(session, exec_id, path)

class GetContextForFavoriteInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetContextForFavorite
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Flickr (AKA the OAuth Consumer Key).)
        """
        super(GetContextForFavoriteInputSet, self)._set_input('APIKey', value)
    def set_PhotoID(self, value):
        """
        Set the value of the PhotoID input for this Choreo. ((required, integer) The id of the photo to fetch the context for.)
        """
        super(GetContextForFavoriteInputSet, self)._set_input('PhotoID', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: xml and json. Defaults to json.)
        """
        super(GetContextForFavoriteInputSet, self)._set_input('ResponseFormat', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((required, string) The user who counts the photo as a favorite.)
        """
        super(GetContextForFavoriteInputSet, self)._set_input('UserID', value)

class GetContextForFavoriteResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetContextForFavorite Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Flickr.)
        """
        return self._output.get('Response', None)

class GetContextForFavoriteChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetContextForFavoriteResultSet(response, path)
