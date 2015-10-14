# -*- coding: utf-8 -*-

###############################################################################
#
# MarkAsSpam
# Mark a post as spam.
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

class MarkAsSpam(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the MarkAsSpam Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(MarkAsSpam, self).__init__(temboo_session, '/Library/Disqus/Posts/MarkAsSpam')


    def new_input_set(self):
        return MarkAsSpamInputSet()

    def _make_result_set(self, result, path):
        return MarkAsSpamResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return MarkAsSpamChoreographyExecution(session, exec_id, path)

class MarkAsSpamInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the MarkAsSpam
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) A valid OAuth 2.0 access token.)
        """
        super(MarkAsSpamInputSet, self)._set_input('AccessToken', value)
    def set_PostID(self, value):
        """
        Set the value of the PostID input for this Choreo. ((required, integer) The post ID which is to be marked as spam.)
        """
        super(MarkAsSpamInputSet, self)._set_input('PostID', value)
    def set_PublicKey(self, value):
        """
        Set the value of the PublicKey input for this Choreo. ((required, string) The Public Key provided by Disqus (AKA the API Key).)
        """
        super(MarkAsSpamInputSet, self)._set_input('PublicKey', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and jsonp.)
        """
        super(MarkAsSpamInputSet, self)._set_input('ResponseFormat', value)


class MarkAsSpamResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the MarkAsSpam Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Disqus.)
        """
        return self._output.get('Response', None)

class MarkAsSpamChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return MarkAsSpamResultSet(response, path)
