"""Soft-start ramp for the Whirl centrifuge."""

import time

from machine import PWM

PWM_PIN = PWM(8)


def run(target_rpm, seconds, points=((0, 300), (10, 6000))):
    start = time.ticks_ms()
    elapsed = 0
    while elapsed < seconds * 1000:
        elapsed = time.ticks_ms() - start
        duty = interpolate(points, elapsed / 1000.0)
        PWM_PIN.duty_u16(int(duty * 65535))
        time.sleep_ms(20)
    PWM_PIN.duty_u16(0)


def interpolate(points, t):
    if t <= points[0][0]:
        return points[0][1] / 10000.0
    for left, right in zip(points, points[1:]):
        if left[0] <= t <= right[0]:
            span = right[0] - left[0]
            if span == 0:
                return right[1] / 10000.0
            fraction = (t - left[0]) / span
            return (left[1] + fraction * (right[1] - left[1])) / 10000.0
    return points[-1][1] / 10000.0
