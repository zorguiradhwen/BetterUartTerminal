# BetterUartTerminal
A uart terminal intended to communicate with an embedded target and provide an easy way to create custom commads executable inside the target


PLANNING:
    + Dependencies:
        - Serial
        - QT
        
    + Modules:
        - Serial_Console
        - command parser: used to preprocess commands to execute them on host or encode them and send them to MCU
        - basic host commands
        - frame encoder/decoder: encode and decode frames to and from MCU
        - logger and data display
        - scriptinterpretor (send and receive commands automatically with a written scripter)
        
        
    
    + Development:
        1. Serial Console:
            * basic funcs:
                  - list available ports:
                  - connect and disconnect ports and handle exceptions
                  - send and receive   
                  
                  
                  