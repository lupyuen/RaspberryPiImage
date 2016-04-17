# -*- coding: utf-8 -*-

###############################################################################
#
# GetTopTracks
# Retrieves the top tracks by an artist on Last.fm, ordered by popularity.
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

class GetTopTracks(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetTopTracks Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetTopTracks, self).__init__(temboo_session, '/Library/LastFm/Artist/GetTopTracks')


    def new_input_set(self):
        return GetTopTracksInputSet()

    def _make_result_set(self, result, path):
        return GetTopTracksResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetTopTracksChoreographyExecution(session, exec_id, path)

class GetTopTracksInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetTopTracks
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) Your Last.fm API Key.)
        """
        super(GetTopTracksInputSet, self)._set_input('APIKey', value)
    def set_Artist(self, value):
        """
        Set the value of the Artist input for this Choreo. ((conditional, string) The artist name. Required unless providing MbID.)
        """
        super(GetTopTracksInputSet, self)._set_input('Artist', value)
    def set_AutoCorrect(self, value):
        """
        Set the value of the AutoCorrect input for this Choreo. ((optional, boolean) Transform misspelled artist names into correct artist names. The corrected artist name will be returned in the response. Defaults to 0.)
        """
        super(GetTopTracksInputSet, self)._set_input('AutoCorrect', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) The number of results to fetch per page. Defaults to 50.)
        """
        super(GetTopTracksInputSet, self)._set_input('Limit', value)
    def set_MbID(self, value):
        """
        Set the value of the MbID input for this Choreo. ((conditional, string) The musicbrainz id for the artist. Required unless providing Artist.)
        """
        super(GetTopTracksInputSet, self)._set_input('MbID', value)
    def set_Page(self, value):
        """
        Set the value of the Page input for this Choreo. ((optional, integer) The page number to fetch. Defaults to 1.)
        """
        super(GetTopTracksInputSet, self)._set_input('Page', value)

class GetTopTracksResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetTopTracks Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Last.fm.)
        """
        return self._output.get('Response', None)

class GetTopTracksChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetTopTracksResultSet(response, path)
