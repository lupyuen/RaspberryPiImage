# -*- coding: utf-8 -*-

###############################################################################
#
# CompareCommits
# Retrieves a comparison between two commits.
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

class CompareCommits(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CompareCommits Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CompareCommits, self).__init__(temboo_session, '/Library/GitHub/ReposAPI/Commits/CompareCommits')


    def new_input_set(self):
        return CompareCommitsInputSet()

    def _make_result_set(self, result, path):
        return CompareCommitsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CompareCommitsChoreographyExecution(session, exec_id, path)

class CompareCommitsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CompareCommits
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((conditional, string) The Access Token retrieved during the OAuth process. Required when accessing a protected resource.)
        """
        super(CompareCommitsInputSet, self)._set_input('AccessToken', value)
    def set_Base(self, value):
        """
        Set the value of the Base input for this Choreo. ((required, string) The base commit (i.e. "master").)
        """
        super(CompareCommitsInputSet, self)._set_input('Base', value)
    def set_Head(self, value):
        """
        Set the value of the Head input for this Choreo. ((required, string) The head commit.)
        """
        super(CompareCommitsInputSet, self)._set_input('Head', value)
    def set_Repo(self, value):
        """
        Set the value of the Repo input for this Choreo. ((required, string) The name of the repository.)
        """
        super(CompareCommitsInputSet, self)._set_input('Repo', value)
    def set_User(self, value):
        """
        Set the value of the User input for this Choreo. ((required, string) The GitHub username.)
        """
        super(CompareCommitsInputSet, self)._set_input('User', value)

class CompareCommitsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CompareCommits Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from GitHub.)
        """
        return self._output.get('Response', None)
    def get_Limit(self):
        """
        Retrieve the value for the "Limit" output from this Choreo execution. ((integer) The available rate limit for your account. This is returned in the GitHub response header.)
        """
        return self._output.get('Limit', None)
    def get_Remaining(self):
        """
        Retrieve the value for the "Remaining" output from this Choreo execution. ((integer) The remaining number of API requests available to you. This is returned in the GitHub response header.)
        """
        return self._output.get('Remaining', None)

class CompareCommitsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CompareCommitsResultSet(response, path)
