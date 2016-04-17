# -*- coding: utf-8 -*-

###############################################################################
#
# Contracts
# Allows access to the information in the Federal Procurement Data System (FPDS) database, which reports all federal contracts awarded. 
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

class Contracts(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Contracts Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(Contracts, self).__init__(temboo_session, '/Library/FedSpending/Contracts')


    def new_input_set(self):
        return ContractsInputSet()

    def _make_result_set(self, result, path):
        return ContractsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ContractsChoreographyExecution(session, exec_id, path)

class ContractsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Contracts
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_City(self, value):
        """
        Set the value of the City input for this Choreo. ((conditional, string) The city within a contractor's address.)
        """
        super(ContractsInputSet, self)._set_input('City', value)
    def set_CompanyName(self, value):
        """
        Set the value of the CompanyName input for this Choreo. ((conditional, string) The name of a a contractor or contractor parent company.)
        """
        super(ContractsInputSet, self)._set_input('CompanyName', value)
    def set_Completion(self, value):
        """
        Set the value of the Completion input for this Choreo. ((conditional, string) The competition status of a contract. Valid values: c=Full competition, o=Full competition, one bid, p=Competition, exclusion of sources, n=Not complete, a=Not available, f=Follow-up, u=Unknown.)
        """
        super(ContractsInputSet, self)._set_input('Completion', value)
    def set_Detail(self, value):
        """
        Set the value of the Detail input for this Choreo. ((optional, string) Controls the level of detail of the output. Acceptable values: -1 (summary), 0 (low), 1 (medium), 2 (high), and 3 (extensive). Defaults to -1. See docs for more information.)
        """
        super(ContractsInputSet, self)._set_input('Detail', value)
    def set_FirstYearRange(self, value):
        """
        Set the value of the FirstYearRange input for this Choreo. ((conditional, integer) Specifies the first year in a range of years; if used, must be used with LastYearRange and without FiscalYear.)
        """
        super(ContractsInputSet, self)._set_input('FirstYearRange', value)
    def set_FiscalYear(self, value):
        """
        Set the value of the FiscalYear input for this Choreo. ((conditional, integer) Specifies a single year; defaults to all years.)
        """
        super(ContractsInputSet, self)._set_input('FiscalYear', value)
    def set_LastYearRange(self, value):
        """
        Set the value of the LastYearRange input for this Choreo. ((conditional, integer) Specifies the last year in a range of years; if used, must be used with FirstYearRange and without FiscalYear.)
        """
        super(ContractsInputSet, self)._set_input('LastYearRange', value)
    def set_MajAgency(self, value):
        """
        Set the value of the MajAgency input for this Choreo. ((conditional, string) The 2-character code for a major governmental agency issuing contracts.)
        """
        super(ContractsInputSet, self)._set_input('MajAgency', value)
    def set_MaxRecords(self, value):
        """
        Set the value of the MaxRecords input for this Choreo. ((optional, integer) Allows you to set the maximum number of records retrieved. Defaults to 100.)
        """
        super(ContractsInputSet, self)._set_input('MaxRecords', value)
    def set_ModAgency(self, value):
        """
        Set the value of the ModAgency input for this Choreo. ((conditional, string) The 4-digit code for a specific governmental agency issuing contracts.)
        """
        super(ContractsInputSet, self)._set_input('ModAgency', value)
    def set_PIID(self, value):
        """
        Set the value of the PIID input for this Choreo. ((conditional, integer) A Federal ID number for the contract.)
        """
        super(ContractsInputSet, self)._set_input('PIID', value)
    def set_PSCCategory(self, value):
        """
        Set the value of the PSCCategory input for this Choreo. ((conditional, string) The 2-character code for a major product or service category.)
        """
        super(ContractsInputSet, self)._set_input('PSCCategory', value)
    def set_PSC(self, value):
        """
        Set the value of the PSC input for this Choreo. ((conditional, string) The 4-character code for a product or service.)
        """
        super(ContractsInputSet, self)._set_input('PSC', value)
    def set_PopCountryCode(self, value):
        """
        Set the value of the PopCountryCode input for this Choreo. ((conditional, string) The two-letter country code for the place of performance country.)
        """
        super(ContractsInputSet, self)._set_input('PopCountryCode', value)
    def set_PopDistrict(self, value):
        """
        Set the value of the PopDistrict input for this Choreo. ((conditional, string) The Congressional District of the place of performance.)
        """
        super(ContractsInputSet, self)._set_input('PopDistrict', value)
    def set_PopZipCode(self, value):
        """
        Set the value of the PopZipCode input for this Choreo. ((conditional, integer) The ZIP code of the place of performance.)
        """
        super(ContractsInputSet, self)._set_input('PopZipCode', value)
    def set_SortBy(self, value):
        """
        Set the value of the SortBy input for this Choreo. ((optional, string) Determines how records are sorted. Valid values: r (contractor/recipient name), f (dollars of awards),g (major contracting agency),p (Product or Service Category),d (date of award). Defaults to f.)
        """
        super(ContractsInputSet, self)._set_input('SortBy', value)
    def set_StateCode(self, value):
        """
        Set the value of the StateCode input for this Choreo. ((conditional, string) The state abbreviation of the state of the place of performance.)
        """
        super(ContractsInputSet, self)._set_input('StateCode', value)
    def set_State(self, value):
        """
        Set the value of the State input for this Choreo. ((conditional, string) The state abbreviation within a contractor's address.)
        """
        super(ContractsInputSet, self)._set_input('State', value)
    def set_TextSearch(self, value):
        """
        Set the value of the TextSearch input for this Choreo. ((conditional, string) Free text search within the text that describes what the contract is for.)
        """
        super(ContractsInputSet, self)._set_input('TextSearch', value)
    def set_VendorCountryCode(self, value):
        """
        Set the value of the VendorCountryCode input for this Choreo. ((conditional, string) The two-letter country code for the country in a contractor's address.)
        """
        super(ContractsInputSet, self)._set_input('VendorCountryCode', value)
    def set_VendorDistrict(self, value):
        """
        Set the value of the VendorDistrict input for this Choreo. ((conditional, string) The 4-character Congressional District within which a contractor is located.)
        """
        super(ContractsInputSet, self)._set_input('VendorDistrict', value)
    def set_ZipCode(self, value):
        """
        Set the value of the ZipCode input for this Choreo. ((conditional, integer) The ZIP code within a contractor's address.)
        """
        super(ContractsInputSet, self)._set_input('ZipCode', value)

class ContractsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Contracts Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from FedSpending.org.)
        """
        return self._output.get('Response', None)

class ContractsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ContractsResultSet(response, path)
