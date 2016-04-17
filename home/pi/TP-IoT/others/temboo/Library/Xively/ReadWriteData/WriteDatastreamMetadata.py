# -*- coding: utf-8 -*-

###############################################################################
#
# WriteDatastreamMetadata
# Allows you to easily update the metadata of your datastream.
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

class WriteDatastreamMetadata(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the WriteDatastreamMetadata Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(WriteDatastreamMetadata, self).__init__(temboo_session, '/Library/Xively/ReadWriteData/WriteDatastreamMetadata')


    def new_input_set(self):
        return WriteDatastreamMetadataInputSet()

    def _make_result_set(self, result, path):
        return WriteDatastreamMetadataResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return WriteDatastreamMetadataChoreographyExecution(session, exec_id, path)

class WriteDatastreamMetadataInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the WriteDatastreamMetadata
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Xively.)
        """
        super(WriteDatastreamMetadataInputSet, self)._set_input('APIKey', value)
    def set_CurrentValue(self, value):
        """
        Set the value of the CurrentValue input for this Choreo. ((optional, string) The current value of the datastream. Leave empty to keep existing  CurrentValue. Type "BLANK" to clear existing value.)
        """
        super(WriteDatastreamMetadataInputSet, self)._set_input('CurrentValue', value)
    def set_CustomDatastreamData(self, value):
        """
        Set the value of the CustomDatastreamData input for this Choreo. ((optional, json) Custom datastream formatted as a JSON array. See documentation for how to construct your own datastream feed. If custom DatastreamData is used, all other optional inputs are ignored.)
        """
        super(WriteDatastreamMetadataInputSet, self)._set_input('CustomDatastreamData', value)
    def set_DatastreamID(self, value):
        """
        Set the value of the DatastreamID input for this Choreo. ((required, string) The ID of the Datastream you would like to add metadata to. Required unless you are using CustomDatastreamData.)
        """
        super(WriteDatastreamMetadataInputSet, self)._set_input('DatastreamID', value)
    def set_FeedID(self, value):
        """
        Set the value of the FeedID input for this Choreo. ((required, integer) The ID for the feed that you would like to update.)
        """
        super(WriteDatastreamMetadataInputSet, self)._set_input('FeedID', value)
    def set_MaxValue(self, value):
        """
        Set the value of the MaxValue input for this Choreo. ((optional, string) The maximum value since the last reset. Leave empty to keep existing MaxValue. Type "BLANK" to clear existing value.)
        """
        super(WriteDatastreamMetadataInputSet, self)._set_input('MaxValue', value)
    def set_MinValue(self, value):
        """
        Set the value of the MinValue input for this Choreo. ((optional, string) The minimum value since the last reset. Leave empty to keep existing MinValue. Type "BLANK" to clear existing value.)
        """
        super(WriteDatastreamMetadataInputSet, self)._set_input('MinValue', value)
    def set_Tags(self, value):
        """
        Set the value of the Tags input for this Choreo. ((optional, string) Comma-separated list of searchable tags (the characters ', ", and commas are not allowed). Tags input overwrites previous tags, enter "BLANK" to clear all tags. Ex: "power,energy".)
        """
        super(WriteDatastreamMetadataInputSet, self)._set_input('Tags', value)
    def set_UnitSymbol(self, value):
        """
        Set the value of the UnitSymbol input for this Choreo. ((optional, string) The symbol of the Unit. Leave empty to keep existing UnitSymbol. Type "BLANK" to clear existing value. Ex: "C".)
        """
        super(WriteDatastreamMetadataInputSet, self)._set_input('UnitSymbol', value)
    def set_UnitType(self, value):
        """
        Set the value of the UnitType input for this Choreo. ((optional, string) The type of Unit. Leave empty to keep existing UnitType. Type "BLANK" to clear existing value. Ex: "basicSI".)
        """
        super(WriteDatastreamMetadataInputSet, self)._set_input('UnitType', value)
    def set_Units(self, value):
        """
        Set the value of the Units input for this Choreo. ((optional, string) The units of the datastream. Leave empty to keep existing Units. Type "BLANK" to clear existing Units. Ex: "Celsius".)
        """
        super(WriteDatastreamMetadataInputSet, self)._set_input('Units', value)

class WriteDatastreamMetadataResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the WriteDatastreamMetadata Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_ResponseStatusCode(self):
        """
        Retrieve the value for the "ResponseStatusCode" output from this Choreo execution. ((integer) The response status code returned from Xively. For a successful datastream update, the code should be 200.)
        """
        return self._output.get('ResponseStatusCode', None)

class WriteDatastreamMetadataChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return WriteDatastreamMetadataResultSet(response, path)
