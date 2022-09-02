# FBP
soft_interlocks = ["Heat-Sink Overtemperature"]

hard_interlocks = [
    "Load Overcurrent",
    "Load Overvoltage",
    "DCLink Overvoltage",
    "DCLink Undervoltage",
    "DCLink Relay Fault",
    "DCLink Fuse Fault",
    "MOSFETs Driver Fault",
    "Welded Relay Fault",
]

# FBP DC-Link
dclink_hard_interlocks = [
    "Power_Module_1_Fault",
    "Power_Module_2_Fault",
    "Power_Module_3_Fault",
    "Total_Output_Overvoltage",
    "Power_Module_1_Overvoltage",
    "Power_Module_2_Overvoltage",
    "Power_Module_3_Overvoltage",
    "Total_Output_Undervoltage",
    "Power_Module_1_Undervoltage",
    "Power_Module_2_Undervoltage",
    "Power_Module_3_Undervoltage",
    "Smoke_Detector",
    "External_Interlock",
]

bsmp_vars = {
    "load_current": {"addr": 33, "egu": "A"},
    "load_voltage": {"addr": 34, "egu": "V"},
    "dc_link_voltage": {"addr": 35, "egu": "V"},
    "heatsink_temp": {"addr": 36, "egu": "°C"},
    "duty_cycle": {"addr": 37, "egu": "%"},
}
