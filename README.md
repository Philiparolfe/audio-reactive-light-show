# Audio Light Show

This Python script utilizes the `gpiozero`, `pyaudio`, and `numpy` libraries to create an audio-controlled light show using a Raspberry Pi (or similar single-board computer) and a relay module. The code monitors audio input and controls relays based on specified frequency ranges and amplitude thresholds, synchronizing the lights with the audio.

## Requirements

Before running the code, make sure you have the following components and libraries installed:

- Raspberry Pi (or similar SBC)
- Relay module (I'm using the Keyestudio RPI 4channel-Relay 5V Shield)
- Appropriate GPIO pins configuration (adjust `RELAY_PINS` to match your setup)
- Python 3
- `gpiozero` library (`pip install gpiozero`)
- `pyaudio` library (`pip install pyaudio`)
- `numpy` library (`pip install numpy`)

## Installation

1. Ensure that the required libraries are installed as mentioned in the "Requirements" section.

2. Connect the relay module to your Raspberry Pi, ensuring the correct GPIO pin configuration as specified in the `RELAY_PINS` variable.

## Usage

1. Clone or download the repository containing this script.

2. Open a terminal and navigate to the directory where the script is located.

3. Run the script by executing the following command:

   ```bash
   python audio_light_show.py
