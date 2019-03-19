from bluepy.sensortag import SensorTag

connected = False


def connect(address):
    global connected
    try:
        sensor_tag = SensorTag(address)
        debug("Connection successful to device " + address)
        connected = True
        return sensor_tag
    except Exception as ex:
        debug(ex.message)


def disconnect(sensor_tag):
    if connected:
        sensor_tag.disconnect()
        debug("Disconnect successful")


def debug(message):
    print "DEBUG | " + message


def main():
    sensor_tag_address = "CC:78:AB:7F:7B:87"
    sensor_tag = connect(sensor_tag_address)
    disconnect(sensor_tag)
    debug("End of test")


if __name__ == "__main__":
    main()