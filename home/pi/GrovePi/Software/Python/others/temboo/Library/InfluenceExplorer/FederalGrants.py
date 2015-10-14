# -*- coding: utf-8 -*-

###############################################################################
#
# FederalGrants
# Returns information about federal grants awarded.
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

class FederalGrants(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the FederalGrants Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(FederalGrants, self).__init__(temboo_session, '/Library/InfluenceExplorer/FederalGrants')


    def new_input_set(self):
        return FederalGrantsInputSet()

    def _make_result_set(self, result, path):
        return FederalGrantsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FederalGrantsChoreographyExecution(session, exec_id, path)

class FederalGrantsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the FederalGrants
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API key provided by Sunlight Data Services.)
        """
        super(FederalGrantsInputSet, self)._set_input('APIKey', value)
    def set_AgencyName(self, value):
        """
        Set the value of the AgencyName input for this Choreo. ((optional, string) Full-text search on the reported name of the federal agency awarding the grant.)
        """
        super(FederalGrantsInputSet, self)._set_input('AgencyName', value)
    def set_Amount(self, value):
        """
        Set the value of the Amount input for this Choreo. ((optional, string) The grant amount. Valid formats include: 500 (exactly $500); >|500 (greater than, or equal to 500); <|500 (less than or equal to 500).)
        """
        super(FederalGrantsInputSet, self)._set_input('Amount', value)
    def set_AssistanceType(self, value):
        """
        Set the value of the AssistanceType input for this Choreo. ((optional, integer) A numeric code for the type of grant awarded. See documentation for more details for this parameter.)
        """
        super(FederalGrantsInputSet, self)._set_input('AssistanceType', value)
    def set_FiscalYear(self, value):
        """
        Set the value of the FiscalYear input for this Choreo. ((optional, date) The year in which the grant was awarded. A YYYY formatted year. You can also specify a range by separating years with a pipe (i.e. 2008|2012).)
        """
        super(FederalGrantsInputSet, self)._set_input('FiscalYear', value)
    def set_RecipientName(self, value):
        """
        Set the value of the RecipientName input for this Choreo. ((optional, string) Full-text search on the reported name of the grant recipient.)
        """
        super(FederalGrantsInputSet, self)._set_input('RecipientName', value)
    def set_RecipientState(self, value):
        """
        Set the value of the RecipientState input for this Choreo. ((optional, string) Two-letter abbreviation of the state in which the grant was awarded.)
        """
        super(FederalGrantsInputSet, self)._set_input('RecipientState', value)
    def set_RecipientType(self, value):
        """
        Set the value of the RecipientType input for this Choreo. ((optional, integer) The numeric code representing the type of entity that received the grant. See documentation for more details about this parameter.)
        """
        super(FederalGrantsInputSet, self)._set_input('RecipientType', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) Indicates the desired format for the response. Accepted values are: json (the default), csv, and xls. Note when specifying xls, restults are returned as Base64 encoded data.)
        """
        super(FederalGrantsInputSet, self)._set_input('ResponseFormat', value)

class FederalGrantsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the FederalGrants Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Influence Explorer. Corresponds to the ResponseFormat input. Defaults to json.)
        """
        return self._output.get('Response', None)

class FederalGrantsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return FederalGrantsResultSet(response, path)
