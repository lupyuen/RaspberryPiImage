# -*- coding: utf-8 -*-

###############################################################################
#
# CreateWatch
# Creates an action that represents a user watching video content.
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

class CreateWatch(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateWatch Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CreateWatch, self).__init__(temboo_session, '/Library/Facebook/Actions/Video/Watches/CreateWatch')


    def new_input_set(self):
        return CreateWatchInputSet()

    def _make_result_set(self, result, path):
        return CreateWatchResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateWatchChoreographyExecution(session, exec_id, path)

class CreateWatchInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateWatch
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved from the final step of the OAuth process.)
        """
        super(CreateWatchInputSet, self)._set_input('AccessToken', value)
    def set_CreatedTime(self, value):
        """
        Set the value of the CreatedTime input for this Choreo. ((optional, date) The time that the action was created (e.g. 2013-06-24T18:53:35+0000).)
        """
        super(CreateWatchInputSet, self)._set_input('CreatedTime', value)
    def set_EndTime(self, value):
        """
        Set the value of the EndTime input for this Choreo. ((optional, date) The time that the user ended the action (e.g. 2013-06-24T18:53:35+0000).)
        """
        super(CreateWatchInputSet, self)._set_input('EndTime', value)
    def set_Episode(self, value):
        """
        Set the value of the Episode input for this Choreo. ((conditional, string) The URL or ID for an Open Graph object representing an episode of a show.)
        """
        super(CreateWatchInputSet, self)._set_input('Episode', value)
    def set_ExpiresIn(self, value):
        """
        Set the value of the ExpiresIn input for this Choreo. ((optional, integer) The amount of time (in milliseconds) from the publish_time that the action will expire.)
        """
        super(CreateWatchInputSet, self)._set_input('ExpiresIn', value)
    def set_ExplicitlyShared(self, value):
        """
        Set the value of the ExplicitlyShared input for this Choreo. ((optional, boolean) Indicates that the user is explicitly sharing this action. Requires the explicitly_shared capability to be enabled.)
        """
        super(CreateWatchInputSet, self)._set_input('ExplicitlyShared', value)
    def set_ExplicityShared(self, value):
        """
        Set the value of the ExplicityShared input for this Choreo. ((optional, boolean) Deprecated (retained for backward compatibility only).)
        """
        super(CreateWatchInputSet, self)._set_input('ExplicityShared', value)
    def set_Message(self, value):
        """
        Set the value of the Message input for this Choreo. ((optional, string) A message attached to this action. Setting this parameter requires enabling of message capabilities.)
        """
        super(CreateWatchInputSet, self)._set_input('Message', value)
    def set_Movie(self, value):
        """
        Set the value of the Movie input for this Choreo. ((conditional, string) The URL or ID for an Open Graph object representing a movie.)
        """
        super(CreateWatchInputSet, self)._set_input('Movie', value)
    def set_NoFeedStory(self, value):
        """
        Set the value of the NoFeedStory input for this Choreo. ((optional, boolean) Whether or not this action should be posted to the users feed.)
        """
        super(CreateWatchInputSet, self)._set_input('NoFeedStory', value)
    def set_Place(self, value):
        """
        Set the value of the Place input for this Choreo. ((optional, string) The URL or ID for an Open Graph object representing the location associated with this action.)
        """
        super(CreateWatchInputSet, self)._set_input('Place', value)
    def set_ProfileID(self, value):
        """
        Set the value of the ProfileID input for this Choreo. ((optional, string) The id of the user's profile. Defaults to "me" indicating the authenticated user.)
        """
        super(CreateWatchInputSet, self)._set_input('ProfileID', value)
    def set_Reference(self, value):
        """
        Set the value of the Reference input for this Choreo. ((optional, string) A string identifier up to 50 characters used for tracking and insights.)
        """
        super(CreateWatchInputSet, self)._set_input('Reference', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to json.)
        """
        super(CreateWatchInputSet, self)._set_input('ResponseFormat', value)
    def set_StartTime(self, value):
        """
        Set the value of the StartTime input for this Choreo. ((optional, date) The time that the user started the action (e.g. 2013-06-24T18:53:35+0000).)
        """
        super(CreateWatchInputSet, self)._set_input('StartTime', value)
    def set_TVShow(self, value):
        """
        Set the value of the TVShow input for this Choreo. ((conditional, string) The URL or ID for an Open Graph object representing a TV show.)
        """
        super(CreateWatchInputSet, self)._set_input('TVShow', value)
    def set_Tags(self, value):
        """
        Set the value of the Tags input for this Choreo. ((optional, string) A comma separated list of other profile IDs that also performed this action.)
        """
        super(CreateWatchInputSet, self)._set_input('Tags', value)
    def set_Video(self, value):
        """
        Set the value of the Video input for this Choreo. ((conditional, string) The URL or ID for an Open Graph object representing any general video content.)
        """
        super(CreateWatchInputSet, self)._set_input('Video', value)

class CreateWatchResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateWatch Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Facebook.)
        """
        return self._output.get('Response', None)
    def get_ActivityURL(self):
        """
        Retrieve the value for the "ActivityURL" output from this Choreo execution. ((string) The URL for the newly created action.)
        """
        return self._output.get('ActivityURL', None)

class CreateWatchChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CreateWatchResultSet(response, path)
