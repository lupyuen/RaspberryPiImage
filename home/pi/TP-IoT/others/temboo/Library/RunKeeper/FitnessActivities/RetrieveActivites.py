# -*- coding: utf-8 -*-

###############################################################################
#
# RetrieveActivites
# Returns a feed of a user's fitness activities.
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

class RetrieveActivites(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RetrieveActivites Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(RetrieveActivites, self).__init__(temboo_session, '/Library/RunKeeper/FitnessActivities/RetrieveActivites')


    def new_input_set(self):
        return RetrieveActivitesInputSet()

    def _make_result_set(self, result, path):
        return RetrieveActivitesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrieveActivitesChoreographyExecution(session, exec_id, path)

class RetrieveActivitesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RetrieveActivites
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved after the final step in the OAuth process.)
        """
        super(RetrieveActivitesInputSet, self)._set_input('AccessToken', value)
    def set_PageSize(self, value):
        """
        Set the value of the PageSize input for this Choreo. ((optional, integer) The number entries to return per page. Defaults to 25.)
        """
        super(RetrieveActivitesInputSet, self)._set_input('PageSize', value)
    def set_Page(self, value):
        """
        Set the value of the Page input for this Choreo. ((optional, integer) The page of entries to return. This parameter is used in combination with the PageSize input to page through results. Defaults to 0 (the first page).)
        """
        super(RetrieveActivitesInputSet, self)._set_input('Page', value)

class RetrieveActivitesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RetrieveActivites Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from RunKeeper.)
        """
        return self._output.get('Response', None)
    def get_Next(self):
        """
        Retrieve the value for the "Next" output from this Choreo execution. ((integer) The next page of entries that is available. This value can be passed into the Page input while paging through entries.)
        """
        return self._output.get('Next', None)
    def get_Previous(self):
        """
        Retrieve the value for the "Previous" output from this Choreo execution. ((integer) The previous page of entries that is available. This value can be passed into the Page input while paging through entries.)
        """
        return self._output.get('Previous', None)

class RetrieveActivitesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return RetrieveActivitesResultSet(response, path)
