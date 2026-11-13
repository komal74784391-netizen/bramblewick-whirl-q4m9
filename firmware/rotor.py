"""Whirl rotor control and interlock handling."""

import json

import machine
import ramp

LID_PIN = machine.Pin(6, machine.Pin.IN, machine.Pin.PULL_UP)
DRIVER_ENABLE = machine.Pin(7, machine.Pin.OUT)


def load_limits(path="rotor_limits.json"):
    with open(path) as fh:
        return json.load(fh)


def lid_closed():
    return LID_PIN.value() == 0


def spin(rotor, target_rpm, seconds):
    limits = load_limits()
    ceiling = limits[rotor]
    if target_rpm > ceiling:
        raise ValueError("rotor {} limited to {} rpm".format(rotor, ceiling))
    if not lid_closed():
        raise RuntimeError("lid open")
    DRIVER_ENABLE.high()
    ramp.run(target_rpm, seconds)
    DRIVER_ENABLE.low()


if __name__ == "__main__":
    spin("micro", 8000, 30)
