# -*- coding: utf-8 -*-

###############################################################################
#
# CancelReportRequest
# Cancels one or more report requests.
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

class CancelReportRequest(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CancelReportRequest Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CancelReportRequest, self).__init__(temboo_session, '/Library/Amazon/Marketplace/Reports/CancelReportRequest')


    def new_input_set(self):
        return CancelReportRequestInputSet()

    def _make_result_set(self, result, path):
        return CancelReportRequestResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CancelReportRequestChoreographyExecution(session, exec_id, path)

class CancelReportRequestInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CancelReportRequest
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(CancelReportRequestInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSMarketplaceId(self, value):
        """
        Set the value of the AWSMarketplaceId input for this Choreo. ((required, string) The Marketplace ID provided by Amazon Web Services.)
        """
        super(CancelReportRequestInputSet, self)._set_input('AWSMarketplaceId', value)
    def set_AWSMerchantId(self, value):
        """
        Set the value of the AWSMerchantId input for this Choreo. ((required, string) The Merchant ID provided by Amazon Web Services.)
        """
        super(CancelReportRequestInputSet, self)._set_input('AWSMerchantId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(CancelReportRequestInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_Endpoint(self, value):
        """
        Set the value of the Endpoint input for this Choreo. ((conditional, string) The base URL for the MWS endpoint. Defaults to mws.amazonservices.co.uk.)
        """
        super(CancelReportRequestInputSet, self)._set_input('Endpoint', value)
    def set_MWSAuthToken(self, value):
        """
        Set the value of the MWSAuthToken input for this Choreo. ((optional, string) The Amazon MWS authorization token for the given seller and developer.)
        """
        super(CancelReportRequestInputSet, self)._set_input('MWSAuthToken', value)
    def set_ReportProcessingStatus(self, value):
        """
        Set the value of the ReportProcessingStatus input for this Choreo. ((optional, string) A report processing status by which to filter report requests. Valid values are: _SUBMITTED_, _IN_PROGRESS_, _CANCELLED_, _DONE_, _DONE_NO_DATA_.)
        """
        super(CancelReportRequestInputSet, self)._set_input('ReportProcessingStatus', value)
    def set_ReportRequestId(self, value):
        """
        Set the value of the ReportRequestId input for this Choreo. ((optional, string) A ReportRequestId value. If you pass in a ReportRequestId value, other query conditions are ignored.)
        """
        super(CancelReportRequestInputSet, self)._set_input('ReportRequestId', value)
    def set_ReportType(self, value):
        """
        Set the value of the ReportType input for this Choreo. ((optional, string) A ReportType enumeration value (i.e. GET_ORDERS_DATA_).)
        """
        super(CancelReportRequestInputSet, self)._set_input('ReportType', value)
    def set_RequestedFromDate(self, value):
        """
        Set the value of the RequestedFromDate input for this Choreo. ((optional, date) The start of the date range used for selecting the data to report, in ISO8601 date format (i.e. 2012-01-01).)
        """
        super(CancelReportRequestInputSet, self)._set_input('RequestedFromDate', value)
    def set_RequestedToDate(self, value):
        """
        Set the value of the RequestedToDate input for this Choreo. ((optional, date) The end of the date range used for selecting the data to report, in ISO8601 date format (i.e. 2012-01-01).)
        """
        super(CancelReportRequestInputSet, self)._set_input('RequestedToDate', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        super(CancelReportRequestInputSet, self)._set_input('ResponseFormat', value)

class CancelReportRequestResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CancelReportRequest Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (Stores the response from Amazon.)
        """
        return self._output.get('Response', None)
    def get_Count(self):
        """
        Retrieve the value for the "Count" output from this Choreo execution. ((integer) A non-negative integer that represents the total number of report requests that were cancelled.)
        """
        return self._output.get('Count', None)

class CancelReportRequestChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CancelReportRequestResultSet(response, path)
