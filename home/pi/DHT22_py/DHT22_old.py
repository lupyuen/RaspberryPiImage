#!/usr/bin/env python

import time

import pigpio

class DHT22_sensor:
   """
   A class to read relative humidity and temperature from the
   DHT22 sensor.  The sensor is also known as the AM2302.

   The sensor can be powered from the Pi 3V3 or the Pi 5V rail.

   Powering from the 3V3 rail is simpler and safer.  You may need
   to power from 5V if the sensor is connected via a long cable.

   For 3V3 operation connect pin 1 to 3V3 and pin 4 to ground.

   Connect pin 2 to a gpio.

   For 5V operation connect pin 1 to 5V and pin 4 to ground.

   The following pin 2 connection works for me.  Use at YOUR OWN RISK.

   5V--5K_resistor--+--10K_resistor--Ground
                    |
   DHT22 pin 2 -----+
                    |
   gpio ------------+
   """

   def __init__(self, gpio):
      """
      Instantiate with the gpio to which the DHT22 output pin is connected.
      """

      self.gpio = gpio

      self.bad_CS = 0 # checksum
      self.bad_TO = 0 # time-out

      self.accumulating = False

      self.rhum = -999
      self.temp = -999

      self.tov = None

      self.tick = 0

      pigpio.set_mode(gpio, pigpio.INPUT)

      pigpio.set_pull_up_down(gpio, pigpio.PUD_OFF)

      self.cb = pigpio.callback(gpio, pigpio.EITHER_EDGE, self._cb)

   def _cb(self, gpio, level, tick):
      """
      Accumulate the 40 data bits.  Format into 5 bytes, humidity high,
      humidity low, temperature high, temperature low, checksum.
      """
      if self.accumulating:

         if level == 0:

            diff = pigpio.tickDiff(self.tick, tick)

            # edge length determines if bit is 1 or 0

            if diff >= 50:
               val = 1
            else:
               val = 0

            if self.bit >= 32: # in checksum byte
               self.CS  = (self.CS<<1)  + val

               if self.bit >= 39:

                  # 40 bits received

                  self.accumulating = False

                  pigpio.set_watchdog(self.gpio, 0)

                  total = self.hH + self.hL + self.tH + self.tL

                  if (total & 255) == self.CS: # is checksum ok

                     self.rhum = ((self.hH<<8) + self.hL) * 0.1

                     if self.tH & 128: # negative temperature
                        mult = -0.1
                        self.tH = self.tH & 127
                     else:
                        mult = 0.1

                     self.temp = ((self.tH<<8) + self.tL) * mult

                     self.tov = time.time()

                  else:

                     self.bad_CS += 1

            elif self.bit >=24: # in temp low byte
               self.tL = (self.tL<<1) + val

            elif self.bit >=16: # in temp high byte
               self.tH = (self.tH<<1) + val

            elif self.bit >= 8: # in humidity low byte
               self.hL = (self.hL<<1) + val

            elif self.bit >= 0: # in humidity high byte
               self.hH = (self.hH<<1) + val

            else:               # header bits
               pass

            self.bit += 1

         elif level == 1:
            self.tick = tick
            if self.bit == -3: # correct for first reading
               self.bit = -2

         else: # level == pigpio.TIMEOUT:
            # time out if less than 40 bits received
            self.accumulating = False
            pigpio.set_watchdog(self.gpio, 0)
            self.bad_TO += 1

      else: # perhaps a repeated watchdog
         if level == pigpio.TIMEOUT:
            pigpio.set_watchdog(self.gpio, 0)

   def temperature(self):
      """Return current temperature."""
      return self.temp

   def humidity(self):
      """Return current relative humidity."""
      return self.rhum

   def staleness(self):
      """Return time since measurement made."""
      if self.tov is not None:
         return time.time() - self.tov
      else:
         return -999

   def bad_checksum(self):
      """Return count of messages received with bad checksums."""
      return self.bad_CS

   def timed_out(self):
      """Return count of messages which have timed out."""
      return self.bad_TO

   def trigger(self):
      """Trigger a new relative humidity and temperature reading."""
      self.bit = -3 # header bits
      self.hH = 0
      self.hL = 0
      self.tH = 0
      self.tL = 0
      self.CS = 0
      self.accumulating = True
      pigpio.write(self.gpio, 0)
      time.sleep(0.0001)
      pigpio.set_mode(self.gpio, pigpio.INPUT)
      pigpio.set_watchdog(self.gpio, 50)

   def cancel(self):
      """Cancel the DHT22 sensor."""
      self.cb.cancel()

if __name__ == "__main__":

   import time

   import pigpio

   import DHT22

   pigpio.start()

   s = DHT22.DHT22_sensor(7)

   r = 0

   while True:

      r += 1

      s.trigger()

      time.sleep(0.2)

      print("{} {} {} {:3.2f} {} {}"
         .format(r, s.humidity(), s.temperature(), s.staleness(),
         s.bad_checksum(), s.timed_out()))

      time.sleep(1.75)

   s.cancel()

   pigpio.stop()

