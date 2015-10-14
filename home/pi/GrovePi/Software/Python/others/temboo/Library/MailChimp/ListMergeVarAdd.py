# -*- coding: utf-8 -*-

###############################################################################
#
# ListMergeVarAdd
# Add a new field to a MailChimp list.
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

class ListMergeVarAdd(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListMergeVarAdd Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ListMergeVarAdd, self).__init__(temboo_session, '/Library/MailChimp/ListMergeVarAdd')


    def new_input_set(self):
        return ListMergeVarAddInputSet()

    def _make_result_set(self, result, path):
        return ListMergeVarAddResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListMergeVarAddChoreographyExecution(session, exec_id, path)

class ListMergeVarAddInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListMergeVarAdd
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Mailchimp.)
        """
        super(ListMergeVarAddInputSet, self)._set_input('APIKey', value)
    def set_Choices(self, value):
        """
        Set the value of the Choices input for this Choreo. ((optional, string) A list of up to 10 choices for radio and dropdown type fields )separated by commas).)
        """
        super(ListMergeVarAddInputSet, self)._set_input('Choices', value)
    def set_DateFormat(self, value):
        """
        Set the value of the DateFormat input for this Choreo. ((optional, string) Valid for birthday and date fields. For birthday, must be "MM/DD" (default) or "DD/MM". For date type, must be "MM/DD/YYYY" (default) or "DD/MM/YYYY".)
        """
        super(ListMergeVarAddInputSet, self)._set_input('DateFormat', value)
    def set_DefaultCountry(self, value):
        """
        Set the value of the DefaultCountry input for this Choreo. ((optional, string) The ISO 3166 2 digit character code for the default country. Defaults to "US".)
        """
        super(ListMergeVarAddInputSet, self)._set_input('DefaultCountry', value)
    def set_DefaultValue(self, value):
        """
        Set the value of the DefaultValue input for this Choreo. ((optional, string) The default value for the new field.)
        """
        super(ListMergeVarAddInputSet, self)._set_input('DefaultValue', value)
    def set_FieldType(self, value):
        """
        Set the value of the FieldType input for this Choreo. ((optional, string) Must be either left unset or one of 'text', 'number', 'radio', 'dropdown', 'date', 'address', 'phone', 'url', or 'imageurl. Defaults to text.)
        """
        super(ListMergeVarAddInputSet, self)._set_input('FieldType', value)
    def set_ListId(self, value):
        """
        Set the value of the ListId input for this Choreo. ((required, string) The ID of the list on which to add the new merge var.)
        """
        super(ListMergeVarAddInputSet, self)._set_input('ListId', value)
    def set_Name(self, value):
        """
        Set the value of the Name input for this Choreo. ((required, string) Provide a long merge var name for user display (i.e. First Name))
        """
        super(ListMergeVarAddInputSet, self)._set_input('Name', value)
    def set_PhoneFormat(self, value):
        """
        Set the value of the PhoneFormat input for this Choreo. ((optional, string) Defaults to "US"  - any other value will cause them to be unformatted (international).)
        """
        super(ListMergeVarAddInputSet, self)._set_input('PhoneFormat', value)
    def set_Public(self, value):
        """
        Set the value of the Public input for this Choreo. ((optional, boolean) Indicates whether the field is displayed in public. Specify '1' (true) or '0' (false). Defaults to 1.)
        """
        super(ListMergeVarAddInputSet, self)._set_input('Public', value)
    def set_Req(self, value):
        """
        Set the value of the Req input for this Choreo. ((optional, boolean) Indicates that the field will be required.  Specify '1' (true) or '0' (false). Defaults to 0.)
        """
        super(ListMergeVarAddInputSet, self)._set_input('Req', value)
    def set_Show(self, value):
        """
        Set the value of the Show input for this Choreo. ((optional, boolean) Indicates whether the field is displayed in the app's list member view.  Specify '1' (true) or '0' (false). Defaults to 1.)
        """
        super(ListMergeVarAddInputSet, self)._set_input('Show', value)
    def set_Tag(self, value):
        """
        Set the value of the Tag input for this Choreo. ((required, string) Provide a short merge var tag name. MUST be 10 UTF-8 chars, including 'A-Z', '0-9', or '_' only (i.e. DESC123456).)
        """
        super(ListMergeVarAddInputSet, self)._set_input('Tag', value)

class ListMergeVarAddResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListMergeVarAdd Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((boolean) The response from Mailchimp. Returns the string "true" for success and an error description for failures.)
        """
        return self._output.get('Response', None)

class ListMergeVarAddChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ListMergeVarAddResultSet(response, path)
