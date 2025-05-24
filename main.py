def on_bluetooth_connected():
    basic.show_icon(IconNames.HAPPY)
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_bluetooth_disconnected():
    basic.show_icon(IconNames.NO)
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)

def on_uart_data_received():
    global receivedString
    receivedString = bluetooth.uart_read_until(serial.delimiters(Delimiters.NEW_LINE))
    if receivedString == "up":
        pins.servo_write_pin(AnalogPin.P0, 180)
        pins.servo_write_pin(AnalogPin.P1, 0)
    if receivedString == "down":
        pins.servo_write_pin(AnalogPin.P0, 0)
        pins.servo_write_pin(AnalogPin.P1, 180)
    if receivedString == "rigth":
        pins.servo_write_pin(AnalogPin.P0, 180)
        pins.servo_write_pin(AnalogPin.P1, 180)
    if receivedString == "left":
        pins.servo_write_pin(AnalogPin.P0, 0)
        pins.servo_write_pin(AnalogPin.P1, 0)
    if receivedString == "stop":
        pins.servo_write_pin(AnalogPin.P0, 90)
        pins.servo_write_pin(AnalogPin.P1, 90)
    if receivedString.char_at(0) == "x":
        pins.servo_write_pin(AnalogPin.P2, parse_float(receivedString.substr(1, 3)))
        if receivedString.char_at(0) == "c":
            pins.servo_write_pin(AnalogPin.P2, parse_float(receivedString.substr(1, 3)))
bluetooth.on_uart_data_received(serial.delimiters(Delimiters.NEW_LINE),
    on_uart_data_received)

receivedString = ""
bluetooth.start_uart_service()
basic.show_icon(IconNames.SQUARE)