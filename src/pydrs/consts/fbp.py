"""""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """''
======================================================================
                    Listas de Entidades BSMP
        A posição da entidade na lista corresponde ao seu ID BSMP
======================================================================
""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" ""

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
