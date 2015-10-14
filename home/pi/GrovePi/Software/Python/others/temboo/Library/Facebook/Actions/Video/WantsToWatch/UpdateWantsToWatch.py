# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateWantsToWatch
# Updates an existing wants_to_watch action.
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

class UpdateWantsToWatch(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateWantsToWatch Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(UpdateWantsToWatch, self).__init__(temboo_session, '/Library/Facebook/Actions/Video/WantsToWatch/UpdateWantsToWatch')


    def new_input_set(self):
        return UpdateWantsToWatchInputSet()

    def _make_result_set(self, result, path):
        return UpdateWantsToWatchResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateWantsToWatchChoreographyExecution(session, exec_id, path)

class UpdateWantsToWatchInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateWantsToWatch
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved from the final step of the OAuth process.)
        """
        super(UpdateWantsToWatchInputSet, self)._set_input('AccessToken', value)
    def set_ActionID(self, value):
        """
        Set the value of the ActionID input for this Choreo. ((required, string) The id of the action to update.)
        """
        super(UpdateWantsToWatchInputSet, self)._set_input('ActionID', value)
    def set_AiringEndTime(self, value):
        """
        Set the value of the AiringEndTime input for this Choreo. ((optional, date) The time that the airing ends.)
        """
        super(UpdateWantsToWatchInputSet, self)._set_input('AiringEndTime', value)
    def set_AiringID(self, value):
        """
        Set the value of the AiringID input for this Choreo. ((optional, string) The id of the video airing.)
        """
        super(UpdateWantsToWatchInputSet, self)._set_input('AiringID', value)
    def set_AiringStartTime(self, value):
        """
        Set the value of the AiringStartTime input for this Choreo. ((optional, date) The time that the airing begins.)
        """
        super(UpdateWantsToWatchInputSet, self)._set_input('AiringStartTime', value)
    def set_EndTime(self, value):
        """
        Set the value of the EndTime input for this Choreo. ((optional, date) The time that the user ended the action (e.g. 2013-06-24T18:53:35+0000).)
        """
        super(UpdateWantsToWatchInputSet, self)._set_input('EndTime', value)
    def set_Episode(self, value):
        """
        Set the value of the Episode input for this Choreo. ((optional, string) The URL or ID for an Open Graph object representing an episode of a show.)
        """
        super(UpdateWantsToWatchInputSet, self)._set_input('Episode', value)
    def set_ExpiresIn(self, value):
        """
        Set the value of the ExpiresIn input for this Choreo. ((optional, integer) The amount of time (in milliseconds) from the publish_time that the action will expire.)
        """
        super(UpdateWantsToWatchInputSet, self)._set_input('ExpiresIn', value)
    def set_Message(self, value):
        """
        Set the value of the Message input for this Choreo. ((optional, string) A message attached to this action. Setting this parameter requires enabling of message capabilities.)
        """
        super(UpdateWantsToWatchInputSet, self)._set_input('Message', value)
    def set_Movie(self, value):
        """
        Set the value of the Movie input for this Choreo. ((optional, string) The URL or ID for an Open Graph object representing a movie.)
        """
        super(UpdateWantsToWatchInputSet, self)._set_input('Movie', value)
    def set_Other(self, value):
        """
        Set the value of the Other input for this Choreo. ((optional, string) The URL or ID for an Open Graph object representing any general video content.)
        """
        super(UpdateWantsToWatchInputSet, self)._set_input('Other', value)
    def set_Place(self, value):
        """
        Set the value of the Place input for this Choreo. ((optional, string) The URL or ID for an Open Graph object representing the location associated with this action.)
        """
        super(UpdateWantsToWatchInputSet, self)._set_input('Place', value)
    def set_TVShow(self, value):
        """
        Set the value of the TVShow input for this Choreo. ((optional, string) The URL or ID for an Open Graph object representing a TV show.)
        """
        super(UpdateWantsToWatchInputSet, self)._set_input('TVShow', value)
    def set_Tags(self, value):
        """
        Set the value of the Tags input for this Choreo. ((optional, string) A comma separated list of other profile IDs that also performed this action.)
        """
        super(UpdateWantsToWatchInputSet, self)._set_input('Tags', value)

class UpdateWantsToWatchResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateWantsToWatch Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Facebook.)
        """
        return self._output.get('Response', None)

class UpdateWantsToWatchChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UpdateWantsToWatchResultSet(response, path)
