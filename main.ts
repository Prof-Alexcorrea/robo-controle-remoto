bluetooth.onBluetoothConnected(function () {
    basic.showIcon(IconNames.Happy)
})
bluetooth.onBluetoothDisconnected(function () {
    basic.showIcon(IconNames.No)
})
bluetooth.onUartDataReceived(serial.delimiters(Delimiters.NewLine), function () {
    receivedString = bluetooth.uartReadUntil(serial.delimiters(Delimiters.NewLine))
    if (receivedString == "up") {
        pins.servoWritePin(AnalogPin.P0, 180)
        pins.servoWritePin(AnalogPin.P1, 0)
    }
    if (receivedString == "down") {
        pins.servoWritePin(AnalogPin.P0, 0)
        pins.servoWritePin(AnalogPin.P1, 180)
    }
    if (receivedString == "rigth") {
        pins.servoWritePin(AnalogPin.P0, 180)
        pins.servoWritePin(AnalogPin.P1, 180)
    }
    if (receivedString == "left") {
        pins.servoWritePin(AnalogPin.P0, 0)
        pins.servoWritePin(AnalogPin.P1, 0)
    }
    if (receivedString == "stop") {
        pins.servoWritePin(AnalogPin.P0, 90)
        pins.servoWritePin(AnalogPin.P1, 90)
    }
    if (receivedString.charAt(0) == "x") {
        pins.servoWritePin(AnalogPin.P2, parseFloat(receivedString.substr(1, 3)))
        if (receivedString.charAt(0) == "c") {
            pins.servoWritePin(AnalogPin.P2, parseFloat(receivedString.substr(1, 3)))
        }
    }
})
let receivedString = ""
bluetooth.startUartService()
basic.showIcon(IconNames.Square)
