# -*- coding: utf-8 -*-

###############################################################################
#
# GetTariffs
# Returns a list of Tariff objects based a specified search criteria.
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

class GetTariffs(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetTariffs Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetTariffs, self).__init__(temboo_session, '/Library/Genability/TariffData/GetTariffs')


    def new_input_set(self):
        return GetTariffsInputSet()

    def _make_result_set(self, result, path):
        return GetTariffsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetTariffsChoreographyExecution(session, exec_id, path)

class GetTariffsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetTariffs
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccountID(self, value):
        """
        Set the value of the AccountID input for this Choreo. ((optional, string) The unique ID of the Account to find tariffs for. Values passed in will override those from the Account.)
        """
        super(GetTariffsInputSet, self)._set_input('AccountID', value)
    def set_AppID(self, value):
        """
        Set the value of the AppID input for this Choreo. ((conditional, string) The App ID provided by Genability.)
        """
        super(GetTariffsInputSet, self)._set_input('AppID', value)
    def set_AppKey(self, value):
        """
        Set the value of the AppKey input for this Choreo. ((required, string) The App Key provided by Genability.)
        """
        super(GetTariffsInputSet, self)._set_input('AppKey', value)
    def set_CustomerClasses(self, value):
        """
        Set the value of the CustomerClasses input for this Choreo. ((optional, string) Returns only these customer classes. Valid values are: RESIDENTIAL, GENERAL.)
        """
        super(GetTariffsInputSet, self)._set_input('CustomerClasses', value)
    def set_EffectiveOn(self, value):
        """
        Set the value of the EffectiveOn input for this Choreo. ((optional, date) Returns only tariffs that are effective on this date.)
        """
        super(GetTariffsInputSet, self)._set_input('EffectiveOn', value)
    def set_EndsWith(self, value):
        """
        Set the value of the EndsWith input for this Choreo. ((optional, string) When true, the search will only return results that end with the specified search string. Otherwise, any match of the search string will be returned as a result.)
        """
        super(GetTariffsInputSet, self)._set_input('EndsWith', value)
    def set_FromDateTime(self, value):
        """
        Set the value of the FromDateTime input for this Choreo. ((optional, date) Returns only tariffs that are effective on or after this date.)
        """
        super(GetTariffsInputSet, self)._set_input('FromDateTime', value)
    def set_IsRegex(self, value):
        """
        Set the value of the IsRegex input for this Choreo. ((optional, boolean) When true, the provided search string will be regarded as a regular expression and the search will return results matching the regular expression.)
        """
        super(GetTariffsInputSet, self)._set_input('IsRegex', value)
    def set_LSEID(self, value):
        """
        Set the value of the LSEID input for this Choreo. ((optional, integer) Filter tariffs for a specific LSE.)
        """
        super(GetTariffsInputSet, self)._set_input('LSEID', value)
    def set_PageCount(self, value):
        """
        Set the value of the PageCount input for this Choreo. ((optional, integer) The number of results to return. Defaults to 25.)
        """
        super(GetTariffsInputSet, self)._set_input('PageCount', value)
    def set_PageStart(self, value):
        """
        Set the value of the PageStart input for this Choreo. ((optional, integer) The page number to begin the result set from. Defaults to 1.)
        """
        super(GetTariffsInputSet, self)._set_input('PageStart', value)
    def set_PopulateProperties(self, value):
        """
        Set the value of the PopulateProperties input for this Choreo. ((optional, boolean) Set to "true" to populate the properties for the returned Tariffs.)
        """
        super(GetTariffsInputSet, self)._set_input('PopulateProperties', value)
    def set_PopulateRates(self, value):
        """
        Set the value of the PopulateRates input for this Choreo. ((optional, boolean) Set to "true" to populate the rate details for the returned Tariffs.)
        """
        super(GetTariffsInputSet, self)._set_input('PopulateRates', value)
    def set_SearchOn(self, value):
        """
        Set the value of the SearchOn input for this Choreo. ((optional, string) Comma separated list of fields to query on. When searchOn is specified, the text provided in the search string field will be searched within these fields.)
        """
        super(GetTariffsInputSet, self)._set_input('SearchOn', value)
    def set_Search(self, value):
        """
        Set the value of the Search input for this Choreo. ((optional, string) The string of text to search on. This can also be a regular expression, in which case you should set the 'isRegex' flag to true.)
        """
        super(GetTariffsInputSet, self)._set_input('Search', value)
    def set_SortOn(self, value):
        """
        Set the value of the SortOn input for this Choreo. ((optional, string) Comma separated list of fields to sort on.)
        """
        super(GetTariffsInputSet, self)._set_input('SortOn', value)
    def set_SortOrder(self, value):
        """
        Set the value of the SortOrder input for this Choreo. ((optional, string) Comma separated list of ordering. Possible values are 'ASC' and 'DESC'. Default is 'ASC'. This list corresponds to the field list used in the SortOn input.)
        """
        super(GetTariffsInputSet, self)._set_input('SortOrder', value)
    def set_StartsWith(self, value):
        """
        Set the value of the StartsWith input for this Choreo. ((optional, boolean) When true, the search will only return results that begin with the specified search string. Otherwise, any match of the search string will be returned as a result.)
        """
        super(GetTariffsInputSet, self)._set_input('StartsWith', value)
    def set_TariffTypes(self, value):
        """
        Set the value of the TariffTypes input for this Choreo. ((optional, string) Returns only these tariff types. Valid values are: DEFAULT, ALTERNATIVE, OPTIONAL_EXTRA, RIDER.)
        """
        super(GetTariffsInputSet, self)._set_input('TariffTypes', value)
    def set_ToDateTime(self, value):
        """
        Set the value of the ToDateTime input for this Choreo. ((optional, date) Returns only tariffs that are effective on or before this date.)
        """
        super(GetTariffsInputSet, self)._set_input('ToDateTime', value)
    def set_ZipCode(self, value):
        """
        Set the value of the ZipCode input for this Choreo. ((optional, string) Return tariffs for a given zip or post code.)
        """
        super(GetTariffsInputSet, self)._set_input('ZipCode', value)

class GetTariffsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetTariffs Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Genability.)
        """
        return self._output.get('Response', None)

class GetTariffsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetTariffsResultSet(response, path)
