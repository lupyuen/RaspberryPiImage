# -*- coding: utf-8 -*-

###############################################################################
#
# TopStatsLastWeek
# Retrieves last weeks's top pages, links, and searches.
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

class TopStatsLastWeek(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the TopStatsLastWeek Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(TopStatsLastWeek, self).__init__(temboo_session, '/Library/Clicky/TopStatsLastWeek')


    def new_input_set(self):
        return TopStatsLastWeekInputSet()

    def _make_result_set(self, result, path):
        return TopStatsLastWeekResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return TopStatsLastWeekChoreographyExecution(session, exec_id, path)

class TopStatsLastWeekInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the TopStatsLastWeek
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Output(self, value):
        """
        Set the value of the Output input for this Choreo. ((optional, string) What format you want the returned data to be in. Accepted values: xml, php, json, csv. Defaults to 'xml'.)
        """
        super(TopStatsLastWeekInputSet, self)._set_input('Output', value)
    def set_SiteID(self, value):
        """
        Set the value of the SiteID input for this Choreo. ((required, integer) Your request must include the site's ID that you want to access data from. Available from your site preferences page.)
        """
        super(TopStatsLastWeekInputSet, self)._set_input('SiteID', value)
    def set_SiteKey(self, value):
        """
        Set the value of the SiteKey input for this Choreo. ((required, string) The unique key assigned to you when you first register with Clicky. Available from your site preferences page.)
        """
        super(TopStatsLastWeekInputSet, self)._set_input('SiteKey', value)
    def set_Type(self, value):
        """
        Set the value of the Type input for this Choreo. ((optional, string) The type of data you want to retrieve. Defaults to "pages,links,searches".)
        """
        super(TopStatsLastWeekInputSet, self)._set_input('Type', value)

class TopStatsLastWeekResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the TopStatsLastWeek Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Clicky formatted as specified in the Output parameter. Default is XML.)
        """
        return self._output.get('Response', None)

class TopStatsLastWeekChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return TopStatsLastWeekResultSet(response, path)
