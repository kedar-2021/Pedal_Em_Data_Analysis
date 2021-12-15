import matplotlib.pyplot as plt

print("Enter pedal input file name")
input_file = input()
throttle_report = "/home/kedar/Downloads/Pedal_Analysis/throttle_report.txt"

pedal_cmd = []
pedal_inp = []
pedal_out = []
timeS = []
timeNS = []
with open(throttle_report) as f:
    for line in f:
        x = list(line.strip().split(':'))
        if x[0] == 'pedal_cmd':
            pedal_cmd.append(float(x[1])*2)
        elif x[0] == 'secs':
            timeS.append(int(x[1]))
        elif x[0] == 'nsecs':
            timeNS.append(int(x[1]))
        elif x[0] == 'pedal_output':
            pedal_out.append(float(x[1]))
        elif x[0] == 'pedal_input':
            pedal_inp.append(float(x[1]))

realT_Throttle = []

for i in range(len(timeS)):

    realT_Throttle.append(float(timeS[i] + timeNS[i] * pow(10,-9)))

plt.subplot(8, 1, 1)
plt.plot(realT_Throttle, pedal_cmd, label = "pedal command", color='red')
plt.legend()
plt.subplot(8, 1, 2)
plt.plot(realT_Throttle, pedal_inp, label = "pedal input", color='green')
plt.legend()
plt.subplot(8, 1, 3)
plt.plot(realT_Throttle, pedal_out, label = "pedal output", color='blue')
plt.legend()
vehicle_dynamic = "/home/kedar/Downloads/Pedal_Analysis/dynamic_report.txt"

linear_acceleration = []
timeS = []
timeNS = []
with open(vehicle_dynamic) as f:
    for line in f:
        x = list(line.strip().split(':'))
        if x[0] == 'linear_acceleration':
            linear_acceleration.append(x[1])
        elif x[0] == 'secs':
            timeS.append(int(x[1]))
        elif x[0] == 'nsecs':
            timeNS.append(int(x[1]))
realT_Dynamic = []

for i in range(len(timeS)):

    realT_Dynamic.append(float(timeS[i] + timeNS[i] * pow(10,-9)))

plt.subplot(8, 1, 4)
plt.plot(realT_Dynamic, linear_acceleration, label = "Linear Acceleration", color='lightcoral')
plt.legend()

wheel_speed_report = "/home/kedar/Downloads/Pedal_Analysis/wheel_speed_report.txt"

wheel_speed = []
timeS = []
timeNS = []
with open(wheel_speed_report) as f:
    for line in f:
        x = list(line.strip().split(':'))
        if x[0] == 'front_left':
            wheel_speed.append(float(x[1]))
        elif x[0] == 'secs':
            timeS.append(int(x[1]))
        elif x[0] == 'nsecs':
            timeNS.append(int(x[1]))
realT_WheelSpeed = []

for i in range(len(timeS)):

    realT_WheelSpeed.append(float(timeS[i] + timeNS[i] * pow(10,-9)))

plt.subplot(8, 1, 5)
plt.plot(realT_WheelSpeed, wheel_speed, label = "Wheel Speed", color='magenta')
plt.legend()


pedal_report = "/home/kedar/Downloads/Pedal_Analysis/pedal_input/" + input_file + ".txt"

ped_em_analog = []
ped_em_digital = []
ped_em_status = []
timeS = []
timeNS = []
with open(pedal_report) as f:
    for line in f:
        x = list(line.strip().split(':'))
        if x[0] == 'ped_em_analog':
            ped_em_analog.append(float(x[1]))
        elif x[0] == 'timestamp_msec':
            timeS.append(float(x[1]))
        elif x[0] == 'ped_em_digital':
            ped_em_digital.append(x[1])
        elif x[0] == 'ped_em_status':
            ped_em_status.append(x[1])

realT_Pedal = []

for i in range(len(timeS)):

    realT_Pedal.append(timeS[i])

plt.subplot(8, 1, 6)
plt.plot(realT_Pedal, ped_em_analog, label = "Analog In", color='lime')
plt.legend()
plt.subplot(8, 1, 7)
plt.plot(realT_Pedal, ped_em_digital, label = "Digital In", color='crimson')
plt.legend()
plt.subplot(8, 1, 8)
plt.plot(realT_Pedal, ped_em_status, label = "Pedal Status", color='deepskyblue')
plt.legend()

plt.show()
