# Pultrusion kinematics support (for Polyformer, Filaminter, etc)
#
# Copyright (C) 2018-2021  Kevin O'Connor <kevin@koconnor.net>
# @author Chris Wilder <wilder.christopher@gmail.com>
#
# This file may be distributed under the terms of the GNU GPLv3 license.
#
"""
TODO: Move this text to a markdown file

**Issues**
FIXME: MCU crashes when setting the hot end temperature to 50C. The error message is "ADC out of range"
FIXME: Unable to control the extruder fan

**Kinematics**
TODO: Add constant rotation for the extruder stepper

**Command and control**
TODO: Add custom gcode to toggle extruder stepper rotation, set speed, velocity, direction; this is for constant rotation
TODO: Add custom gcode to toggle heater
TODO: Add custom gcode to start/stop pultrusion (main op); spool rotation, heater, and fan

**Stability**
TODO: Figure out correction coef for stepper kinematics.
TODO: Figure out correction coef for heater
TODO: Get the gearbox ratio and the microsteps for my stepper
TODO: Figure out optimal pultrusion settings: motor, heater(200C), and fan

------------------------------------------------------------------------------------------------
What to add to PultrusionKinematics to make the Polymake Filaminter work
------------------------------------------------------------------------------------------------
 - Add default `trapq` definition; trapazoid stepper velocity/acceleration pattern
 - Is a `chelper` file needed for this device and for what?

------------------------------------------------------------------------------------------------
Ideas
------------------------------------------------------------------------------------------------
 - Physics (additional metrics)
    - pull strength
    - material stretch
    - filament production rate
 - Quality control
    - Measure and track filament diameter
 - Dual hotends
 - filament winder
 - hopper & grinder for recycling old prints
 - laythe-like bottle cutter

"""

class PultrusionKinematics:
    def __init__(self, toolhead, config):
        self.axes_minmax = toolhead.Coord(0., 0., 0., 0.)
    def get_steppers(self):
        return []
    def calc_position(self, stepper_positions):
        return [0, 0, 0]
    def set_position(self, newpos, homing_axes):
        pass
    def home(self, homing_state):
        pass
    def check_move(self, move):
        """ Verify if the move is valid. Any error will prevent further processing
        """
        pass
    def get_status(self, eventtime):
        return {
            'homed_axes': '',
            'axis_minimum': self.axes_minmax,
            'axis_maximum': self.axes_minmax,
        }

def load_kinematics(toolhead, config):
    return PultrusionKinematics(toolhead, config)
