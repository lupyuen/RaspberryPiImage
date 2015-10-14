from temboo.Library.Google.Spreadsheets import AddListRows
from temboo.core.session import TembooSession

# Create a session with your Temboo account details
session = TembooSession("lupyuen", "myFirstApp", "2e0421546ea248d4a5cd2029f2979e23")

# Instantiate the Choreo
addListRowsChoreo = AddListRows(session)

# Get an InputSet object for the Choreo
addListRowsInputs = addListRowsChoreo.new_input_set()

# Set credential to use for execution
addListRowsInputs.set_credential('SensorData')

# Set the data to be added
addListRowsInputs.set_RowsetXML("""
<rowset>
<row>
<Timestamp>2015-08-19 02:26:21</Timestamp>
<Temperature>27.5</Temperature>
<Humidity>76</Humidity>
<LightLevel>74</LightLevel>
<SoundLevel>74</SoundLevel>
</row>
</rowset>
""")

# Execute the Choreo
addListRowsResults = addListRowsChoreo.execute_with_results(addListRowsInputs)

# Print the Choreo outputs
print("Response: " + addListRowsResults.get_Response())
print("NewAccessToken: " + addListRowsResults.get_NewAccessToken())
