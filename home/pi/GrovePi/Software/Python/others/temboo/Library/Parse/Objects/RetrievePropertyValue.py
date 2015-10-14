# -*- coding: utf-8 -*-

###############################################################################
#
# RetrievePropertyValue
# Retrieves the value for a given property contained within an object.
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

class RetrievePropertyValue(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RetrievePropertyValue Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(RetrievePropertyValue, self).__init__(temboo_session, '/Library/Parse/Objects/RetrievePropertyValue')


    def new_input_set(self):
        return RetrievePropertyValueInputSet()

    def _make_result_set(self, result, path):
        return RetrievePropertyValueResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrievePropertyValueChoreographyExecution(session, exec_id, path)

class RetrievePropertyValueInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RetrievePropertyValue
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_ApplicationID(self, value):
        """
        Set the value of the ApplicationID input for this Choreo. ((required, string) The Application ID provided by Parse.)
        """
        super(RetrievePropertyValueInputSet, self)._set_input('ApplicationID', value)
    def set_ClassName(self, value):
        """
        Set the value of the ClassName input for this Choreo. ((required, string) The class name for the object being retrieved.)
        """
        super(RetrievePropertyValueInputSet, self)._set_input('ClassName', value)
    def set_ObjectID(self, value):
        """
        Set the value of the ObjectID input for this Choreo. ((required, string) The ID of the object to retrieve.)
        """
        super(RetrievePropertyValueInputSet, self)._set_input('ObjectID', value)
    def set_PropertyName(self, value):
        """
        Set the value of the PropertyName input for this Choreo. ((required, string) The name of the property to return.)
        """
        super(RetrievePropertyValueInputSet, self)._set_input('PropertyName', value)
    def set_RESTAPIKey(self, value):
        """
        Set the value of the RESTAPIKey input for this Choreo. ((required, string) The REST API Key provided by Parse.)
        """
        super(RetrievePropertyValueInputSet, self)._set_input('RESTAPIKey', value)

class RetrievePropertyValueResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RetrievePropertyValue Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Value(self):
        """
        Retrieve the value for the "Value" output from this Choreo execution. ((string) The value of the specified property.)
        """
        return self._output.get('Value', None)

class RetrievePropertyValueChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return RetrievePropertyValueResultSet(response, path)
