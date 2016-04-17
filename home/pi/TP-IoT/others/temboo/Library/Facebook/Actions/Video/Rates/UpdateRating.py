# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateRating
# Updates an existing video rating action.
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

class UpdateRating(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateRating Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(UpdateRating, self).__init__(temboo_session, '/Library/Facebook/Actions/Video/Rates/UpdateRating')


    def new_input_set(self):
        return UpdateRatingInputSet()

    def _make_result_set(self, result, path):
        return UpdateRatingResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateRatingChoreographyExecution(session, exec_id, path)

class UpdateRatingInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateRating
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved from the final step of the OAuth process.)
        """
        super(UpdateRatingInputSet, self)._set_input('AccessToken', value)
    def set_ActionID(self, value):
        """
        Set the value of the ActionID input for this Choreo. ((required, string) The id of the action to update.)
        """
        super(UpdateRatingInputSet, self)._set_input('ActionID', value)
    def set_EndTime(self, value):
        """
        Set the value of the EndTime input for this Choreo. ((optional, date) The time that the user ended the action (e.g. 2013-06-24T18:53:35+0000).)
        """
        super(UpdateRatingInputSet, self)._set_input('EndTime', value)
    def set_Episode(self, value):
        """
        Set the value of the Episode input for this Choreo. ((optional, string) The URL or ID for an Open Graph object representing an episode.)
        """
        super(UpdateRatingInputSet, self)._set_input('Episode', value)
    def set_ExpiresIn(self, value):
        """
        Set the value of the ExpiresIn input for this Choreo. ((optional, integer) The amount of time (in milliseconds) from the publish_time that the action will expire.)
        """
        super(UpdateRatingInputSet, self)._set_input('ExpiresIn', value)
    def set_Message(self, value):
        """
        Set the value of the Message input for this Choreo. ((optional, string) A message attached to this action. Setting this parameter requires enabling of message capabilities.)
        """
        super(UpdateRatingInputSet, self)._set_input('Message', value)
    def set_Movie(self, value):
        """
        Set the value of the Movie input for this Choreo. ((optional, string) The URL or ID for an Open Graph object representing a movie.)
        """
        super(UpdateRatingInputSet, self)._set_input('Movie', value)
    def set_Other(self, value):
        """
        Set the value of the Other input for this Choreo. ((optional, string) The URL or ID for an Open Graph object representing any general video content.)
        """
        super(UpdateRatingInputSet, self)._set_input('Other', value)
    def set_Place(self, value):
        """
        Set the value of the Place input for this Choreo. ((optional, string) The URL or ID for an Open Graph object representing the location associated with this action.)
        """
        super(UpdateRatingInputSet, self)._set_input('Place', value)
    def set_RatingNormalizedValue(self, value):
        """
        Set the value of the RatingNormalizedValue input for this Choreo. ((optional, decimal) The rating expressed as a decimal value between 0 and 1.0.)
        """
        super(UpdateRatingInputSet, self)._set_input('RatingNormalizedValue', value)
    def set_RatingScale(self, value):
        """
        Set the value of the RatingScale input for this Choreo. ((optional, integer) The highest possible value in the rating scale.)
        """
        super(UpdateRatingInputSet, self)._set_input('RatingScale', value)
    def set_RatingValue(self, value):
        """
        Set the value of the RatingValue input for this Choreo. ((optional, decimal) The value of the book rating.)
        """
        super(UpdateRatingInputSet, self)._set_input('RatingValue', value)
    def set_ReviewText(self, value):
        """
        Set the value of the ReviewText input for this Choreo. ((optional, string) The text content of the book review.)
        """
        super(UpdateRatingInputSet, self)._set_input('ReviewText', value)
    def set_Review(self, value):
        """
        Set the value of the Review input for this Choreo. ((optional, string) The URL or ID for an Open Graph object representing a book review.)
        """
        super(UpdateRatingInputSet, self)._set_input('Review', value)
    def set_TVShow(self, value):
        """
        Set the value of the TVShow input for this Choreo. ((optional, string) The URL or ID for an Open Graph object representing a TV show.)
        """
        super(UpdateRatingInputSet, self)._set_input('TVShow', value)
    def set_Tags(self, value):
        """
        Set the value of the Tags input for this Choreo. ((optional, string) A comma separated list of other profile IDs that also performed this action.)
        """
        super(UpdateRatingInputSet, self)._set_input('Tags', value)

class UpdateRatingResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateRating Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Facebook.)
        """
        return self._output.get('Response', None)

class UpdateRatingChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UpdateRatingResultSet(response, path)
