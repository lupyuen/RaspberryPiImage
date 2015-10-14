# -*- coding: utf-8 -*-

###############################################################################
#
# GetReportRequestList
# Returns a list of report requests that you can use to get the ReportProcessingStatus and ReportId in order to retrieve a report.
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

class GetReportRequestList(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetReportRequestList Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetReportRequestList, self).__init__(temboo_session, '/Library/Amazon/Marketplace/Reports/GetReportRequestList')


    def new_input_set(self):
        return GetReportRequestListInputSet()

    def _make_result_set(self, result, path):
        return GetReportRequestListResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetReportRequestListChoreographyExecution(session, exec_id, path)

class GetReportRequestListInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetReportRequestList
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(GetReportRequestListInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSMarketplaceId(self, value):
        """
        Set the value of the AWSMarketplaceId input for this Choreo. ((required, string) The Marketplace ID provided by Amazon Web Services.)
        """
        super(GetReportRequestListInputSet, self)._set_input('AWSMarketplaceId', value)
    def set_AWSMerchantId(self, value):
        """
        Set the value of the AWSMerchantId input for this Choreo. ((required, string) The Merchant ID provided by Amazon Web Services.)
        """
        super(GetReportRequestListInputSet, self)._set_input('AWSMerchantId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(GetReportRequestListInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_Endpoint(self, value):
        """
        Set the value of the Endpoint input for this Choreo. ((conditional, string) The base URL for the MWS endpoint. Defaults to mws.amazonservices.co.uk.)
        """
        super(GetReportRequestListInputSet, self)._set_input('Endpoint', value)
    def set_MWSAuthToken(self, value):
        """
        Set the value of the MWSAuthToken input for this Choreo. ((optional, string) The Amazon MWS authorization token for the given seller and developer.)
        """
        super(GetReportRequestListInputSet, self)._set_input('MWSAuthToken', value)
    def set_MaxCount(self, value):
        """
        Set the value of the MaxCount input for this Choreo. ((optional, integer) A non-negative integer that represents the maximum number of report requests to return. Defaults to 10. Max is 100.)
        """
        super(GetReportRequestListInputSet, self)._set_input('MaxCount', value)
    def set_ReportProcessingStatusList(self, value):
        """
        Set the value of the ReportProcessingStatusList input for this Choreo. ((optional, string) A comma separated list of up to three ReportProcessingStatuses by which to filter report requests.)
        """
        super(GetReportRequestListInputSet, self)._set_input('ReportProcessingStatusList', value)
    def set_ReportRequestIdList(self, value):
        """
        Set the value of the ReportRequestIdList input for this Choreo. ((optional, string) A comma separated list of up to three ReportRequestId values. If you pass in a ReportRequestId values, other query conditions are ignored.)
        """
        super(GetReportRequestListInputSet, self)._set_input('ReportRequestIdList', value)
    def set_ReportTypeList(self, value):
        """
        Set the value of the ReportTypeList input for this Choreo. ((optional, string) A comma separated list of up to three ReportType enumeration values.)
        """
        super(GetReportRequestListInputSet, self)._set_input('ReportTypeList', value)
    def set_RequestedFromDate(self, value):
        """
        Set the value of the RequestedFromDate input for this Choreo. ((optional, date) The start of the date range used for selecting the data to report, in ISO8601 date format (i.e. 2012-01-01).)
        """
        super(GetReportRequestListInputSet, self)._set_input('RequestedFromDate', value)
    def set_RequestedToDate(self, value):
        """
        Set the value of the RequestedToDate input for this Choreo. ((optional, date) The end of the date range used for selecting the data to report, in ISO8601 date format (i.e. 2012-01-01).)
        """
        super(GetReportRequestListInputSet, self)._set_input('RequestedToDate', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        super(GetReportRequestListInputSet, self)._set_input('ResponseFormat', value)

class GetReportRequestListResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetReportRequestList Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (Stores the response from Amazon.)
        """
        return self._output.get('Response', None)
    def get_GeneratedReportId(self):
        """
        Retrieve the value for the "GeneratedReportId" output from this Choreo execution. ((integer) The GeneratedReportId parsed from the Amazon response. If multiple records are returned, this output variable will contain the first id in the list.)
        """
        return self._output.get('GeneratedReportId', None)
    def get_ReportProcessingStatus(self):
        """
        Retrieve the value for the "ReportProcessingStatus" output from this Choreo execution. ((string) The report status parsed from the Amazon response. If multiple records are returned, this output variable will contain the report status in the list.)
        """
        return self._output.get('ReportProcessingStatus', None)
    def get_ReportRequestId(self):
        """
        Retrieve the value for the "ReportRequestId" output from this Choreo execution. ((integer) The report request id parsed from the Amazon response. If multiple records are returned, this output variable will contain the first id in the list.)
        """
        return self._output.get('ReportRequestId', None)

class GetReportRequestListChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetReportRequestListResultSet(response, path)
