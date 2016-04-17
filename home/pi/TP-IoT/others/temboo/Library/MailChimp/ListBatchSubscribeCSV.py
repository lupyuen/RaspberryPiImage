# -*- coding: utf-8 -*-

###############################################################################
#
# ListBatchSubscribeCSV
# Adds or updates multiple subscribers in a given CSV file.
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

class ListBatchSubscribeCSV(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListBatchSubscribeCSV Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ListBatchSubscribeCSV, self).__init__(temboo_session, '/Library/MailChimp/ListBatchSubscribeCSV')


    def new_input_set(self):
        return ListBatchSubscribeCSVInputSet()

    def _make_result_set(self, result, path):
        return ListBatchSubscribeCSVResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListBatchSubscribeCSVChoreographyExecution(session, exec_id, path)

class ListBatchSubscribeCSVInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListBatchSubscribeCSV
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_CSVFile(self, value):
        """
        Set the value of the CSVFile input for this Choreo. ((conditional, multiline) The list of subscriber email addresses to unsubscribe in CSV format.)
        """
        super(ListBatchSubscribeCSVInputSet, self)._set_input('CSVFile', value)
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Mailchimp)
        """
        super(ListBatchSubscribeCSVInputSet, self)._set_input('APIKey', value)
    def set_DoubleOptIn(self, value):
        """
        Set the value of the DoubleOptIn input for this Choreo. ((conditional, boolean) Flag to control whether a double opt-in confirmation message is sent. Specify '1' (true) or '0' (false). Defaults to 0.)
        """
        super(ListBatchSubscribeCSVInputSet, self)._set_input('DoubleOptIn', value)
    def set_EmailType(self, value):
        """
        Set the value of the EmailType input for this Choreo. ((optional, string) Must be one of 'text', 'html', or 'mobile'. Defaults to html.)
        """
        super(ListBatchSubscribeCSVInputSet, self)._set_input('EmailType', value)
    def set_ListId(self, value):
        """
        Set the value of the ListId input for this Choreo. ((required, string) The id of the Mailchimp list associated with the email addresses to subscribe.)
        """
        super(ListBatchSubscribeCSVInputSet, self)._set_input('ListId', value)
    def set_ReplaceInterests(self, value):
        """
        Set the value of the ReplaceInterests input for this Choreo. ((optional, boolean) A flag to determine whether to replace the interest groups with the groups provided or add the provided groups to the member's interest groups. Specify '1' (true) or '0' (false). Defaults to 1.)
        """
        super(ListBatchSubscribeCSVInputSet, self)._set_input('ReplaceInterests', value)
    def set_SupressErrors(self, value):
        """
        Set the value of the SupressErrors input for this Choreo. ((optional, boolean) Whether or not to suppress errors that arise from attempting to add/update a subscriber. Defaults to 0 (false). Set to 1 (true) to supress errors.)
        """
        super(ListBatchSubscribeCSVInputSet, self)._set_input('SupressErrors', value)
    def set_UpdateExisting(self, value):
        """
        Set the value of the UpdateExisting input for this Choreo. ((conditional, boolean) Indicates that if the email already exists, this request will perform an update instead of an insert. Specify '1' (true) or '0' (false). Defaults to 1.)
        """
        super(ListBatchSubscribeCSVInputSet, self)._set_input('UpdateExisting', value)


class ListBatchSubscribeCSVResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListBatchSubscribeCSV Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_ErrorList(self):
        """
        Retrieve the value for the "ErrorList" output from this Choreo execution. ((multiline) A list of emails that were not successfully subscribed.)
        """
        return self._output.get('ErrorList', None)
    def get_SuccessList(self):
        """
        Retrieve the value for the "SuccessList" output from this Choreo execution. ((multiline) A list of email successfully subscribed.)
        """
        return self._output.get('SuccessList', None)

class ListBatchSubscribeCSVChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ListBatchSubscribeCSVResultSet(response, path)
