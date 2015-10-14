# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateProduct
# Updates an existing product batch.
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

class UpdateProduct(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateProduct Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(UpdateProduct, self).__init__(temboo_session, '/Library/Xively/Products/UpdateProduct')


    def new_input_set(self):
        return UpdateProductInputSet()

    def _make_result_set(self, result, path):
        return UpdateProductResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateProductChoreographyExecution(session, exec_id, path)

class UpdateProductInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateProduct
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Xively.)
        """
        super(UpdateProductInputSet, self)._set_input('APIKey', value)
    def set_CustomProduct(self, value):
        """
        Set the value of the CustomProduct input for this Choreo. ((optional, json) Optional custom configuration for creating your product in JSON. If you use this field the other optional parameters will be ignored. See Choreo description and Xively documentation for details.)
        """
        super(UpdateProductInputSet, self)._set_input('CustomProduct', value)
    def set_Datastreams(self, value):
        """
        Set the value of the Datastreams input for this Choreo. ((optional, json) Default device datastream JSON array. Every newly created device in this product will have this default datastream. Ex: [{"id":"channel1"},{"id":"demo"}].)
        """
        super(UpdateProductInputSet, self)._set_input('Datastreams', value)
    def set_Description(self, value):
        """
        Set the value of the Description input for this Choreo. ((optional, string) Description of the product.)
        """
        super(UpdateProductInputSet, self)._set_input('Description', value)
    def set_Name(self, value):
        """
        Set the value of the Name input for this Choreo. ((optional, string) Name of the product.)
        """
        super(UpdateProductInputSet, self)._set_input('Name', value)
    def set_Private(self, value):
        """
        Set the value of the Private input for this Choreo. ((optional, string) Default device feed privacy settings. Valid values: "true", "false" (default). Note - leaving this blank will automatically change a private device feed to a public device feed.)
        """
        super(UpdateProductInputSet, self)._set_input('Private', value)
    def set_ProductID(self, value):
        """
        Set the value of the ProductID input for this Choreo. ((required, string) The ID of the product you are trying to update.)
        """
        super(UpdateProductInputSet, self)._set_input('ProductID', value)

class UpdateProductResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateProduct Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_ResponseStatusCode(self):
        """
        Retrieve the value for the "ResponseStatusCode" output from this Choreo execution. ((integer) The response status code returned from Xively. For a successful product update, the code should be 200.)
        """
        return self._output.get('ResponseStatusCode', None)

class UpdateProductChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UpdateProductResultSet(response, path)
