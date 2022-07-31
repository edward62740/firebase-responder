# I<sup>2</sup>DS Responder

Provides methods to trigger smart home device generic on/off calls from Firebase RTDB listener values. After passing method handler() as Firebase listener callback,
the added devices are asyncronously switched on/off based on the parameters:

```python
 responder.add(ResponderDevice(trig, inversion, method_on, method_off, delay_ms))

```
trig: Trigger value of the device\
inversion: Inversion of the trigger value\
method_on: Method to call when trigger value is received\
method_off: Method to call when trigger value is received and delay_ms is set\
delay_ms: Delay in milliseconds

Refer to main.py for example usage.
