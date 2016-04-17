# -*- coding: utf-8 -*-

###############################################################################
#
# CreateGist
# Creates a gist.
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

class CreateGist(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateGist Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CreateGist, self).__init__(temboo_session, '/Library/GitHub/GistsAPI/Gists/CreateGist')


    def new_input_set(self):
        return CreateGistInputSet()

    def _make_result_set(self, result, path):
        return CreateGistResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateGistChoreographyExecution(session, exec_id, path)

class CreateGistInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateGist
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        super(CreateGistInputSet, self)._set_input('AccessToken', value)
    def set_Description(self, value):
        """
        Set the value of the Description input for this Choreo. ((optional, string) The description for this gist.)
        """
        super(CreateGistInputSet, self)._set_input('Description', value)
    def set_FileContents(self, value):
        """
        Set the value of the FileContents input for this Choreo. ((required, string) The file contents of the gist.)
        """
        super(CreateGistInputSet, self)._set_input('FileContents', value)
    def set_FileName(self, value):
        """
        Set the value of the FileName input for this Choreo. ((required, string) The file name of the gist (i.e. myProject.py).)
        """
        super(CreateGistInputSet, self)._set_input('FileName', value)
    def set_Public(self, value):
        """
        Set the value of the Public input for this Choreo. ((required, boolean) Indicates whether or not the gist is public or private.)
        """
        super(CreateGistInputSet, self)._set_input('Public', value)
    def set_User(self, value):
        """
        Set the value of the User input for this Choreo. ((required, string) Deprecated (retained for backward compatibility only).)
        """
        super(CreateGistInputSet, self)._set_input('User', value)

class CreateGistResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateGist Choreo.
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

class CreateGistChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CreateGistResultSet(response, path)
