# -*- coding: utf-8 -*-

###############################################################################
#
# RevokeSubscription
# Allows your application to revoke a previously subscribed notification.
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

class RevokeSubscription(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RevokeSubscription Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(RevokeSubscription, self).__init__(temboo_session, '/Library/Withings/Notification/RevokeSubscription')


    def new_input_set(self):
        return RevokeSubscriptionInputSet()

    def _make_result_set(self, result, path):
        return RevokeSubscriptionResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RevokeSubscriptionChoreographyExecution(session, exec_id, path)

class RevokeSubscriptionInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RevokeSubscription
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        super(RevokeSubscriptionInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        super(RevokeSubscriptionInputSet, self)._set_input('AccessToken', value)
    def set_Application(self, value):
        """
        Set the value of the Application input for this Choreo. ((optional, integer) Specifies the device type for which the notification is to be revoked. Set to 1 for Bodyscale.)
        """
        super(RevokeSubscriptionInputSet, self)._set_input('Application', value)
    def set_CallbackURL(self, value):
        """
        Set the value of the CallbackURL input for this Choreo. ((required, string) The URL used when subscribing to the notification service.)
        """
        super(RevokeSubscriptionInputSet, self)._set_input('CallbackURL', value)
    def set_ConsumerKey(self, value):
        """
        Set the value of the ConsumerKey input for this Choreo. ((required, string) The Consumer Key provided by Withings.)
        """
        super(RevokeSubscriptionInputSet, self)._set_input('ConsumerKey', value)
    def set_ConsumerSecret(self, value):
        """
        Set the value of the ConsumerSecret input for this Choreo. ((required, string) The Consumer Secret provided by Withings.)
        """
        super(RevokeSubscriptionInputSet, self)._set_input('ConsumerSecret', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((required, string) The ID of the user to revoke a subscription for.)
        """
        super(RevokeSubscriptionInputSet, self)._set_input('UserID', value)

class RevokeSubscriptionResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RevokeSubscription Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Withings.)
        """
        return self._output.get('Response', None)

class RevokeSubscriptionChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return RevokeSubscriptionResultSet(response, path)
