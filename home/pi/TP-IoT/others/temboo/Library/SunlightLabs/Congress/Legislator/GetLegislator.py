# -*- coding: utf-8 -*-

###############################################################################
#
# GetLegislator
# Returns information for a particular member with a given identifier.
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

class GetLegislator(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetLegislator Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetLegislator, self).__init__(temboo_session, '/Library/SunlightLabs/Congress/Legislator/GetLegislator')


    def new_input_set(self):
        return GetLegislatorInputSet()

    def _make_result_set(self, result, path):
        return GetLegislatorResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetLegislatorChoreographyExecution(session, exec_id, path)

class GetLegislatorInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetLegislator
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Sunlight Labs.)
        """
        super(GetLegislatorInputSet, self)._set_input('APIKey', value)
    def set_AllLegislators(self, value):
        """
        Set the value of the AllLegislators input for this Choreo. ((optional, boolean) A boolean flag indicating to search for all legislators even when they are no longer in office.)
        """
        super(GetLegislatorInputSet, self)._set_input('AllLegislators', value)
    def set_BioguideID(self, value):
        """
        Set the value of the BioguideID input for this Choreo. ((conditional, string) The bioguide_id of the legislator to return.)
        """
        super(GetLegislatorInputSet, self)._set_input('BioguideID', value)
    def set_CRPID(self, value):
        """
        Set the value of the CRPID input for this Choreo. ((optional, string) The crp_id associated with a legislator to return.)
        """
        super(GetLegislatorInputSet, self)._set_input('CRPID', value)
    def set_FECID(self, value):
        """
        Set the value of the FECID input for this Choreo. ((optional, string) The fec_id associated with the legislator to return.)
        """
        super(GetLegislatorInputSet, self)._set_input('FECID', value)
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, string) A comma-separated list of fields to include in the response.)
        """
        super(GetLegislatorInputSet, self)._set_input('Fields', value)
    def set_GovTrackID(self, value):
        """
        Set the value of the GovTrackID input for this Choreo. ((optional, string) The govetrack_id associated with a legistlator to return.)
        """
        super(GetLegislatorInputSet, self)._set_input('GovTrackID', value)
    def set_ICPSRID(self, value):
        """
        Set the value of the ICPSRID input for this Choreo. ((optional, string) Identifier for this member as it is maintained by the Inter-university Consortium for Political and Social Research.)
        """
        super(GetLegislatorInputSet, self)._set_input('ICPSRID', value)
    def set_LISID(self, value):
        """
        Set the value of the LISID input for this Choreo. ((optional, string) Identifier for this member as it appears on some of Congress' data systems (namely Senate votes).)
        """
        super(GetLegislatorInputSet, self)._set_input('LISID', value)
    def set_OCDID(self, value):
        """
        Set the value of the OCDID input for this Choreo. ((optional, string) Identifier for this member across all countries and levels of government, as defined by the Open Civic Data project.)
        """
        super(GetLegislatorInputSet, self)._set_input('OCDID', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        super(GetLegislatorInputSet, self)._set_input('ResponseFormat', value)
    def set_ThomasID(self, value):
        """
        Set the value of the ThomasID input for this Choreo. ((optional, string) Identifier for this member as it appears on THOMAS.gov and Congress.gov.)
        """
        super(GetLegislatorInputSet, self)._set_input('ThomasID', value)
    def set_VoteSmartID(self, value):
        """
        Set the value of the VoteSmartID input for this Choreo. ((optional, integer) The votesmart_id of a legislator to return.)
        """
        super(GetLegislatorInputSet, self)._set_input('VoteSmartID', value)

class GetLegislatorResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetLegislator Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from the Sunlight Congress API.)
        """
        return self._output.get('Response', None)

class GetLegislatorChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetLegislatorResultSet(response, path)
