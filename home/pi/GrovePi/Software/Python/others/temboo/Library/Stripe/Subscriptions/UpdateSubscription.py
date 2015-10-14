# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateSubscription
# Subscribes a customer to a specified plan.
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

class UpdateSubscription(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateSubscription Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(UpdateSubscription, self).__init__(temboo_session, '/Library/Stripe/Subscriptions/UpdateSubscription')


    def new_input_set(self):
        return UpdateSubscriptionInputSet()

    def _make_result_set(self, result, path):
        return UpdateSubscriptionResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateSubscriptionChoreographyExecution(session, exec_id, path)

class UpdateSubscriptionInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateSubscription
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Stripe)
        """
        super(UpdateSubscriptionInputSet, self)._set_input('APIKey', value)
    def set_Coupon(self, value):
        """
        Set the value of the Coupon input for this Choreo. ((optional, string) If you provide a coupon code, it can be specified here)
        """
        super(UpdateSubscriptionInputSet, self)._set_input('Coupon', value)
    def set_CustomerID(self, value):
        """
        Set the value of the CustomerID input for this Choreo. ((required, string) The unique identifier of the customer you want to subscribe to a plan)
        """
        super(UpdateSubscriptionInputSet, self)._set_input('CustomerID', value)
    def set_Plan(self, value):
        """
        Set the value of the Plan input for this Choreo. ((required, string) The unique identifier of the plan to subscribe the customer to)
        """
        super(UpdateSubscriptionInputSet, self)._set_input('Plan', value)
    def set_Prorate(self, value):
        """
        Set the value of the Prorate input for this Choreo. ((optional, boolean) When set to 1, Stripe will prorate switching plans during a billing cycle. When set to 0, this feature is disabled. Defaults to 1.)
        """
        super(UpdateSubscriptionInputSet, self)._set_input('Prorate', value)
    def set_Token(self, value):
        """
        Set the value of the Token input for this Choreo. ((optional, string) The token associated with a set of credit card details.)
        """
        super(UpdateSubscriptionInputSet, self)._set_input('Token', value)
    def set_TrialEnd(self, value):
        """
        Set the value of the TrialEnd input for this Choreo. ((optional, date) A timestamp representing the end of the trial period in UTC. The customer will not be charged during the trial period.)
        """
        super(UpdateSubscriptionInputSet, self)._set_input('TrialEnd', value)

class UpdateSubscriptionResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateSubscription Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Stripe)
        """
        return self._output.get('Response', None)

class UpdateSubscriptionChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UpdateSubscriptionResultSet(response, path)
