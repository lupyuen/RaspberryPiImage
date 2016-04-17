# -*- coding: utf-8 -*-

###############################################################################
#
# CompanyShare
# Posts shared comment on a company page.
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

class CompanyShare(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CompanyShare Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CompanyShare, self).__init__(temboo_session, '/Library/LinkedIn/Companies/CompanyShare')


    def new_input_set(self):
        return CompanyShareInputSet()

    def _make_result_set(self, result, path):
        return CompanyShareResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CompanyShareChoreographyExecution(session, exec_id, path)

class CompanyShareInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CompanyShare
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by LinkedIn (AKA the Client ID).)
        """
        super(CompanyShareInputSet, self)._set_input('APIKey', value)
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret retrieved during the OAuth process (AKA the OAuth User Secret).)
        """
        super(CompanyShareInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process (AKA the OAuth User Token).)
        """
        super(CompanyShareInputSet, self)._set_input('AccessToken', value)
    def set_Comment(self, value):
        """
        Set the value of the Comment input for this Choreo. ((conditional, string) A comment by the member to associated with the share. If this is not provided, you must specify the SubmittedURL.)
        """
        super(CompanyShareInputSet, self)._set_input('Comment', value)
    def set_CompanyID(self, value):
        """
        Set the value of the CompanyID input for this Choreo. ((required, integer) A LinkedIn assigned ID associated with the company.)
        """
        super(CompanyShareInputSet, self)._set_input('CompanyID', value)
    def set_Description(self, value):
        """
        Set the value of the Description input for this Choreo. ((optional, string) The description of the content being shared.)
        """
        super(CompanyShareInputSet, self)._set_input('Description', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: xml (the default) and json.)
        """
        super(CompanyShareInputSet, self)._set_input('ResponseFormat', value)
    def set_SecretKey(self, value):
        """
        Set the value of the SecretKey input for this Choreo. ((required, string) The Secret Key provided by LinkedIn (AKA the Client Secret).)
        """
        super(CompanyShareInputSet, self)._set_input('SecretKey', value)
    def set_SharedTargetCode(self, value):
        """
        Set the value of the SharedTargetCode input for this Choreo. ((optional, string) A shared target code used to ensure that the shared content reaches a specific audience.)
        """
        super(CompanyShareInputSet, self)._set_input('SharedTargetCode', value)
    def set_SharedTargetValue(self, value):
        """
        Set the value of the SharedTargetValue input for this Choreo. ((optional, string) The name of the shared target used to ensure that the shared content reaches a specific audience.)
        """
        super(CompanyShareInputSet, self)._set_input('SharedTargetValue', value)
    def set_SubmittedImageURL(self, value):
        """
        Set the value of the SubmittedImageURL input for this Choreo. ((optional, string) A fully qualified URL to a thumbnail image to accompany the shared content.)
        """
        super(CompanyShareInputSet, self)._set_input('SubmittedImageURL', value)
    def set_SubmittedURL(self, value):
        """
        Set the value of the SubmittedURL input for this Choreo. ((optional, string) A fully qualified URL for the content being shared.)
        """
        super(CompanyShareInputSet, self)._set_input('SubmittedURL', value)
    def set_Title(self, value):
        """
        Set the value of the Title input for this Choreo. ((optional, string) The title of the content being shared.)
        """
        super(CompanyShareInputSet, self)._set_input('Title', value)
    def set_Visibility(self, value):
        """
        Set the value of the Visibility input for this Choreo. ((required, string) The visibility setting of the share. Valid values are: anyone, connections-only.)
        """
        super(CompanyShareInputSet, self)._set_input('Visibility', value)

class CompanyShareResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CompanyShare Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from LinkedIn.)
        """
        return self._output.get('Response', None)

class CompanyShareChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CompanyShareResultSet(response, path)
