# -*- coding: utf-8 -*-

###############################################################################
#
# RunNewPriceCalculation
# Calculate electricity costs based on a POSTed calculation criteria. 
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

class RunNewPriceCalculation(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RunNewPriceCalculation Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(RunNewPriceCalculation, self).__init__(temboo_session, '/Library/Genability/PricingAndCalc/RunNewPriceCalculation')


    def new_input_set(self):
        return RunNewPriceCalculationInputSet()

    def _make_result_set(self, result, path):
        return RunNewPriceCalculationResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RunNewPriceCalculationChoreographyExecution(session, exec_id, path)

class RunNewPriceCalculationInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RunNewPriceCalculation
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_POSTData(self, value):
        """
        Set the value of the POSTData input for this Choreo. ((required, json) The POST payload in JSON format.)
        """
        super(RunNewPriceCalculationInputSet, self)._set_input('POSTData', value)
    def set_AppID(self, value):
        """
        Set the value of the AppID input for this Choreo. ((required, string) The App ID provided by Genability.)
        """
        super(RunNewPriceCalculationInputSet, self)._set_input('AppID', value)
    def set_AppKey(self, value):
        """
        Set the value of the AppKey input for this Choreo. ((required, string) The App Key provided by Genability.)
        """
        super(RunNewPriceCalculationInputSet, self)._set_input('AppKey', value)
    def set_MasterTariffID(self, value):
        """
        Set the value of the MasterTariffID input for this Choreo. ((required, string) A Genability tariff ID.)
        """
        super(RunNewPriceCalculationInputSet, self)._set_input('MasterTariffID', value)

class RunNewPriceCalculationResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RunNewPriceCalculation Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Genability.)
        """
        return self._output.get('Response', None)

class RunNewPriceCalculationChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return RunNewPriceCalculationResultSet(response, path)
