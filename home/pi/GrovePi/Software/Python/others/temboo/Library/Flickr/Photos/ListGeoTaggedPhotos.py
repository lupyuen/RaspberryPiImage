# -*- coding: utf-8 -*-

###############################################################################
#
# ListGeoTaggedPhotos
# Returns a list of your geo-tagged photos.
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

class ListGeoTaggedPhotos(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListGeoTaggedPhotos Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ListGeoTaggedPhotos, self).__init__(temboo_session, '/Library/Flickr/Photos/ListGeoTaggedPhotos')


    def new_input_set(self):
        return ListGeoTaggedPhotosInputSet()

    def _make_result_set(self, result, path):
        return ListGeoTaggedPhotosResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListGeoTaggedPhotosChoreographyExecution(session, exec_id, path)

class ListGeoTaggedPhotosInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListGeoTaggedPhotos
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Flickr (AKA the OAuth Consumer Key).)
        """
        super(ListGeoTaggedPhotosInputSet, self)._set_input('APIKey', value)
    def set_APISecret(self, value):
        """
        Set the value of the APISecret input for this Choreo. ((required, string) The API Secret provided by Flickr (AKA the OAuth Consumer Secret).)
        """
        super(ListGeoTaggedPhotosInputSet, self)._set_input('APISecret', value)
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        super(ListGeoTaggedPhotosInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        super(ListGeoTaggedPhotosInputSet, self)._set_input('AccessToken', value)
    def set_Extras(self, value):
        """
        Set the value of the Extras input for this Choreo. ((optional, string) A comma-delimited list of extra information to retrieve for each returned record. See Choreo documentation for accepted values.)
        """
        super(ListGeoTaggedPhotosInputSet, self)._set_input('Extras', value)
    def set_MaxTakenDate(self, value):
        """
        Set the value of the MaxTakenDate input for this Choreo. ((optional, date) Photos with an taken date less than or equal to this value will be returned. The date should be in the form of a mysql datetime.)
        """
        super(ListGeoTaggedPhotosInputSet, self)._set_input('MaxTakenDate', value)
    def set_MaxUploadDate(self, value):
        """
        Set the value of the MaxUploadDate input for this Choreo. ((optional, date) Photos with an upload date less than or equal to this value will be returned. The date should be in the form of a unix timestamp.)
        """
        super(ListGeoTaggedPhotosInputSet, self)._set_input('MaxUploadDate', value)
    def set_Media(self, value):
        """
        Set the value of the Media input for this Choreo. ((optional, string) Filter results by media type. Possible values are all (default), photos or videos.)
        """
        super(ListGeoTaggedPhotosInputSet, self)._set_input('Media', value)
    def set_MinTakenDate(self, value):
        """
        Set the value of the MinTakenDate input for this Choreo. ((optional, date) Photos with an taken date greater than or equal to this value will be returned. The date should be in the form of a mysql datetime.)
        """
        super(ListGeoTaggedPhotosInputSet, self)._set_input('MinTakenDate', value)
    def set_MinUploadDate(self, value):
        """
        Set the value of the MinUploadDate input for this Choreo. ((optional, date) Photos with an upload date greater than or equal to this value will be returned. The date should be in the form of a unix timestamp.)
        """
        super(ListGeoTaggedPhotosInputSet, self)._set_input('MinUploadDate', value)
    def set_Page(self, value):
        """
        Set the value of the Page input for this Choreo. ((optional, integer) The page of results to return. Used for paging through many results. Defaults to 1.)
        """
        super(ListGeoTaggedPhotosInputSet, self)._set_input('Page', value)
    def set_PerPage(self, value):
        """
        Set the value of the PerPage input for this Choreo. ((optional, integer) Number of photos to return per page. If this argument is omitted, it defaults to 100. The maximum allowed value is 500.)
        """
        super(ListGeoTaggedPhotosInputSet, self)._set_input('PerPage', value)
    def set_PrivacyFilter(self, value):
        """
        Set the value of the PrivacyFilter input for this Choreo. ((optional, integer) Valid values are: 1 (public photos), 2 (private photos visible to friends), 3 (private photos visible to family), 4 (private photos visible to friends and family), 5 (completely private photos).)
        """
        super(ListGeoTaggedPhotosInputSet, self)._set_input('PrivacyFilter', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: xml and json. Defaults to json.)
        """
        super(ListGeoTaggedPhotosInputSet, self)._set_input('ResponseFormat', value)
    def set_Sort(self, value):
        """
        Set the value of the Sort input for this Choreo. ((optional, string) The sort order. Accepted values are: date-posted-asc, date-posted-desc, date-taken-asc, date-taken-desc, interestingness-desc, and interestingness-asc.)
        """
        super(ListGeoTaggedPhotosInputSet, self)._set_input('Sort', value)

class ListGeoTaggedPhotosResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListGeoTaggedPhotos Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Flickr.)
        """
        return self._output.get('Response', None)

class ListGeoTaggedPhotosChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ListGeoTaggedPhotosResultSet(response, path)
