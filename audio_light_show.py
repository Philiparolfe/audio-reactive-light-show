from gpiozero import OutputDevice
import pyaudio
import numpy as np
import asyncio


RELAY_PINS = [4, 22, 6, 26]  

class AudioLightShow:
    def __init__(self):
        self.audio = pyaudio.PyAudio()
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 2
        self.RATE = 44100
        self.CHUNK = 1024
        self.relay_devices = [OutputDevice(pin) for pin in RELAY_PINS]

    async def trigger_relay_in_frequency_range(self, frequency_range, amplitude_threshold, relay_index):
        while True:
            try:
                
                stream = self.audio.open(format=self.FORMAT, channels=self.CHANNELS, rate=self.RATE, input=True, input_device_index=1, frames_per_buffer=self.CHUNK)
                data = stream.read(self.CHUNK)
                audio_data = np.frombuffer(data, dtype=np.int16)

                # Calculate the frequency content of the audio data
                fft_result = np.fft.fft(audio_data)
                psd = np.abs(fft_result) ** 2
                freq_axis = np.fft.fftfreq(len(audio_data), 1.0 / self.RATE)

                # Find the indices corresponding to the specified frequency range
                lower_freq, upper_freq = frequency_range
                lower_index = np.argmin(np.abs(freq_axis - lower_freq))
                upper_index = np.argmin(np.abs(freq_axis - upper_freq))

                # Calculate the amplitude within the frequency range
                amplitude_in_range = np.sum(psd[lower_index:upper_index + 1])

                # Check if the amplitude within the range crosses the threshold
                if amplitude_in_range > amplitude_threshold:
                    self.relay_devices[relay_index].on()
                else:
                    self.relay_devices[relay_index].off()

                # Clean up audio stream and terminate audio resources
                stream.stop_stream()
                stream.close()

            except KeyboardInterrupt:
                break
            except Exception as e:
                print(e)
                break

            # Wait for a short duration before checking again
            await asyncio.sleep(0.0001)

    async def run(self):
        await asyncio.gather(
            self.trigger_relay_in_frequency_range((40, 70), 10000000000000, 0),
            self.trigger_relay_in_frequency_range((390, 410), 100000000000, 2),
            self.trigger_relay_in_frequency_range((5900, 6100), 1000000000, 3)
        )

if __name__ == "__main__":
    audio_light_show = AudioLightShow()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(audio_light_show.run())
