import krpc
import time

conn = krpc.connect(name='Sub-orbital flight')
vessel = conn.space_center.active_vessel

vessel.auto_pilot.target_pitch_and_heading(90,90)
vessel.auto_pilot.engage()
vessel.control.throttle = 1
time.sleep(1)

input("Press Any Key to Launch...")
print('Launch!')
vessel.control.activate_next_stage()