# -*- coding: utf-8 -*-

###############################################################################
#
# CreatePlan
# Creates a subscription plan
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

class CreatePlan(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreatePlan Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CreatePlan, self).__init__(temboo_session, '/Library/Stripe/Plans/CreatePlan')


    def new_input_set(self):
        return CreatePlanInputSet()

    def _make_result_set(self, result, path):
        return CreatePlanResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreatePlanChoreographyExecution(session, exec_id, path)

class CreatePlanInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreatePlan
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Stripe)
        """
        super(CreatePlanInputSet, self)._set_input('APIKey', value)
    def set_Amount(self, value):
        """
        Set the value of the Amount input for this Choreo. ((required, integer) The amount in cents to charge on a recurring basis for subscribers of this plan)
        """
        super(CreatePlanInputSet, self)._set_input('Amount', value)
    def set_Currency(self, value):
        """
        Set the value of the Currency input for this Choreo. ((optional, string) 3-letter ISO code for currency. Defaults to 'usd' which is currently the only supported currency.)
        """
        super(CreatePlanInputSet, self)._set_input('Currency', value)
    def set_Interval(self, value):
        """
        Set the value of the Interval input for this Choreo. ((required, string) Indicates billing frequency. Valid values are: month or year.)
        """
        super(CreatePlanInputSet, self)._set_input('Interval', value)
    def set_PlanID(self, value):
        """
        Set the value of the PlanID input for this Choreo. ((required, string) The unique identifier of the plan you want to create)
        """
        super(CreatePlanInputSet, self)._set_input('PlanID', value)
    def set_PlanName(self, value):
        """
        Set the value of the PlanName input for this Choreo. ((required, string) The name of the plan which will be displayed in the Stripe web interface.)
        """
        super(CreatePlanInputSet, self)._set_input('PlanName', value)
    def set_TrialPeriodDays(self, value):
        """
        Set the value of the TrialPeriodDays input for this Choreo. ((optional, integer) The number of days in a trial period (customer will not be billed until the trial period is over))
        """
        super(CreatePlanInputSet, self)._set_input('TrialPeriodDays', value)

class CreatePlanResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreatePlan Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Stripe)
        """
        return self._output.get('Response', None)

class CreatePlanChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CreatePlanResultSet(response, path)
