# -*- coding: utf-8 -*-

###############################################################################
#
# ThreadDetails
# Obtain thread details.
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

class ThreadDetails(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ThreadDetails Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ThreadDetails, self).__init__(temboo_session, '/Library/Disqus/Threads/ThreadDetails')


    def new_input_set(self):
        return ThreadDetailsInputSet()

    def _make_result_set(self, result, path):
        return ThreadDetailsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ThreadDetailsChoreographyExecution(session, exec_id, path)

class ThreadDetailsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ThreadDetails
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Forum(self, value):
        """
        Set the value of the Forum input for this Choreo. ((optional, string) Forum Short Name (i.e., the subdomain of the Disqus Site URL).  Required if setting either ThreadByIdentification, or ThreadByLink.)
        """
        super(ThreadDetailsInputSet, self)._set_input('Forum', value)
    def set_PublicKey(self, value):
        """
        Set the value of the PublicKey input for this Choreo. ((required, string) The Public Key provided by Disqus (AKA the API Key).)
        """
        super(ThreadDetailsInputSet, self)._set_input('PublicKey', value)
    def set_Related(self, value):
        """
        Set the value of the Related input for this Choreo. ((optional, string) Indicates the relations to include with your response.  Valid entries include: author, category, or forum.)
        """
        super(ThreadDetailsInputSet, self)._set_input('Related', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and jsonp.)
        """
        super(ThreadDetailsInputSet, self)._set_input('ResponseFormat', value)
    def set_ThreadID(self, value):
        """
        Set the value of the ThreadID input for this Choreo. ((conditional, integer) The ID of a thread that is to be retrieved. Required unless specifying ThreadIdentifier or ThreadLink. If using this parameter, ThreadIdentifier cannot be set.)
        """
        super(ThreadDetailsInputSet, self)._set_input('ThreadID', value)
    def set_ThreadIdentifier(self, value):
        """
        Set the value of the ThreadIdentifier input for this Choreo. ((conditional, string) The identifier to retrieve associated thread details. Note that a Forum must also be provided when using this parameter. If set, ThreadID and ThreadLink cannot be used.)
        """
        super(ThreadDetailsInputSet, self)._set_input('ThreadIdentifier', value)
    def set_ThreadLink(self, value):
        """
        Set the value of the ThreadLink input for this Choreo. ((conditional, string) A link pointing to the thread that is to be retrieved. Note that a Forum must also be provided when using this parameter. If set, ThreadID and ThreadIdentifier cannot be set.)
        """
        super(ThreadDetailsInputSet, self)._set_input('ThreadLink', value)


class ThreadDetailsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ThreadDetails Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Disqus.)
        """
        return self._output.get('Response', None)

class ThreadDetailsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ThreadDetailsResultSet(response, path)
