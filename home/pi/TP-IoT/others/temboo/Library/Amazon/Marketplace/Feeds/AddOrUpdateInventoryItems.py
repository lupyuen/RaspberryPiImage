# -*- coding: utf-8 -*-

###############################################################################
#
# AddOrUpdateInventoryItems
# Adds or updates one or more inventory listings in your Seller Central account with a given flat flile.
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

class AddOrUpdateInventoryItems(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the AddOrUpdateInventoryItems Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(AddOrUpdateInventoryItems, self).__init__(temboo_session, '/Library/Amazon/Marketplace/Feeds/AddOrUpdateInventoryItems')


    def new_input_set(self):
        return AddOrUpdateInventoryItemsInputSet()

    def _make_result_set(self, result, path):
        return AddOrUpdateInventoryItemsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AddOrUpdateInventoryItemsChoreographyExecution(session, exec_id, path)

class AddOrUpdateInventoryItemsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the AddOrUpdateInventoryItems
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_FeedData(self, value):
        """
        Set the value of the FeedData input for this Choreo. ((conditional, multiline) The feed data to sumbit to Amazon Marketplace.)
        """
        super(AddOrUpdateInventoryItemsInputSet, self)._set_input('FeedData', value)
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(AddOrUpdateInventoryItemsInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSMarketplaceId(self, value):
        """
        Set the value of the AWSMarketplaceId input for this Choreo. ((required, string) The Marketplace ID provided by Amazon Web Services.)
        """
        super(AddOrUpdateInventoryItemsInputSet, self)._set_input('AWSMarketplaceId', value)
    def set_AWSMerchantId(self, value):
        """
        Set the value of the AWSMerchantId input for this Choreo. ((required, string) The Merchant ID provided by Amazon Web Services.)
        """
        super(AddOrUpdateInventoryItemsInputSet, self)._set_input('AWSMerchantId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(AddOrUpdateInventoryItemsInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_Endpoint(self, value):
        """
        Set the value of the Endpoint input for this Choreo. ((conditional, string) The base URL for the MWS endpoint. Defaults to mws.amazonservices.co.uk.)
        """
        super(AddOrUpdateInventoryItemsInputSet, self)._set_input('Endpoint', value)
    def set_MWSAuthToken(self, value):
        """
        Set the value of the MWSAuthToken input for this Choreo. ((optional, string) The Amazon MWS authorization token for the given seller and developer.)
        """
        super(AddOrUpdateInventoryItemsInputSet, self)._set_input('MWSAuthToken', value)
    def set_TimeToWait(self, value):
        """
        Set the value of the TimeToWait input for this Choreo. ((optional, integer) By default, the Choreo will wait for 10 minutes to see if the report is ready for retrieval. Max is 120 minutes.)
        """
        super(AddOrUpdateInventoryItemsInputSet, self)._set_input('TimeToWait', value)


class AddOrUpdateInventoryItemsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the AddOrUpdateInventoryItems Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Amazon after submitting the feed.)
        """
        return self._output.get('Response', None)
    def get_ProcessingStatus(self):
        """
        Retrieve the value for the "ProcessingStatus" output from this Choreo execution. ((string) The processing status of the feed submission which is parsed from the Amazon response.)
        """
        return self._output.get('ProcessingStatus', None)
    def get_SubmissionId(self):
        """
        Retrieve the value for the "SubmissionId" output from this Choreo execution. ((integer) The submission id parsed from the Amazon response.)
        """
        return self._output.get('SubmissionId', None)
    def get_SubmissionResult(self):
        """
        Retrieve the value for the "SubmissionResult" output from this Choreo execution. ((string) The submission result returned from Amazon.)
        """
        return self._output.get('SubmissionResult', None)

class AddOrUpdateInventoryItemsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return AddOrUpdateInventoryItemsResultSet(response, path)
