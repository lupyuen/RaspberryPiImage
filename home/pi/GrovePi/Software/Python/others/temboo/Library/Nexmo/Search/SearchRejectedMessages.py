# -*- coding: utf-8 -*-

###############################################################################
#
# SearchRejectedMessages
# Search for a previously sent message by Message ID.  Note that a sent message won't be immediately available for search.
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

class SearchRejectedMessages(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SearchRejectedMessages Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(SearchRejectedMessages, self).__init__(temboo_session, '/Library/Nexmo/Search/SearchRejectedMessages')


    def new_input_set(self):
        return SearchRejectedMessagesInputSet()

    def _make_result_set(self, result, path):
        return SearchRejectedMessagesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchRejectedMessagesChoreographyExecution(session, exec_id, path)

class SearchRejectedMessagesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SearchRejectedMessages
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) Your API Key provided to you by Nexmo.)
        """
        super(SearchRejectedMessagesInputSet, self)._set_input('APIKey', value)
    def set_APISecret(self, value):
        """
        Set the value of the APISecret input for this Choreo. ((required, string) Your API Secret provided to you by Nexmo.)
        """
        super(SearchRejectedMessagesInputSet, self)._set_input('APISecret', value)
    def set_Date(self, value):
        """
        Set the value of the Date input for this Choreo. ((required, string) Date message was sent in the form of YYYY-MM-DD. (e.g. 2013-07-01))
        """
        super(SearchRejectedMessagesInputSet, self)._set_input('Date', value)
    def set_MessageID(self, value):
        """
        Set the value of the MessageID input for this Choreo. ((required, string) Your Message ID.)
        """
        super(SearchRejectedMessagesInputSet, self)._set_input('MessageID', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "json" (the default) and "xml".)
        """
        super(SearchRejectedMessagesInputSet, self)._set_input('ResponseFormat', value)
    def set_To(self, value):
        """
        Set the value of the To input for this Choreo. ((required, string) The recipient's phone number.  (e.g. 123456780))
        """
        super(SearchRejectedMessagesInputSet, self)._set_input('To', value)

class SearchRejectedMessagesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SearchRejectedMessages Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Nexmo. Corresponds to the ResponseFormat input. Defaults to json.)
        """
        return self._output.get('Response', None)

class SearchRejectedMessagesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return SearchRejectedMessagesResultSet(response, path)
