# -*- coding: utf-8 -*-

###############################################################################
#
# StreamSensorData
# Creates a new label.
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

class StreamSensorData(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the StreamSensorData Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(StreamSensorData, self).__init__(temboo_session, '/Library/Util/StreamSensorData')


    def new_input_set(self):
        return StreamSensorDataInputSet()

    def _make_result_set(self, result, path):
        return StreamSensorDataResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return StreamSensorDataChoreographyExecution(session, exec_id, path)

class StreamSensorDataInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the StreamSensorData
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Async(self, value):
        """
        Set the value of the Async input for this Choreo. ((optional, boolean) When set to "true" the request to the data service happens asyncronously. Set to "false" if you want the Choreo to wait for the execution to complete and return API's response.)
        """
        super(StreamSensorDataInputSet, self)._set_input('Async', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by the data service.)
        """
        super(StreamSensorDataInputSet, self)._set_input('ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The Client Secret provided by the data service.)
        """
        super(StreamSensorDataInputSet, self)._set_input('ClientSecret', value)
    def set_DatasetID(self, value):
        """
        Set the value of the DatasetID input for this Choreo. ((required, string) The ID of the dataset that your table belongs to.)
        """
        super(StreamSensorDataInputSet, self)._set_input('DatasetID', value)
    def set_ProjectID(self, value):
        """
        Set the value of the ProjectID input for this Choreo. ((required, string) The ID of your Google API project.)
        """
        super(StreamSensorDataInputSet, self)._set_input('ProjectID', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((conditional, string) An OAuth Refresh Token used to generate a new Access Token when the original token is expired.)
        """
        super(StreamSensorDataInputSet, self)._set_input('RefreshToken', value)
    def set_SensorData(self, value):
        """
        Set the value of the SensorData input for this Choreo. ((required, json) A JSON object containing key/value pairs.)
        """
        super(StreamSensorDataInputSet, self)._set_input('SensorData', value)
    def set_Service(self, value):
        """
        Set the value of the Service input for this Choreo. ((required, string) Indicates the service to stream to. Valid values are: BigQuery or Power BI)
        """
        super(StreamSensorDataInputSet, self)._set_input('Service', value)
    def set_TableID(self, value):
        """
        Set the value of the TableID input for this Choreo. ((required, string) The ID (or name) of the table to insert a row into.)
        """
        super(StreamSensorDataInputSet, self)._set_input('TableID', value)
    def set_TimestampColumn(self, value):
        """
        Set the value of the TimestampColumn input for this Choreo. ((optional, string) The name of the column that that the choreo will auto-generate a timestamp for.)
        """
        super(StreamSensorDataInputSet, self)._set_input('TimestampColumn', value)
    def set_TimestampFormat(self, value):
        """
        Set the value of the TimestampFormat input for this Choreo. ((optional, string) The format of the auto generated timestamp (e.g. yyyy-MM-dd HH:mm:ss.SSS). If set to "milliseconds" or "seconds", the timestamp will be an epoch date.)
        """
        super(StreamSensorDataInputSet, self)._set_input('TimestampFormat', value)

class StreamSensorDataResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the StreamSensorData Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) Contains the response from Google when using the Async=fase option.)
        """
        return self._output.get('Response', None)
    def get_ResponseStatusCode(self):
        """
        Retrieve the value for the "ResponseStatusCode" output from this Choreo execution. ((integer) The response status code from the API.)
        """
        return self._output.get('ResponseStatusCode', None)

class StreamSensorDataChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return StreamSensorDataResultSet(response, path)
