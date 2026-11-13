# Bramblewick Whirl

Open-source design package for the Whirl microcentrifuge.

## Implementation

Whirl is a direct-drive microcentrifuge. A 2208-class BLDC motor drives a
single-piece aluminium rotor, and the lid interlock is a magnetic reed switch
read by the RP2040 controller.

- `hardware/` - KiCad driver schematic and board layout.
- `firmware/` - soft-start ramp, rotor limits and lid interlock handling.
- `enclosure/` - rotor chamber and lid models.
- `docs/` - service notes.

## Build

Flash `firmware/rotor.py` and `firmware/ramp.py`. Rotor limits are compiled
into the firmware from `rotor_limits.json`; the bench planner reads the same
values from the component entry.

The rotor chamber is printed in ASA; the lid uses a polycarbonate window.
