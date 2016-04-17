# -*- coding: utf-8 -*-

###############################################################################
#
# AddURL
# Add a document to an Instapaper account.
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

class AddURL(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the AddURL Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(AddURL, self).__init__(temboo_session, '/Library/Instapaper/AddURL')


    def new_input_set(self):
        return AddURLInputSet()

    def _make_result_set(self, result, path):
        return AddURLResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AddURLChoreographyExecution(session, exec_id, path)

class AddURLInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the AddURL
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Instapaper password.)
        """
        super(AddURLInputSet, self)._set_input('Password', value)
    def set_Selection(self, value):
        """
        Set the value of the Selection input for this Choreo. ((optional, string) Enter a description of the URL being added.)
        """
        super(AddURLInputSet, self)._set_input('Selection', value)
    def set_Title(self, value):
        """
        Set the value of the Title input for this Choreo. ((optional, string) Enter a titile for the uploaded URL. If no title is provided, Instapaper will crawl the URL to detect a title.)
        """
        super(AddURLInputSet, self)._set_input('Title', value)
    def set_URL(self, value):
        """
        Set the value of the URL input for this Choreo. ((required, string) Enter the URL of the document that is being added to an Instapaper account.)
        """
        super(AddURLInputSet, self)._set_input('URL', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) Your Instapaper username.)
        """
        super(AddURLInputSet, self)._set_input('Username', value)

class AddURLResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the AddURL Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((integer) The response from Instapaper. Successful reqests will return a 201 status code.)
        """
        return self._output.get('Response', None)

class AddURLChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return AddURLResultSet(response, path)
