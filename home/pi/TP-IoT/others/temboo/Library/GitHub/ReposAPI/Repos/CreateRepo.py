# -*- coding: utf-8 -*-

###############################################################################
#
# CreateRepo
# Creates a new repository for the authenticated user.
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

class CreateRepo(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateRepo Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CreateRepo, self).__init__(temboo_session, '/Library/GitHub/ReposAPI/Repos/CreateRepo')


    def new_input_set(self):
        return CreateRepoInputSet()

    def _make_result_set(self, result, path):
        return CreateRepoResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateRepoChoreographyExecution(session, exec_id, path)

class CreateRepoInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateRepo
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        super(CreateRepoInputSet, self)._set_input('AccessToken', value)
    def set_Description(self, value):
        """
        Set the value of the Description input for this Choreo. ((optional, string) A text description for the repo.)
        """
        super(CreateRepoInputSet, self)._set_input('Description', value)
    def set_HasDownloads(self, value):
        """
        Set the value of the HasDownloads input for this Choreo. ((optional, boolean) Se to "true" to enable downloads for this repository. Defaults to "true".)
        """
        super(CreateRepoInputSet, self)._set_input('HasDownloads', value)
    def set_HasIssues(self, value):
        """
        Set the value of the HasIssues input for this Choreo. ((optional, boolean) Set to "true" to enable issues for this repository. Defaults to "true.")
        """
        super(CreateRepoInputSet, self)._set_input('HasIssues', value)
    def set_HasWiki(self, value):
        """
        Set the value of the HasWiki input for this Choreo. ((optional, boolean) Set to "true" to enable the wiki for this repository. Defaults to "true".)
        """
        super(CreateRepoInputSet, self)._set_input('HasWiki', value)
    def set_Homepage(self, value):
        """
        Set the value of the Homepage input for this Choreo. ((optional, string) A homepage link.)
        """
        super(CreateRepoInputSet, self)._set_input('Homepage', value)
    def set_Name(self, value):
        """
        Set the value of the Name input for this Choreo. ((required, string) The name of the repo being created.)
        """
        super(CreateRepoInputSet, self)._set_input('Name', value)
    def set_Private(self, value):
        """
        Set the value of the Private input for this Choreo. ((optional, boolean) A flag indicating the the repo is private or public. Set to "true" to create a private repository. Defaults to "false".)
        """
        super(CreateRepoInputSet, self)._set_input('Private', value)
    def set_TeamID(self, value):
        """
        Set the value of the TeamID input for this Choreo. ((optional, integer) The id of the team that will be granted access to this repository. Only valid when creating a repo in an organization.)
        """
        super(CreateRepoInputSet, self)._set_input('TeamID', value)

class CreateRepoResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateRepo Choreo.
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

class CreateRepoChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CreateRepoResultSet(response, path)
