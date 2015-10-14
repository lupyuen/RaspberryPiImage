# -*- coding: utf-8 -*-

###############################################################################
#
# WriteData
# Allows you to update your feed, including updating/creating new datastreams and datapoints. 
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

class WriteData(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the WriteData Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(WriteData, self).__init__(temboo_session, '/Library/Xively/ReadWriteData/WriteData')


    def new_input_set(self):
        return WriteDataInputSet()

    def _make_result_set(self, result, path):
        return WriteDataResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return WriteDataChoreographyExecution(session, exec_id, path)

class WriteDataInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the WriteData
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_FeedData(self, value):
        """
        Set the value of the FeedData input for this Choreo. ((optional, any) Custom data body for the new feed in JSON or XML format (set by FeedType).  See Xively documentation (link below) for the minimum required fields. If FeedData is used, Value and Timestamp are ignored.)
        """
        super(WriteDataInputSet, self)._set_input('FeedData', value)
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Xively.)
        """
        super(WriteDataInputSet, self)._set_input('APIKey', value)
    def set_DatastreamID(self, value):
        """
        Set the value of the DatastreamID input for this Choreo. ((optional, string) ID for single datastream you would like to update. Required if specifying a single datapoint update using Value.)
        """
        super(WriteDataInputSet, self)._set_input('DatastreamID', value)
    def set_FeedID(self, value):
        """
        Set the value of the FeedID input for this Choreo. ((required, integer) The ID for the feed that you would like to update.)
        """
        super(WriteDataInputSet, self)._set_input('FeedID', value)
    def set_FeedType(self, value):
        """
        Set the value of the FeedType input for this Choreo. ((optional, string) The type of feed that is being provided for custom FeedData. Valid values are "json" (the default), "xml" and "csv". Ignored if specifying single datapoint Value.)
        """
        super(WriteDataInputSet, self)._set_input('FeedType', value)
    def set_Timestamp(self, value):
        """
        Set the value of the Timestamp input for this Choreo. ((optional, date) Can be used with a single Value and DatastreamID. If specified, sets timestamp for Value. If Value is set with blank Timestamp, Value's timestamp will be current time. Ex: 2013-05-10T00:00:00.123456Z.)
        """
        super(WriteDataInputSet, self)._set_input('Timestamp', value)
    def set_Value(self, value):
        """
        Set the value of the Value input for this Choreo. ((optional, string) Specifies the value for a single datapoint in a specified datastream.)
        """
        super(WriteDataInputSet, self)._set_input('Value', value)

class WriteDataResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the WriteData Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_ResponseStatusCode(self):
        """
        Retrieve the value for the "ResponseStatusCode" output from this Choreo execution. ((integer) The response status code returned from Xively. For a successful feed / data update, the code should be 200.)
        """
        return self._output.get('ResponseStatusCode', None)

class WriteDataChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return WriteDataResultSet(response, path)
