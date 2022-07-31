# Responder usage example

import tinytuya
from magichome.magichome import MagicHomeApi
import firebase_admin
from firebase_admin import credentials, db
import tracemalloc
from responder import ResponderClass, ResponderDevice

sw1 = tinytuya.OutletDevice('', '', '')

led1 = MagicHomeApi('', 1)
led2 = MagicHomeApi('', 1)

cred = credentials.Certificate("")
default_app = firebase_admin.initialize_app(cred, {
    'databaseURL': ''
})


def main():
    sw1.set_version()
    # Default value of 0
    rc = ResponderClass(0)

    # Trigger value of 1, no inversion
    rc.add(ResponderDevice(1, False, led1.turn_on))
    rc.add(ResponderDevice(1, False, led2.turn_on))
    # Trigger value of 1, no inversion, delay of 3500ms before turning back off
    rc.add(ResponderDevice(1, False, sw1.turn_on, sw1.turn_off, 3500))

    # Register firebase callback as rc.main
    firebase_admin.db.reference('path/to/trigger/value').listen(rc.handler)


if __name__ == "__main__":
    main()
