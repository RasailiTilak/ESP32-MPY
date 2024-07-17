# ESP32-MPY
All the project  of the esp32 microcontroller programming using the micro python from crash.

# HOW TO FLASH THE ESP32 MICROPYTHON  FIRMWARE 
1. Download the latest version of the ESP32 MicroPython firmware(.bin) file, from the official website:[ https://](https://micropython.org/download/ESP32_GENERIC/)
## WINDOWS
- GO TO THE DOWNLOAD FOLDER
- CREATE THE NEW FOLDER AND PLACE THE (.bin ) INSIDE THE FOLDER
- OPEN THE TERMINAL
    # TERMINAL SECTION
    - create virtual env
    - py -m venv .venv
    - .venv\Scripts\activate
    - pip install esptool
    - esptool.exe --chip esp32 --port COM21 erase_flash // check  the COM PORT through the device manager
    HOLD BOOT BOTTON
    - esptool.exe --chip esp32 --port COM21 write_flash -z 0x1000 esp32-20190125-v1.10.bin // make sure your  COM PORT  and (.bin) file name are correct
    HOLD BOOT BOTTON



