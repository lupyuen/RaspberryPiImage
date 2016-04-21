'''
Assume /etc/wpa_supplicant/wpa_supplicant.conf contains:
<<
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
network={
    ssid="SSID1"
    ...
}
network={
    ...
>>

We insert the new SSID at the top, skip any duplicates later:
<<
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
# Inserted by update_wifi_config.py on DD-MM-YYYY HH:NN
network={
    ssid="NEW_SSID"
    ...
}
network={
    ssid="SSID1"
    ...
}
network={
    ...
>>

'''
import sys
import os
import re
import datetime
from shutil import copyfile

#new_config = 'pending_wifi_config_TP-Secure'
#new_config = 'pending_wifi_config_abc'
new_config = sys.argv[1]

config_filename = '/etc/wpa_supplicant/wpa_supplicant.conf'
temp_filename = '/tmp/update_wifi_config.tmp'
comment = '# Inserted by update_wifi_config.py on '
comment_trimmed = comment.replace(' ', '').replace('\t', '').replace('\n', '')

is_header = True
inserted_new_config = False

# Read the new network config.
with open(new_config, 'r') as new_config_lines:
    # Get the SSID of the new config so we can remove the duplicate: ssid="???"
    new_config_text = new_config_lines.read()
    match = re.search(r'ssid="(.+)"', new_config_text)
    new_ssid = match.group(1)
    print('Inserting SSID ' + new_ssid + '...')

    # Write the new wpa_supplicant.conf file to the temp file.
    with open(temp_filename, 'w') as out:
        with open(config_filename, 'r') as original_config:
            config = ''
            for line in original_config:

                # Copy the header lines.
                line_trimmed = line.replace(' ', '').replace('\t', '').replace('\n', '')
                if line_trimmed.startswith('network=') or \
                    line_trimmed.startswith(comment_trimmed):
                    is_header = False
                if is_header:
                    out.write(line)
                    continue

                # Copy the new network config.
                if not inserted_new_config:
                    out.write(comment + str(datetime.datetime.now()).split('.')[0])
                    out.write(new_config_text + '\n')
                    inserted_new_config = True

                # Accumulate the whole network config.
                config = config + line

                # If this is not the last line of the config, continue.
                if not line_trimmed.endswith('}'):
                    continue

                # If this config is same as new SSID, don't copy it.
                match = re.search(r'ssid="(.+)"', config)
                if not match:
                    out.write(config)
                    config = ''
                    continue
                current_ssid = match.group(1)
                if current_ssid == new_ssid:
                    print('Skipping previous version of SSID ' + current_ssid + '...')
                    config = ''
                    continue

                # Else copy the config.
                print('Copying SSID ' + current_ssid + '...')
                out.write(config)
                config = ''

                # End of loop.

            if not inserted_new_config:
                out.write(comment + str(datetime.datetime.now()).split('.')[0])
                out.write(new_config_text + '\n')

            # Write the rest of the lines.
            if config != '':
                out.write(config)

# Overwrite the original file.
copyfile(temp_filename, config_filename)
os.remove(temp_filename)

# Remove the new SSID config.
os.remove(new_config)
