# -*- coding: utf-8 -*-

###############################################################################
#
# ListBatchUnsubscribeCSV
# Unsubscribes one or more members listed in a CSV file from a MailChimp list.
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

class ListBatchUnsubscribeCSV(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListBatchUnsubscribeCSV Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ListBatchUnsubscribeCSV, self).__init__(temboo_session, '/Library/MailChimp/ListBatchUnsubscribeCSV')


    def new_input_set(self):
        return ListBatchUnsubscribeCSVInputSet()

    def _make_result_set(self, result, path):
        return ListBatchUnsubscribeCSVResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListBatchUnsubscribeCSVChoreographyExecution(session, exec_id, path)

class ListBatchUnsubscribeCSVInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListBatchUnsubscribeCSV
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_CSVFile(self, value):
        """
        Set the value of the CSVFile input for this Choreo. ((conditional, multiline) The list of subscriber email addresses to unsubscribe in CSV format.)
        """
        super(ListBatchUnsubscribeCSVInputSet, self)._set_input('CSVFile', value)
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Mailchimp)
        """
        super(ListBatchUnsubscribeCSVInputSet, self)._set_input('APIKey', value)
    def set_DeleteMember(self, value):
        """
        Set the value of the DeleteMember input for this Choreo. ((optional, boolean) A flag used to completely delete the member from your list instead of just unsubscribing. Specify '1' (true) or '0' (false). Defaults to 0.)
        """
        super(ListBatchUnsubscribeCSVInputSet, self)._set_input('DeleteMember', value)
    def set_ListId(self, value):
        """
        Set the value of the ListId input for this Choreo. ((required, string) The id of the Mailchimp list associated with the email addresses to unsubscribe.)
        """
        super(ListBatchUnsubscribeCSVInputSet, self)._set_input('ListId', value)
    def set_SendGoodbye(self, value):
        """
        Set the value of the SendGoodbye input for this Choreo. ((optional, boolean) A flag used to send the goodbye email to the email address. Specify '1' (true) or '0' (false). Defaults to 0.)
        """
        super(ListBatchUnsubscribeCSVInputSet, self)._set_input('SendGoodbye', value)
    def set_SendNotify(self, value):
        """
        Set the value of the SendNotify input for this Choreo. ((optional, boolean) A flag used to send the unsubscribe notification email to the address defined in the list email notification settings. Specify '1' (true) or '0' (false). Defaults to 0.)
        """
        super(ListBatchUnsubscribeCSVInputSet, self)._set_input('SendNotify', value)
    def set_SupressErrors(self, value):
        """
        Set the value of the SupressErrors input for this Choreo. ((optional, boolean) Whether or not to suppress errors that arise from attempting to unsubscribe an email address. Defaults to 0 (false). Set to 1 (true) to supress errors.)
        """
        super(ListBatchUnsubscribeCSVInputSet, self)._set_input('SupressErrors', value)


class ListBatchUnsubscribeCSVResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListBatchUnsubscribeCSV Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_ErrorList(self):
        """
        Retrieve the value for the "ErrorList" output from this Choreo execution. ((multiline) A list of emails that were not successfully unsubscribed.)
        """
        return self._output.get('ErrorList', None)
    def get_SuccessList(self):
        """
        Retrieve the value for the "SuccessList" output from this Choreo execution. ((multiline) A list of email successfully unsubscribed.)
        """
        return self._output.get('SuccessList', None)

class ListBatchUnsubscribeCSVChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ListBatchUnsubscribeCSVResultSet(response, path)
