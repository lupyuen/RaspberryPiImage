import time
import pigpio
import DHT22

pi = pigpio.pi()

# s = DHT22.sensor(pi, 4)
s = DHT22.sensor(pi, 22, LED=16, power=8)

s.trigger()

time.sleep(0.2)

print("temperature={} {} {:3.2f} {} {} {} {}".format(
  s.temperature(), s.humidity(), s.staleness(),
  s.bad_checksum(), s.short_message(), s.missing_message(),
  s.sensor_resets()))

s.cancel()

pi.stop()
