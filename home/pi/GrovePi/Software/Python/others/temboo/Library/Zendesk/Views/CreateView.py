# -*- coding: utf-8 -*-

###############################################################################
#
# CreateView
# Creates a new view.
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

class CreateView(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateView Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CreateView, self).__init__(temboo_session, '/Library/Zendesk/Views/CreateView')


    def new_input_set(self):
        return CreateViewInputSet()

    def _make_result_set(self, result, path):
        return CreateViewResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateViewChoreographyExecution(session, exec_id, path)

class CreateViewInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateView
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AllConditions(self, value):
        """
        Set the value of the AllConditions input for this Choreo. ((conditional, json) JSON Array of conditions.  Tickets must fulfill all of the conditions to be considered matching.)
        """
        super(CreateViewInputSet, self)._set_input('AllConditions', value)
    def set_AnyConditions(self, value):
        """
        Set the value of the AnyConditions input for this Choreo. ((conditional, json) JSON Array of conditions.  Tickets may fulfill any of the conditions to be considered matching.)
        """
        super(CreateViewInputSet, self)._set_input('AnyConditions', value)
    def set_Email(self, value):
        """
        Set the value of the Email input for this Choreo. ((required, string) The email address you use to login to your Zendesk account.)
        """
        super(CreateViewInputSet, self)._set_input('Email', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Zendesk password.)
        """
        super(CreateViewInputSet, self)._set_input('Password', value)
    def set_Server(self, value):
        """
        Set the value of the Server input for this Choreo. ((required, string) Your Zendesk domain and subdomain (e.g., temboocare.zendesk.com).)
        """
        super(CreateViewInputSet, self)._set_input('Server', value)
    def set_Title(self, value):
        """
        Set the value of the Title input for this Choreo. ((required, string) Title of the view to be created.)
        """
        super(CreateViewInputSet, self)._set_input('Title', value)

class CreateViewResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateView Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Zendesk.)
        """
        return self._output.get('Response', None)

class CreateViewChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CreateViewResultSet(response, path)
