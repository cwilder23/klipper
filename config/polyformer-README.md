Polyformer Klipper configuration procedure
==========================================

__Control board:__ _Bigtree SKR Pico v1.0_
__Controller interface:__ _UART_
__Host system:__ _Raspberry Pi3_
__Host OS:__ MainsailOS

# MainsailOS + klipper

__Note:__ Install the firmware on the control board before wiring up the hardware.
1. Follow these instruction to setup the host device, build the firmware and flash the control board
  - TODO: Add URLs. Use MainsailOS image. RPi first and then control board
  - TODO: Configure MainsailOS via `Pi Imager`, so that it will be readily available on you local net
  - TODO: Add image and URL for setting up the the control board for flashing
2. Wire up the hardware. Follow the wiring diagram to guide you through the process. 
  - __NOTE:__ If you deviate from the wiring example, you will need to adjust the `printer.cfg` file accordingly
3. Boot the host and control board
  - It is a good time to verify the base system is working. At this point, _klipper_ will not be able to talk to the control board yet. 
4. Configure klipper
  1. Verify `printer-polyformer-filaminter.cfg` setup for your hardware. If you purchasd the hardware from the Polyformer BOM <TODO: Add URL>, 
    then no further changes are needed
  2. Upload the klipper configuration file, `printer-polyformer-filaminter.cfg` to the host system and rename the config file to `printer.cfg`:

```bash
  scp printer-polyformer-filaminter.cfg pi@polyminter.local:~/klipper_config/printer.cfg
```

  3. Open the MainSail Web app in a browser <http://filaminter.local>
  4. Use the web interface to restart _klipper_. This will load the config.
  6. AFter klipper loads the  config without errors and the host can talk to the control board, proceed to calibration.
5. PID Calibration (for extruder heater)
  1. Open the _G-Code console_ on the MainSail web UI
  2. Run the following g-code commands. This will take about 5 minutes to complete:

```
	PID_CALIBRATE HEATER=extruder TARGET=210 WRITE_FILE=1
	# Wait for klipper to complete the colibration procedure. ~5 minutes

    # Write the PID colibration coeff to the 'printer.cfg' file
	SAVE_CONFIG
23:43:59
PID parameters: pid_Kp=27.155 pid_Ki=1.403 pid_Kd=131.361
The SAVE_CONFIG command will update the printer config file
with these parameters and restart the printer.
23:39:13
  ```
  3. Edit `printer.cfg`, set the PID coeffs (`pid_Kp`, `pid_Ki`, `pid_Kd`) to the values that were just calculated. The computed PID coeffs are appended to the `printer.cfg` in a block comment
  4. Save teh config and restart _klipper_
6. Verify temperature stabiity


