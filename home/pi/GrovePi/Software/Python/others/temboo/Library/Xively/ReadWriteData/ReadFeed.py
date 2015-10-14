# -*- coding: utf-8 -*-

###############################################################################
#
# ReadFeed
# Returns filterable data on a specific feed viewable by the authenticated account.
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

class ReadFeed(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ReadFeed Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ReadFeed, self).__init__(temboo_session, '/Library/Xively/ReadWriteData/ReadFeed')


    def new_input_set(self):
        return ReadFeedInputSet()

    def _make_result_set(self, result, path):
        return ReadFeedResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ReadFeedChoreographyExecution(session, exec_id, path)

class ReadFeedInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ReadFeed
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Xively.)
        """
        super(ReadFeedInputSet, self)._set_input('APIKey', value)
    def set_Datastreams(self, value):
        """
        Set the value of the Datastreams input for this Choreo. ((optional, string) Filter by datastream. Valid values - comma separated datastream IDs (Ex: energy,power).)
        """
        super(ReadFeedInputSet, self)._set_input('Datastreams', value)
    def set_Duration(self, value):
        """
        Set the value of the Duration input for this Choreo. ((optional, string) Used for a historical query. If used with EndDate will request data prior to EndDate, if used with StartDate will request data after StartDate. By itself will give most recent data. Ex: 6hours, 2days.)
        """
        super(ReadFeedInputSet, self)._set_input('Duration', value)
    def set_EndDate(self, value):
        """
        Set the value of the EndDate input for this Choreo. ((optional, date) Used for a historical query. Defines the end point of the data returned as a timestamp. Ex: 2013-05-10T12:00:00Z.)
        """
        super(ReadFeedInputSet, self)._set_input('EndDate', value)
    def set_FeedID(self, value):
        """
        Set the value of the FeedID input for this Choreo. ((required, integer) The ID of the feed you wish to view.)
        """
        super(ReadFeedInputSet, self)._set_input('FeedID', value)
    def set_FeedType(self, value):
        """
        Set the value of the FeedType input for this Choreo. ((optional, string) The type of feed that is being returned. Valid values are "json" (the default), "csv" and "xml". No metadata is returned for the csv feed.)
        """
        super(ReadFeedInputSet, self)._set_input('FeedType', value)
    def set_FindPrevious(self, value):
        """
        Set the value of the FindPrevious input for this Choreo. ((optional, boolean) Used for a historical query. Will also return the previous value to the date range being requested. Useful when graphing, to start a graph with a datapoint. Valid values: "true", blank (default).)
        """
        super(ReadFeedInputSet, self)._set_input('FindPrevious', value)
    def set_IntervalType(self, value):
        """
        Set the value of the IntervalType input for this Choreo. ((optional, string) Used for a historical query. If set to "discrete" the data will be returned in fixed time interval format according to Interval value. If not set, the raw datapoints will be returned.)
        """
        super(ReadFeedInputSet, self)._set_input('IntervalType', value)
    def set_Interval(self, value):
        """
        Set the value of the Interval input for this Choreo. ((optional, integer) Used for a historical query. Determines what interval of data is requested and is defined in seconds between the datapoints. See documentation for full list of possible values. Ex.: 0, 30, 60, etc.)
        """
        super(ReadFeedInputSet, self)._set_input('Interval', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) Used for a historical query. Limits the number of results to the number specified here. Defaults to 100, has a maximum of 1000.)
        """
        super(ReadFeedInputSet, self)._set_input('Limit', value)
    def set_ShowUser(self, value):
        """
        Set the value of the ShowUser input for this Choreo. ((optional, string) Include user login for each feed. For JSON/XML response only. Valid values: "true", "false" (default).)
        """
        super(ReadFeedInputSet, self)._set_input('ShowUser', value)
    def set_StartDate(self, value):
        """
        Set the value of the StartDate input for this Choreo. ((optional, date) Used for a historical query. Defines the starting point of the query as a timestamp. Ex: 2013-05-10T00:00:00Z.)
        """
        super(ReadFeedInputSet, self)._set_input('StartDate', value)

class ReadFeedResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ReadFeed Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Xively.)
        """
        return self._output.get('Response', None)

class ReadFeedChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ReadFeedResultSet(response, path)
