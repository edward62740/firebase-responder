import asyncio
import time


class ResponderClass(object):
    """ ResponderClass contains all ResponderDevice instances. """

    def __init__(self, default):
        """ Initialize a ResponderClass instance with default value 0 (i.e do nothing if this value is received). """
        self.devices = []
        self.default = default

    def add(self, device):
        """ Add a ResponderDevice instance to the list of devices. """
        self.devices.append(device)

    async def _task(self, event):
        """ Asynchronously run respond() method for each instance of ResponderDevice. """
        print("began at {}".format(time.time()))
        await asyncio.wait([

            asyncio.create_task(device.respond(event.data))
            for device in self.devices
        ])

    def handler(self, event):
        """ Should be registered as callback for Firebase RTDB listener. """
        if event.data != self.default:
            asyncio.run(self._task(event))


class ResponderDevice(object):
    """ ResponderDevice contains device-specific information. """
    def __init__(self, trig, inversion, method_on, method_off=None, delay_ms=-1):
        """
        Initialize a ResponderDevice instance.
        :param trig: Trigger value of the device
        :param inversion: Inversion of the trigger value
        :param method_on: Method to call when trigger value is received
        :param method_off: Method to call when trigger value is received and delay_ms is set
        :param delay_ms: Delay in milliseconds
        """
        self.method_on = method_on
        self.method_off = method_off
        self.trig = trig
        self.inversion = inversion
        self.delay_ms = delay_ms

    async def respond(self, data):
        """ Internal call to turn on/off device. """
        if data == self.trig:
            self.method_on() if not self.inversion else self.method_off()
            if self.method_off is not None and self.delay_ms != -1:
                await asyncio.sleep(self.delay_ms / 1000)
                print("Delay {}ms".format(self.delay_ms))
                self.method_off() if not self.inversion else self.method_on()
                print("finished at {}".format(time.time()))
