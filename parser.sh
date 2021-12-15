
#!/bin/bash
topic_throttle_report="/vehicle/throttle_report"
throttle_report_output="/home/kedar/Downloads/Pedal_Analysis/throttle_report.txt"
topic_vehicle_dynamic="/vehicle/vehicle_dynamic"
vehicle_dynamic_output="/home/kedar/Downloads/Pedal_Analysis/dynamic_report.txt"
topic_wheel_speed="/vehicle/wheel_speed_report"
wheel_speed_output="/home/kedar/Downloads/Pedal_Analysis/wheel_speed_report.txt"
topic_dbw_enabled="/vehicle/dbw_enabled"
dbw_enabled_output="/home/kedar/Downloads/Pedal_Analysis/dbw_enabled_report.txt"


function generate_outputs {
    read -p "Please type path to the bag file ..." path_to_bag

    plusecho -b $path_to_bag $topic_throttle_report 2> $throttle_report_output
    plusecho -b $path_to_bag $topic_vehicle_dynamic 2> $vehicle_dynamic_output
    plusecho -b $path_to_bag $topic_wheel_speed 2> $wheel_speed_output
    plusecho -b $path_to_bag $topic_dbw_enabled 2> $dbw_enabled_output
}

generate_outputs

#python3 parser.py