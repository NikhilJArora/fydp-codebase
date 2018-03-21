import subprocess

cmd = "scp pi@raspi:/home/pi/dev/src/output.csv ~/data/fydp/pi_data/"
while True:
    subprocess.check_call([
                        'scp',
                        'pi@raspi:/home/pi/dev/src/output.csv',
                        '/Users/nikhilarora/data/fydp/pi_data/'
                        ])
