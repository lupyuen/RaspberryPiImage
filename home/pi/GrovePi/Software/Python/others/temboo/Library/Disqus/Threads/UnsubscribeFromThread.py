# -*- coding: utf-8 -*-

###############################################################################
#
# UnsubscribeFromThread
# Unsubscribe from a thread.
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

class UnsubscribeFromThread(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UnsubscribeFromThread Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(UnsubscribeFromThread, self).__init__(temboo_session, '/Library/Disqus/Threads/UnsubscribeFromThread')


    def new_input_set(self):
        return UnsubscribeFromThreadInputSet()

    def _make_result_set(self, result, path):
        return UnsubscribeFromThreadResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UnsubscribeFromThreadChoreographyExecution(session, exec_id, path)

class UnsubscribeFromThreadInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UnsubscribeFromThread
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Email(self, value):
        """
        Set the value of the Email input for this Choreo. ((conditional, string) The email address that will be unsubsribed from the thread.)
        """
        super(UnsubscribeFromThreadInputSet, self)._set_input('Email', value)
    def set_Forum(self, value):
        """
        Set the value of the Forum input for this Choreo. ((optional, string) Forum Short Name (i.e., the subdomain of the Disqus Site URL) of a thread that is to be unsubscribed from. Required if setting either ThreadByIdentification, or ThreadByLink.)
        """
        super(UnsubscribeFromThreadInputSet, self)._set_input('Forum', value)
    def set_PublicKey(self, value):
        """
        Set the value of the PublicKey input for this Choreo. ((required, string) The Public Key provided by Disqus (AKA the API Key).)
        """
        super(UnsubscribeFromThreadInputSet, self)._set_input('PublicKey', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and jsonp.)
        """
        super(UnsubscribeFromThreadInputSet, self)._set_input('ResponseFormat', value)
    def set_ThreadID(self, value):
        """
        Set the value of the ThreadID input for this Choreo. ((conditional, integer) The ID of a thread that is to be unsubscribed from. Required unless specifying the ThreadIdentifier or ThreadLink. If using this parameter, ThreadIdentifier cannot be set.)
        """
        super(UnsubscribeFromThreadInputSet, self)._set_input('ThreadID', value)
    def set_ThreadIdentifier(self, value):
        """
        Set the value of the ThreadIdentifier input for this Choreo. ((conditional, string) The identifier for the thread that is to be unsubscribed from.  Note that a Forum must also be provided when using this parameter. If set, ThreadID and ThreadLink cannot be used.)
        """
        super(UnsubscribeFromThreadInputSet, self)._set_input('ThreadIdentifier', value)
    def set_ThreadLink(self, value):
        """
        Set the value of the ThreadLink input for this Choreo. ((conditional, string) A link pointing to the thread that is to be unsubscribed from. Note that a Forum must also be provided when using this parameter. If set, ThreadID and ThreadIdentifier cannot be set.)
        """
        super(UnsubscribeFromThreadInputSet, self)._set_input('ThreadLink', value)


class UnsubscribeFromThreadResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UnsubscribeFromThread Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Disqus.)
        """
        return self._output.get('Response', None)

class UnsubscribeFromThreadChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UnsubscribeFromThreadResultSet(response, path)
