# -*- coding: utf-8 -*-

###############################################################################
#
# AddMultipleContacts
# Creates multiple contacts in your Constant Contact list via the Activities bulk API.  The Choreo can use Excel or CSV files for the bulk upload.
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

class AddMultipleContacts(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the AddMultipleContacts Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(AddMultipleContacts, self).__init__(temboo_session, '/Library/ConstantContact/AddMultipleContacts')


    def new_input_set(self):
        return AddMultipleContactsInputSet()

    def _make_result_set(self, result, path):
        return AddMultipleContactsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AddMultipleContactsChoreographyExecution(session, exec_id, path)

class AddMultipleContactsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the AddMultipleContacts
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_FileContents(self, value):
        """
        Set the value of the FileContents input for this Choreo. ((conditional, multiline) The file contents of the list you want to upload. Should be in CSV format.)
        """
        super(AddMultipleContactsInputSet, self)._set_input('FileContents', value)
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Constant Contact.)
        """
        super(AddMultipleContactsInputSet, self)._set_input('APIKey', value)
    def set_ListId(self, value):
        """
        Set the value of the ListId input for this Choreo. ((required, integer) The numberic id for the list that you want to add contacts to.)
        """
        super(AddMultipleContactsInputSet, self)._set_input('ListId', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Constant Contact password.)
        """
        super(AddMultipleContactsInputSet, self)._set_input('Password', value)
    def set_UserName(self, value):
        """
        Set the value of the UserName input for this Choreo. ((required, string) Your Constant Contact username.)
        """
        super(AddMultipleContactsInputSet, self)._set_input('UserName', value)


class AddMultipleContactsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the AddMultipleContacts Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Constant Contact.)
        """
        return self._output.get('Response', None)

class AddMultipleContactsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return AddMultipleContactsResultSet(response, path)
