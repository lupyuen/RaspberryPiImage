# -*- coding: utf-8 -*-

###############################################################################
#
# CreateIdentity
# Create a new identity.
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

class CreateIdentity(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateIdentity Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CreateIdentity, self).__init__(temboo_session, '/Library/SendGrid/NewsletterAPI/Identity/CreateIdentity')


    def new_input_set(self):
        return CreateIdentityInputSet()

    def _make_result_set(self, result, path):
        return CreateIdentityResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateIdentityChoreographyExecution(session, exec_id, path)

class CreateIdentityInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateIdentity
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key obtained from SendGrid.)
        """
        super(CreateIdentityInputSet, self)._set_input('APIKey', value)
    def set_APIUser(self, value):
        """
        Set the value of the APIUser input for this Choreo. ((required, string) The username registered with SendGrid. )
        """
        super(CreateIdentityInputSet, self)._set_input('APIUser', value)
    def set_Address(self, value):
        """
        Set the value of the Address input for this Choreo. ((required, string) The physical address to be used for this Identity.)
        """
        super(CreateIdentityInputSet, self)._set_input('Address', value)
    def set_City(self, value):
        """
        Set the value of the City input for this Choreo. ((required, string) The city for this Identity.)
        """
        super(CreateIdentityInputSet, self)._set_input('City', value)
    def set_Country(self, value):
        """
        Set the value of the Country input for this Choreo. ((required, string) The country to be associated with this Identity.)
        """
        super(CreateIdentityInputSet, self)._set_input('Country', value)
    def set_Email(self, value):
        """
        Set the value of the Email input for this Choreo. ((required, string) The email address to be used for this identity.)
        """
        super(CreateIdentityInputSet, self)._set_input('Email', value)
    def set_Identity(self, value):
        """
        Set the value of the Identity input for this Choreo. ((required, string) The name for this identity.)
        """
        super(CreateIdentityInputSet, self)._set_input('Identity', value)
    def set_Name(self, value):
        """
        Set the value of the Name input for this Choreo. ((required, string) Enter the name to be associated with this identity.)
        """
        super(CreateIdentityInputSet, self)._set_input('Name', value)
    def set_ReplyTo(self, value):
        """
        Set the value of the ReplyTo input for this Choreo. ((required, string) An email address to be used in the Reply-To field.)
        """
        super(CreateIdentityInputSet, self)._set_input('ReplyTo', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format of the response from SendGrid.  Specify json, or xml.  Default is set to json.)
        """
        super(CreateIdentityInputSet, self)._set_input('ResponseFormat', value)
    def set_State(self, value):
        """
        Set the value of the State input for this Choreo. ((required, string) The state to be associated with this Identity.)
        """
        super(CreateIdentityInputSet, self)._set_input('State', value)
    def set_Zip(self, value):
        """
        Set the value of the Zip input for this Choreo. ((required, integer) The zip code associated with this Identity.)
        """
        super(CreateIdentityInputSet, self)._set_input('Zip', value)


class CreateIdentityResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateIdentity Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from SendGrid. The format corresponds to the ResponseFormat input. Default is json.)
        """
        return self._output.get('Response', None)

class CreateIdentityChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CreateIdentityResultSet(response, path)
