-- Open the TCP connection
tcp.open()

-- Function to send data to the host PC
function sendData()
    while true do
        -- Read voltage, current, and power using the meter's API
        local voltage = meter.readVoltage()
        local current = meter.readCurrent()
        local power = meter.readPower()

        -- Format the data into a string
        local dataString = string.format("Voltage: %.2f V, Current: %.2f A, Power: %.2f W", voltage, current, power)

        -- Send the formatted string to the host PC over TCP
        tcp.write(dataString)

        -- Wait for a short period before sending the next set of readings
        -- Using delay.ms if available or any similar function
        delay.ms(1) -- Change the ms delay according to your need,less than this may cause the toolbox to hang
    end
end

-- Set up a callback function to run sendData when data is received (or use any trigger as per your requirement)
function tcp_callback()
    sendData()
end

tcp.onReceived(tcp_callback)
