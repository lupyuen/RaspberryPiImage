# -*- coding: utf-8 -*-

###############################################################################
#
# ListSearchResults
# Returns a list of search results that match the specified query parameters.
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

class ListSearchResults(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListSearchResults Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ListSearchResults, self).__init__(temboo_session, '/Library/YouTube/Search/ListSearchResults')


    def new_input_set(self):
        return ListSearchResultsInputSet()

    def _make_result_set(self, result, path):
        return ListSearchResultsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListSearchResultsChoreographyExecution(session, exec_id, path)

class ListSearchResultsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListSearchResults
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((optional, string) The API Key provided by Google for simple API access when you do not need to access user data.)
        """
        super(ListSearchResultsInputSet, self)._set_input('APIKey', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid access token retrieved during the OAuth process. This is required for OAuth authentication unless you provide the ClientID, ClientSecret, and RefreshToken to generate a new access token.)
        """
        super(ListSearchResultsInputSet, self)._set_input('AccessToken', value)
    def set_ChannelID(self, value):
        """
        Set the value of the ChannelID input for this Choreo. ((optional, string) Indicates that the response should only contain resources created by this channel.)
        """
        super(ListSearchResultsInputSet, self)._set_input('ChannelID', value)
    def set_ChannelType(self, value):
        """
        Set the value of the ChannelType input for this Choreo. ((optional, string) Restricts a search to a particular type of channel. Valid values are: "any" (returns all channels) and "show" (only retrieves shows).)
        """
        super(ListSearchResultsInputSet, self)._set_input('ChannelType', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((optional, string) The Client ID provided by Google. Required for OAuth authentication unless providing a valid AccessToken.)
        """
        super(ListSearchResultsInputSet, self)._set_input('ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((optional, string) The Client Secret provided by Google. Required for OAuth authentication unless providing a valid AccessToken.)
        """
        super(ListSearchResultsInputSet, self)._set_input('ClientSecret', value)
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, string) Allows you to specify a subset of fields to include in the response using an xpath-like syntax (i.e. items/snippet/title).)
        """
        super(ListSearchResultsInputSet, self)._set_input('Fields', value)
    def set_MaxResults(self, value):
        """
        Set the value of the MaxResults input for this Choreo. ((optional, integer) The maximum number of results to return.)
        """
        super(ListSearchResultsInputSet, self)._set_input('MaxResults', value)
    def set_Order(self, value):
        """
        Set the value of the Order input for this Choreo. ((optional, string) Indicates how the results are sorted. Valid values are: date, rating, relevance, and viewCount.)
        """
        super(ListSearchResultsInputSet, self)._set_input('Order', value)
    def set_PageToken(self, value):
        """
        Set the value of the PageToken input for this Choreo. ((optional, string) The "nextPageToken" found in the response which is used to page through results.)
        """
        super(ListSearchResultsInputSet, self)._set_input('PageToken', value)
    def set_Part(self, value):
        """
        Set the value of the Part input for this Choreo. ((optional, string) Specifies a comma-separated list of one or more search resource properties that the API response will include. Part names that you can pass are 'id' and 'snippet' (the default).)
        """
        super(ListSearchResultsInputSet, self)._set_input('Part', value)
    def set_PublishedAfter(self, value):
        """
        Set the value of the PublishedAfter input for this Choreo. ((optional, date) Returns only results created after the specified time (formatted as a RFC 3339 date-time i.e. 1970-01-01T00:00:00Z).)
        """
        super(ListSearchResultsInputSet, self)._set_input('PublishedAfter', value)
    def set_PublishedBefore(self, value):
        """
        Set the value of the PublishedBefore input for this Choreo. ((optional, date) Returns only results created before the specified time (formatted as a RFC 3339 date-time i.e. 1970-01-01T00:00:00Z).)
        """
        super(ListSearchResultsInputSet, self)._set_input('PublishedBefore', value)
    def set_Query(self, value):
        """
        Set the value of the Query input for this Choreo. ((conditional, string) A query string for searching videos.)
        """
        super(ListSearchResultsInputSet, self)._set_input('Query', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((optional, string) An OAuth refresh token used to generate a new access token when the original token is expired. Required for OAuth authentication unless providing a valid AccessToken.)
        """
        super(ListSearchResultsInputSet, self)._set_input('RefreshToken', value)
    def set_RegionCode(self, value):
        """
        Set the value of the RegionCode input for this Choreo. ((optional, string) Returns results for the specified country. The parameter value is an ISO 3166-1 alpha-2 country code.)
        """
        super(ListSearchResultsInputSet, self)._set_input('RegionCode', value)
    def set_RelatedToVideoID(self, value):
        """
        Set the value of the RelatedToVideoID input for this Choreo. ((optional, string) Retrieves a list of videos that are related to this video id. When using this parameter, the Type parameter must be set to video.)
        """
        super(ListSearchResultsInputSet, self)._set_input('RelatedToVideoID', value)
    def set_TopicID(self, value):
        """
        Set the value of the TopicID input for this Choreo. ((optional, string) Returns only results associated with the specified topic.)
        """
        super(ListSearchResultsInputSet, self)._set_input('TopicID', value)
    def set_Type(self, value):
        """
        Set the value of the Type input for this Choreo. ((optional, string) Restricts a search query to only retrieve a particular type of resource. The default value is: video,channel,playlist.)
        """
        super(ListSearchResultsInputSet, self)._set_input('Type', value)
    def set_VideoCaption(self, value):
        """
        Set the value of the VideoCaption input for this Choreo. ((optional, string) Returns filtered results based on whether videos have captions. Valid values are: any (the default), closedCaption (only returns videos with captions), or none (only returns videos without captions).)
        """
        super(ListSearchResultsInputSet, self)._set_input('VideoCaption', value)
    def set_VideoCategoryID(self, value):
        """
        Set the value of the VideoCategoryID input for this Choreo. ((optional, string) Filters video search results based on their category.)
        """
        super(ListSearchResultsInputSet, self)._set_input('VideoCategoryID', value)
    def set_VideoDefinition(self, value):
        """
        Set the value of the VideoDefinition input for this Choreo. ((optional, string) Filters video results based high or standard definition. Valid values are: any, high, or standard.)
        """
        super(ListSearchResultsInputSet, self)._set_input('VideoDefinition', value)
    def set_VideoDimension(self, value):
        """
        Set the value of the VideoDimension input for this Choreo. ((optional, string) Restrict a search to only retrieve 2D or 3D videos. Valid values are: 2d, 3d, or any.)
        """
        super(ListSearchResultsInputSet, self)._set_input('VideoDimension', value)
    def set_VideoDuration(self, value):
        """
        Set the value of the VideoDuration input for this Choreo. ((optional, string) Filters search results based on the video duration. Valid values are: any, long, medium, and short.)
        """
        super(ListSearchResultsInputSet, self)._set_input('VideoDuration', value)
    def set_VideoEmbeddable(self, value):
        """
        Set the value of the VideoEmbeddable input for this Choreo. ((optional, string) Filters search results to include only videos that can be embedded into a webpage. Valid values are: any (the default) or true (which will enable this filter).)
        """
        super(ListSearchResultsInputSet, self)._set_input('VideoEmbeddable', value)
    def set_VideoLicense(self, value):
        """
        Set the value of the VideoLicense input for this Choreo. ((optional, string) Filters search results to only include videos with a particular license. Valid values are: any, creativeCommon, and youtube.)
        """
        super(ListSearchResultsInputSet, self)._set_input('VideoLicense', value)
    def set_VideoSyndicated(self, value):
        """
        Set the value of the VideoSyndicated input for this Choreo. ((optional, string) Filters search results for videos that can be played outside of youtube.com. Valid values are: any (the default) or true (which will enable this filter).)
        """
        super(ListSearchResultsInputSet, self)._set_input('VideoSyndicated', value)
    def set_VideoType(self, value):
        """
        Set the value of the VideoType input for this Choreo. ((optional, string) Filters search results to a particular type of videos. Valid values are: any, episode, and movie.)
        """
        super(ListSearchResultsInputSet, self)._set_input('VideoType', value)

class ListSearchResultsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListSearchResults Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from YouTube.)
        """
        return self._output.get('Response', None)
    def get_NewAccessToken(self):
        """
        Retrieve the value for the "NewAccessToken" output from this Choreo execution. ((string) Contains a new AccessToken when the RefreshToken is provided.)
        """
        return self._output.get('NewAccessToken', None)

class ListSearchResultsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ListSearchResultsResultSet(response, path)
