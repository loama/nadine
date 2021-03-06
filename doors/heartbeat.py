import sys
import time
import threading

from core import Messages

class HeartBeat(threading.Thread):


    def __init__(self, connection, poll_delay_sec):
        threading.Thread.__init__(self)
        self.connection = connection
        self.poll_delay_sec = poll_delay_sec
        self.new_data = False


    def run(self):
        self.running = True
        print("Polling every %d seconds" % self.poll_delay_sec)

        while self.running:
            if not self.new_data:
                print("Contacting the Keymaster...")
                response = self.connection.send_message(Messages.CHECK_DOOR_CODES)
                if response == Messages.NEW_DATA:
                    print("There is new data to be processed")
                    self.new_data = True
                else:
                    print("No new door codes")
            
            time.sleep(self.poll_delay_sec)


    def all_clear(self):
        response = self.connection.send_message(Messages.MARK_SUCCESS)
        if not response == Messages.SUCCESS_RESPONSE:
            raise Exception("Did not receive proper success response!")
        self.new_data = False


    def stop(self):
        self.poll_delay_sec = 0.1
        self.running = False