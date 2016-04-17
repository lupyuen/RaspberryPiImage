# -*- coding: utf-8 -*-

###############################################################################
#
# RenameItem
# Rename an item.
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

class RenameItem(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RenameItem Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(RenameItem, self).__init__(temboo_session, '/Library/FilesAnywhere/RenameItem')


    def new_input_set(self):
        return RenameItemInputSet()

    def _make_result_set(self, result, path):
        return RenameItemResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RenameItemChoreographyExecution(session, exec_id, path)

class RenameItemInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RenameItem
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((conditional, string) The API Key provided by FilesAnywhere. Required unless supplying a valid Token input.)
        """
        super(RenameItemInputSet, self)._set_input('APIKey', value)
    def set_NewName(self, value):
        """
        Set the value of the NewName input for this Choreo. ((required, string) Enter the new name for the item.)
        """
        super(RenameItemInputSet, self)._set_input('NewName', value)
    def set_OrgID(self, value):
        """
        Set the value of the OrgID input for this Choreo. ((conditional, integer) Defaults to 0 for a FilesAnywhere Web account.  Use 50 for a FilesAnywhere WebAdvanced account.)
        """
        super(RenameItemInputSet, self)._set_input('OrgID', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((conditional, password) Your FilesAnywhere password. Required unless supplying a valid Token input.)
        """
        super(RenameItemInputSet, self)._set_input('Password', value)
    def set_Path(self, value):
        """
        Set the value of the Path input for this Choreo. ((required, string) The path to the file you want to rename (i.e. \JOHNSMITH\MyFolder\MyFile.txt).)
        """
        super(RenameItemInputSet, self)._set_input('Path', value)
    def set_Token(self, value):
        """
        Set the value of the Token input for this Choreo. ((conditional, string) If provided, the Choreo will use the token to authenticate. If the token is expired or not provided, the Choreo will relogin and retrieve a new token when APIKey, Username, and Password are supplied.)
        """
        super(RenameItemInputSet, self)._set_input('Token', value)
    def set_Type(self, value):
        """
        Set the value of the Type input for this Choreo. ((required, string) Specify the type of file being renamed by entering: folder, OR, file.)
        """
        super(RenameItemInputSet, self)._set_input('Type', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((conditional, string) Your FilesAnywhere username. Required unless supplying a valid Token input.)
        """
        super(RenameItemInputSet, self)._set_input('Username', value)

class RenameItemResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RenameItem Choreo.
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

class RenameItemChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return RenameItemResultSet(response, path)
