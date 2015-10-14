# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteItem
# Deletes a file from a specified directory in your FilesAnywhere account.
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

class DeleteItem(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteItem Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(DeleteItem, self).__init__(temboo_session, '/Library/FilesAnywhere/DeleteItem')


    def new_input_set(self):
        return DeleteItemInputSet()

    def _make_result_set(self, result, path):
        return DeleteItemResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteItemChoreographyExecution(session, exec_id, path)

class DeleteItemInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteItem
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((conditional, string) The API Key provided by FilesAnywhere. Required unless supplying a valid Token input.)
        """
        super(DeleteItemInputSet, self)._set_input('APIKey', value)
    def set_OrgID(self, value):
        """
        Set the value of the OrgID input for this Choreo. ((conditional, integer) Defaults to 0 for a FilesAnywhere Web account.  Use 50 for a FilesAnywhere WebAdvanced account.)
        """
        super(DeleteItemInputSet, self)._set_input('OrgID', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((conditional, password) Your FilesAnywhere password. Required unless supplying a valid Token input.)
        """
        super(DeleteItemInputSet, self)._set_input('Password', value)
    def set_Path(self, value):
        """
        Set the value of the Path input for this Choreo. ((required, string) The path to the file you want to delete (i.e. \JOHNSMITH\MyFolder\MyFile.txt).)
        """
        super(DeleteItemInputSet, self)._set_input('Path', value)
    def set_Token(self, value):
        """
        Set the value of the Token input for this Choreo. ((conditional, string) If provided, the Choreo will use the token to authenticate. If the token is expired or not provided, the Choreo will relogin and retrieve a new token when APIKey, Username, and Password are supplied.)
        """
        super(DeleteItemInputSet, self)._set_input('Token', value)
    def set_Type(self, value):
        """
        Set the value of the Type input for this Choreo. ((optional, string) The type of item you are deleting. Can be set to 'file' or 'folder'. Defaults to 'file'.)
        """
        super(DeleteItemInputSet, self)._set_input('Type', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((conditional, string) Your FilesAnywhere username. Required unless supplying a valid Token input.)
        """
        super(DeleteItemInputSet, self)._set_input('Username', value)

class DeleteItemResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteItem Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from FilesAnywhere.)
        """
        return self._output.get('Response', None)
    def get_Token(self):
        """
        Retrieve the value for the "Token" output from this Choreo execution. ((conditional, string) If provided, the Choreo will use the token to authenticate. If the token is expired or not provided, the Choreo will relogin and retrieve a new token when APIKey, Username, and Password are supplied.)
        """
        return self._output.get('Token', None)

class DeleteItemChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return DeleteItemResultSet(response, path)
