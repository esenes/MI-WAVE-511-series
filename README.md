# MI-WAVE-511-series
Code to control a MI-WAVE 511 RF attenuators

Basic usage with two attenuators:
```
import PrologixGPIBEthernetCustom
import Attenuator_511A

controller = PrologixGPIBEthernetCustom.PrologixGPIBEthernetCustom('1.1.1.1')
controller.connect()

atten1 = Attenuator_511A.Attenuator_511A(4, controller)
atten2 = Attenuator_511A.Attenuator_511A(2, controller)

# and that's it !
att1.set_attenuation(10) #dB
att2.set_attenuation(30) #dB

controller.close()
```
This can be scaled to all the possible GPIB addresses available. 
