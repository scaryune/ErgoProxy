---
aliases: [radio, RF, radio-frequency]
---
# Radio Frequency:

## *Basic Premise:*
A transmitter, which has a power source, completes a circuit of electricity. When the circuit is closed/ completed, the circuit creates an electromagnetic force which can be picked up by the receiver.

Radios and other devices use #sine-wave s to transmit data. A receiver can distinguish different channels of information by frequency (number of cycles in the sine wave per second)

Every #radio has 2 parts:

- #Transmitter:
	- Takes a stream of data and encodes it into a sine wave.
	- Can then be amplified and sent out
- #Receiver:
	- receives the sine waves and decodes them back into readable data.
- *Both the transmitter and receiver use #antenna s*

## *Creating a #sine-wave*

### #capacitor 
A capacitor stores electrical energy in an electric field.
	- Does so by accumulating electrons on two surfaces ( #terminals)which are near each other but insulated from one another.
		- Similar to a battery
		- Each terminal holds an opposite charge, which creates an #electric-field
- A capacitor can be charged (ex: by a battery)
	- As electrons from the #battery flow through the capacitor:
		- As the negative terminal gains electrons, the positive terminal loses electrons == *equilibrium*
- When the capacitor is fully charged, it can be used to power something (ex: a motorized pulley)
	- Closing the circuit between the capacitor and the motor allows the electrons on the negative terminal to travel to the positive terminal (through the circuit)
	- This releases a lot of energy all at once (faster than attaching the motor to a battery)
	- #capacitance 

### Inductor
An inductor is another way to store energy (ex: electrons)
- Passing an electric current through a wire:
	- will create an #electromagnetic-field:
	- If a wire is coiled:
		- each coil creates its own EM-field when a current passes through it.
		- Due to proximity of the coils, their EM-fields will combine into a larger, more powerful field.
- Usually a curled coil in the circuit
	- In a circuit, inductors are high-resistance, meaning when a current is going through the circuit, the current will prefer other paths than through the inductor.
	- Despite being high resistance, some current will flow through the inductor
		- Over time, as more current goes through the coil, an electromagnetic field builds between the coils
			- inductors *store energy in the electromagnetic field they create*
				- the inductor is "charging up"
		- As the electromagnetic field gets stronger, the resistance of the inductor decreases
			- Eventually, the resistance is so low that a current can flow through it easily.
- When the EM-field in the coil is at its maximum and the OG power supply is shut off:
	- *the EM-field will collapse and release all of the energy it was storing into the circuit*
- **Inductors Don't Like Change**
	- When a circuit goes from off to on:
		- the current increases
		- the inductor **opposes this change** (resistance)
	- When the circuit turns off again, and the inductor is charged (has an EM-field)
		- It will release its energy in an opposing force called #back-EMF

>[!links]
>Capacitors:
> https://en.wikipedia.org/wiki/Capacitor
> 
> https://www.youtube.com/watch?v=5hFC9ugTGLs&ab_channel=NationalMagLab
> 
> Inductors:
> https://www.youtube.com/watch?v=NgwXkUt3XxQ&ab_channel=Afrotechmods
>  
> https://www.youtube.com/watch?v=KSylo01n5FY&ab_channel=TheEngineeringMindset
> 
> Flipper Zero:
> https://flipperzero.one/
> 
> https://docs.flipperzero.one/sub-ghz/read
> 
> Other:
> https://www.youtube.com/watch?v=lQUC6d6_r38&ab_channel=HamRadioCrashCourse
