"""Example for using pymysensors."""
import mysensors.mysensors as mysensors


def event(update_type, nid):
    """Callback for mysensors updates."""
    print(update_type + " " + str(nid))

# To create a serial gateway.
#GATEWAY = mysensors.SerialGateway(
#    '/dev/ttyACM0', event, protocol_version='2.0')

# To create a TCP gateway.
GATEWAY = mysensors.TCPGateway('192.168.1.84', event, True)

GATEWAY.debug = True
GATEWAY.start()
# To set sensor 1, child 1, sub-type V_LIGHT (= 2), with value 1.
# GATEWAY.set_child_value(1, 1, 2, 1)
# GATEWAY.stop()
