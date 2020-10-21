# MI-WAVE-511-series
Code to control a MI-WAVE 511 RF attenuators

Basic usage:
```
import PrologixGPIBEthernetCustom

controller = PrologixGPIBEthernetCustom.PrologixGPIBEthernetCustom(172.128.1.1)
controller.connect()

controller.set_attenuation(10, 4)
controller.set_attenuation(20, 2)

controller.close()
