# -*- coding: utf-8 -*-

###############################################################################
#
# CreateTag
# Creates a tag object.
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

class CreateTag(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateTag Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CreateTag, self).__init__(temboo_session, '/Library/GitHub/GitDataAPI/Tags/CreateTag')


    def new_input_set(self):
        return CreateTagInputSet()

    def _make_result_set(self, result, path):
        return CreateTagResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateTagChoreographyExecution(session, exec_id, path)

class CreateTagInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateTag
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        super(CreateTagInputSet, self)._set_input('AccessToken', value)
    def set_Message(self, value):
        """
        Set the value of the Message input for this Choreo. ((required, string) The tag message.)
        """
        super(CreateTagInputSet, self)._set_input('Message', value)
    def set_Object(self, value):
        """
        Set the value of the Object input for this Choreo. ((required, string) The SHA of the git object that is being tagged.)
        """
        super(CreateTagInputSet, self)._set_input('Object', value)
    def set_Repo(self, value):
        """
        Set the value of the Repo input for this Choreo. ((required, string) The name of the repo associated with the tag being created.)
        """
        super(CreateTagInputSet, self)._set_input('Repo', value)
    def set_Tag(self, value):
        """
        Set the value of the Tag input for this Choreo. ((required, string) A string to use for the tag (i.e. v0.0.1).)
        """
        super(CreateTagInputSet, self)._set_input('Tag', value)
    def set_TaggerDate(self, value):
        """
        Set the value of the TaggerDate input for this Choreo. ((required, date) A timestamp of when the object is tagged. Should be formatted like: 2011-06-17T14:53:35-07:00.)
        """
        super(CreateTagInputSet, self)._set_input('TaggerDate', value)
    def set_TaggerEmail(self, value):
        """
        Set the value of the TaggerEmail input for this Choreo. ((required, string) The email of the author of the tag.)
        """
        super(CreateTagInputSet, self)._set_input('TaggerEmail', value)
    def set_TaggerName(self, value):
        """
        Set the value of the TaggerName input for this Choreo. ((required, string) The name of the author of the tag.)
        """
        super(CreateTagInputSet, self)._set_input('TaggerName', value)
    def set_Type(self, value):
        """
        Set the value of the Type input for this Choreo. ((required, string) The type of object that is being tagged. Valid values are: commit, tree, or blob.)
        """
        super(CreateTagInputSet, self)._set_input('Type', value)
    def set_User(self, value):
        """
        Set the value of the User input for this Choreo. ((required, string) The GitHub username.)
        """
        super(CreateTagInputSet, self)._set_input('User', value)

class CreateTagResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateTag Choreo.
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

class CreateTagChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CreateTagResultSet(response, path)
