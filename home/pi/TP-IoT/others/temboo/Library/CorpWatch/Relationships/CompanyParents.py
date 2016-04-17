# -*- coding: utf-8 -*-

###############################################################################
#
# CompanyParents
# Returns a list of principal owning companies, or "parents," of a company.
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

class CompanyParents(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CompanyParents Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CompanyParents, self).__init__(temboo_session, '/Library/CorpWatch/Relationships/CompanyParents')


    def new_input_set(self):
        return CompanyParentsInputSet()

    def _make_result_set(self, result, path):
        return CompanyParentsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CompanyParentsChoreographyExecution(session, exec_id, path)

class CompanyParentsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CompanyParents
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((optional, string) The APIKey from CorpWatch if you have one.)
        """
        super(CompanyParentsInputSet, self)._set_input('APIKey', value)
    def set_CWID(self, value):
        """
        Set the value of the CWID input for this Choreo. ((required, string) CoprWatch ID for the company. Format looks like: cw_8484.)
        """
        super(CompanyParentsInputSet, self)._set_input('CWID', value)
    def set_Index(self, value):
        """
        Set the value of the Index input for this Choreo. ((optional, integer) Set the index number of the first result to be returned. The index of the first result is 0.)
        """
        super(CompanyParentsInputSet, self)._set_input('Index', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) The number of results to be returned. Defaults to 100. Maximum is 5000.)
        """
        super(CompanyParentsInputSet, self)._set_input('Limit', value)
    def set_ResponseType(self, value):
        """
        Set the value of the ResponseType input for this Choreo. ((optional, string) Specify json or xml for the type of response to be returned. Defaults to xml.)
        """
        super(CompanyParentsInputSet, self)._set_input('ResponseType', value)
    def set_Year(self, value):
        """
        Set the value of the Year input for this Choreo. ((optional, integer) If a year is specified, only parents for that year will be returned and the data in the company objects returned will be set appropriately for the request year. Defaults to most recent.)
        """
        super(CompanyParentsInputSet, self)._set_input('Year', value)

class CompanyParentsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CompanyParents Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from CorpWatch.)
        """
        return self._output.get('Response', None)

class CompanyParentsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CompanyParentsResultSet(response, path)
