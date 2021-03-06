#!/usr/bin/env python
import sys
import json
import time
import traceback

from core import Messages, EncryptedConnection, Gatekeeper
from heartbeat import HeartBeat

class GatekeeperApp(object):
    def run(self, config, syncClocks, initialSync):
        try:
            print "Starting up Gatekeeper..."
            connection = EncryptedConnection(config['ENCRYPTION_KEY'], config['KEYMASTER_URL'])
            gatekeeper = Gatekeeper(connection)
            
            # Test the connection
            response = connection.send_message(Messages.TEST_QUESTION)
            if response == Messages.TEST_RESPONSE:
                print "Connection successfull!"
            else:
                raise Exception("Could not connect to Keymaster")
            
            # Pull the configuration
            print "Pulling door configuration..."
            response = connection.send_message(Messages.PULL_CONFIGURATION)
            #print response
            gatekeeper.configure_doors(response)
            if len(gatekeeper.doors) == 0:
                print "No doors to program.  Exiting"
                return
            print "Configured %d doors" % len(gatekeeper.doors)
            
            # Set the time on each door
            if syncClocks:
                print "Syncing the door clocks..."
                gatekeeper.sync_clocks()
            
            # Pull new data if requested
            if initialSync:
                gatekeeper.pull_door_codes()
            
            try:
                heartbeat = None
                while True:
                    if not heartbeat or not heartbeat.is_alive():
                        print "Starting Heart Beat..."
                        heartbeat = HeartBeat(connection, config['POLL_DELAY_SEC'])
                        heartbeat.setDaemon(True)
                        heartbeat.start()
                
                    if heartbeat.new_data:
                        print "Pulling door codes..."
                        gatekeeper.pull_door_codes()
                        heartbeat.all_clear()
                
                    time.sleep(.1)
            except KeyboardInterrupt:
                print " Keyboard Interupt!"
                print "Shutting down..."
                if heartbeat and heartbeat.is_alive():
                    heartbeat.stop()
                    heartbeat.join()
                print "Done!"

        except Exception as e:
            traceback.print_exc()
            print "Error: %s" % str(e)


if __name__ == "__main__":
    # Pull the config
    with open('gw_config.json', 'r') as f:
        config = json.load(f)
    
    # Pull the command line args
    initialSync = "-s" in sys.argv
    syncClocks = "-c" in sys.argv

    # Start the application
    app = GatekeeperApp()
    app.run(config, syncClocks, initialSync)
