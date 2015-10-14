# -*- coding: utf-8 -*-

###############################################################################
#
# ListUpdateMember
# Update information for a member of a MailChimp list.
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

class ListUpdateMember(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListUpdateMember Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ListUpdateMember, self).__init__(temboo_session, '/Library/MailChimp/ListUpdateMember')


    def new_input_set(self):
        return ListUpdateMemberInputSet()

    def _make_result_set(self, result, path):
        return ListUpdateMemberResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListUpdateMemberChoreographyExecution(session, exec_id, path)

class ListUpdateMemberInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListUpdateMember
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Mailchimp.)
        """
        super(ListUpdateMemberInputSet, self)._set_input('APIKey', value)
    def set_EmailAddress(self, value):
        """
        Set the value of the EmailAddress input for this Choreo. ((required, string) The current email address for the subscriber you want to update.)
        """
        super(ListUpdateMemberInputSet, self)._set_input('EmailAddress', value)
    def set_EmailType(self, value):
        """
        Set the value of the EmailType input for this Choreo. ((optional, string) Must be one of 'text', 'html', or 'mobile'. Defaults to html.)
        """
        super(ListUpdateMemberInputSet, self)._set_input('EmailType', value)
    def set_ListId(self, value):
        """
        Set the value of the ListId input for this Choreo. ((required, string) The id of the list that the existing subsbriber belongs to.)
        """
        super(ListUpdateMemberInputSet, self)._set_input('ListId', value)
    def set_Merge1(self, value):
        """
        Set the value of the Merge1 input for this Choreo. ((optional, string) Corresponds to the first merge var field defined in your account.)
        """
        super(ListUpdateMemberInputSet, self)._set_input('Merge1', value)
    def set_Merge2(self, value):
        """
        Set the value of the Merge2 input for this Choreo. ((optional, string) Corresponds to the second merge var field defined in your account.)
        """
        super(ListUpdateMemberInputSet, self)._set_input('Merge2', value)
    def set_Merge3(self, value):
        """
        Set the value of the Merge3 input for this Choreo. ((optional, string) Corresponds to the third merge var field defined in your account.)
        """
        super(ListUpdateMemberInputSet, self)._set_input('Merge3', value)
    def set_Merge4(self, value):
        """
        Set the value of the Merge4 input for this Choreo. ((optional, string) Corresponds to the fourth merge var field defined in your account.)
        """
        super(ListUpdateMemberInputSet, self)._set_input('Merge4', value)
    def set_NewEmail(self, value):
        """
        Set the value of the NewEmail input for this Choreo. ((optional, multiline) Set this to update the email address of a subscriber.)
        """
        super(ListUpdateMemberInputSet, self)._set_input('NewEmail', value)
    def set_ReplaceInterests(self, value):
        """
        Set the value of the ReplaceInterests input for this Choreo. ((optional, boolean) A flag to determine whether to replace the interest groups with the groups provided or add the provided groups to the member's interest groups. Specify '1' (true) or '0' (false). Defaults to 1.)
        """
        super(ListUpdateMemberInputSet, self)._set_input('ReplaceInterests', value)

class ListUpdateMemberResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListUpdateMember Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Mailchimp. Returns the string "true" for success and an error description for failures.)
        """
        return self._output.get('Response', None)

class ListUpdateMemberChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ListUpdateMemberResultSet(response, path)
