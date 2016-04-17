# -*- coding: utf-8 -*-

###############################################################################
#
# GetFeedSubmissionList
# Returns a list of all feed submissions submitted in the previous 90 days.
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

class GetFeedSubmissionList(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetFeedSubmissionList Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetFeedSubmissionList, self).__init__(temboo_session, '/Library/Amazon/Marketplace/Feeds/GetFeedSubmissionList')


    def new_input_set(self):
        return GetFeedSubmissionListInputSet()

    def _make_result_set(self, result, path):
        return GetFeedSubmissionListResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetFeedSubmissionListChoreographyExecution(session, exec_id, path)

class GetFeedSubmissionListInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetFeedSubmissionList
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(GetFeedSubmissionListInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSMarketplaceId(self, value):
        """
        Set the value of the AWSMarketplaceId input for this Choreo. ((required, string) The Marketplace ID provided by Amazon Web Services.)
        """
        super(GetFeedSubmissionListInputSet, self)._set_input('AWSMarketplaceId', value)
    def set_AWSMerchantId(self, value):
        """
        Set the value of the AWSMerchantId input for this Choreo. ((required, string) The Merchant ID provided by Amazon Web Services.)
        """
        super(GetFeedSubmissionListInputSet, self)._set_input('AWSMerchantId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(GetFeedSubmissionListInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_Endpoint(self, value):
        """
        Set the value of the Endpoint input for this Choreo. ((conditional, string) The base URL for the MWS endpoint. Defaults to mws.amazonservices.co.uk.)
        """
        super(GetFeedSubmissionListInputSet, self)._set_input('Endpoint', value)
    def set_FeedProcessingStatusList(self, value):
        """
        Set the value of the FeedProcessingStatusList input for this Choreo. ((optional, string) A comma separated list of one or more feed processing statuses by which to filter the list of feed submissions.)
        """
        super(GetFeedSubmissionListInputSet, self)._set_input('FeedProcessingStatusList', value)
    def set_FeedSubmissionIdList(self, value):
        """
        Set the value of the FeedSubmissionIdList input for this Choreo. ((optional, string) A comma separated list of FeedSubmmissionId values. If you pass in FeedSubmmissionId values in a request, other query conditions are ignored.)
        """
        super(GetFeedSubmissionListInputSet, self)._set_input('FeedSubmissionIdList', value)
    def set_FeedTypeList(self, value):
        """
        Set the value of the FeedTypeList input for this Choreo. ((optional, string) A comma separated list of one or more FeedType enumeration values by which to filter the list of feed submissions.)
        """
        super(GetFeedSubmissionListInputSet, self)._set_input('FeedTypeList', value)
    def set_MWSAuthToken(self, value):
        """
        Set the value of the MWSAuthToken input for this Choreo. ((optional, string) The Amazon MWS authorization token for the given seller and developer.)
        """
        super(GetFeedSubmissionListInputSet, self)._set_input('MWSAuthToken', value)
    def set_MaxCount(self, value):
        """
        Set the value of the MaxCount input for this Choreo. ((optional, integer) A non-negative integer that indicates the maximum number of feed submissions to return in the list. Defaults to 10. Max is 100.)
        """
        super(GetFeedSubmissionListInputSet, self)._set_input('MaxCount', value)
    def set_SubmittedFromDate(self, value):
        """
        Set the value of the SubmittedFromDate input for this Choreo. ((optional, date) The earliest submission date that you are looking for, in ISO8601 date format (i.e. 2012-01-01).)
        """
        super(GetFeedSubmissionListInputSet, self)._set_input('SubmittedFromDate', value)
    def set_SubmittedToDate(self, value):
        """
        Set the value of the SubmittedToDate input for this Choreo. ((optional, date) The latest submission date that you are looking for, in ISO8601 date format (i.e. 2012-01-01).)
        """
        super(GetFeedSubmissionListInputSet, self)._set_input('SubmittedToDate', value)

class GetFeedSubmissionListResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetFeedSubmissionList Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) Stores the response from Amazon.)
        """
        return self._output.get('Response', None)
    def get_FeedProcessingStatus(self):
        """
        Retrieve the value for the "FeedProcessingStatus" output from this Choreo execution. ((string) The FeedProcessingStatus parsed from the Amazon response.)
        """
        return self._output.get('FeedProcessingStatus', None)
    def get_FeedSubmissionId(self):
        """
        Retrieve the value for the "FeedSubmissionId" output from this Choreo execution. ((integer) The FeedSubmissionId parsed from the Amazon response. If multiple records are returned, this output variable will contain the first id in the list.)
        """
        return self._output.get('FeedSubmissionId', None)

class GetFeedSubmissionListChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetFeedSubmissionListResultSet(response, path)
