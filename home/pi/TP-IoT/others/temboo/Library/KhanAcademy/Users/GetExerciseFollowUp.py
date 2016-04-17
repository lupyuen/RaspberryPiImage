# -*- coding: utf-8 -*-

###############################################################################
#
# GetExerciseFollowUp
# Retrieves user data about all excercises which have the specified excercise as a prerequisite.
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

class GetExerciseFollowUp(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetExerciseFollowUp Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetExerciseFollowUp, self).__init__(temboo_session, '/Library/KhanAcademy/Users/GetExerciseFollowUp')


    def new_input_set(self):
        return GetExerciseFollowUpInputSet()

    def _make_result_set(self, result, path):
        return GetExerciseFollowUpResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetExerciseFollowUpChoreographyExecution(session, exec_id, path)

class GetExerciseFollowUpInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetExerciseFollowUp
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_ConsumerKey(self, value):
        """
        Set the value of the ConsumerKey input for this Choreo. ((required, string) The Consumer Key provided by Khan Academy.)
        """
        super(GetExerciseFollowUpInputSet, self)._set_input('ConsumerKey', value)
    def set_ConsumerSecret(self, value):
        """
        Set the value of the ConsumerSecret input for this Choreo. ((required, string) The OAuth Consumer Secret provided by Khan Academy.)
        """
        super(GetExerciseFollowUpInputSet, self)._set_input('ConsumerSecret', value)
    def set_Email(self, value):
        """
        Set the value of the Email input for this Choreo. ((optional, string) The email address (coach or student ID) of user. If not provided, defaults to currently logged in user.)
        """
        super(GetExerciseFollowUpInputSet, self)._set_input('Email', value)
    def set_ExerciseName(self, value):
        """
        Set the value of the ExerciseName input for this Choreo. ((required, string) The exercise for which you want to retrieve follwow up exercises (e.g. "simplifying_fractions").)
        """
        super(GetExerciseFollowUpInputSet, self)._set_input('ExerciseName', value)
    def set_OAuthTokenSecret(self, value):
        """
        Set the value of the OAuthTokenSecret input for this Choreo. ((required, string) The OAuth Token Secret retrieved during the OAuth process.)
        """
        super(GetExerciseFollowUpInputSet, self)._set_input('OAuthTokenSecret', value)
    def set_OAuthToken(self, value):
        """
        Set the value of the OAuthToken input for this Choreo. ((required, string) The OAuth Token retrieved during the OAuth process.)
        """
        super(GetExerciseFollowUpInputSet, self)._set_input('OAuthToken', value)

class GetExerciseFollowUpResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetExerciseFollowUp Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Khan Academy.)
        """
        return self._output.get('Response', None)

class GetExerciseFollowUpChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetExerciseFollowUpResultSet(response, path)
