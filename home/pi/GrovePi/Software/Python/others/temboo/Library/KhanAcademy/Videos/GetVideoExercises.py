# -*- coding: utf-8 -*-

###############################################################################
#
# GetVideoExercises
# Retrieves all the exercises associated with a given video.
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

class GetVideoExercises(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetVideoExercises Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetVideoExercises, self).__init__(temboo_session, '/Library/KhanAcademy/Videos/GetVideoExercises')


    def new_input_set(self):
        return GetVideoExercisesInputSet()

    def _make_result_set(self, result, path):
        return GetVideoExercisesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetVideoExercisesChoreographyExecution(session, exec_id, path)

class GetVideoExercisesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetVideoExercises
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_YouTubeID(self, value):
        """
        Set the value of the YouTubeID input for this Choreo. ((required, string) The Youtube ID of the video for which you want data.)
        """
        super(GetVideoExercisesInputSet, self)._set_input('YouTubeID', value)

class GetVideoExercisesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetVideoExercises Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Khan Academy.)
        """
        return self._output.get('Response', None)

class GetVideoExercisesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetVideoExercisesResultSet(response, path)
