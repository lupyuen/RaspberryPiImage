# -*- coding: utf-8 -*-

###############################################################################
#
# PublishLink
# Publishes a link on a given profile.
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

class PublishLink(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the PublishLink Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(PublishLink, self).__init__(temboo_session, '/Library/Facebook/Publishing/PublishLink')


    def new_input_set(self):
        return PublishLinkInputSet()

    def _make_result_set(self, result, path):
        return PublishLinkResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PublishLinkChoreographyExecution(session, exec_id, path)

class PublishLinkInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the PublishLink
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved from the final step of the OAuth process.)
        """
        super(PublishLinkInputSet, self)._set_input('AccessToken', value)
    def set_Caption(self, value):
        """
        Set the value of the Caption input for this Choreo. ((optional, string) Deprecated (retained for backward compatibility only).)
        """
        super(PublishLinkInputSet, self)._set_input('Caption', value)
    def set_Description(self, value):
        """
        Set the value of the Description input for this Choreo. ((optional, string) Deprecated (retained for backward compatibility only).)
        """
        super(PublishLinkInputSet, self)._set_input('Description', value)
    def set_Link(self, value):
        """
        Set the value of the Link input for this Choreo. ((required, string) The link to publish.)
        """
        super(PublishLinkInputSet, self)._set_input('Link', value)
    def set_Message(self, value):
        """
        Set the value of the Message input for this Choreo. ((optional, string) A message about the link.)
        """
        super(PublishLinkInputSet, self)._set_input('Message', value)
    def set_Name(self, value):
        """
        Set the value of the Name input for this Choreo. ((optional, string) Deprecated (retained for backward compatibility only).)
        """
        super(PublishLinkInputSet, self)._set_input('Name', value)
    def set_Picture(self, value):
        """
        Set the value of the Picture input for this Choreo. ((optional, string) Deprecated (retained for backward compatibility only).)
        """
        super(PublishLinkInputSet, self)._set_input('Picture', value)
    def set_ProfileID(self, value):
        """
        Set the value of the ProfileID input for this Choreo. ((optional, string) The id of the profile that the link will be published to. Defaults to "me" indicating the authenticated user.)
        """
        super(PublishLinkInputSet, self)._set_input('ProfileID', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to json.)
        """
        super(PublishLinkInputSet, self)._set_input('ResponseFormat', value)

class PublishLinkResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the PublishLink Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Facebook. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        return self._output.get('Response', None)

class PublishLinkChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return PublishLinkResultSet(response, path)
