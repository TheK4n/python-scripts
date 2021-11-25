from abc import ABC


class Remote:
    def __init__(self, device: "Device"):
        self.device = device

    def toggle_power(self):
        if self.device.is_enabled():
            self.device.disable()
        else:
            self.device.enable()

    def volume_down(self):
        self.device.set_volume(self.device.get_volume() - 10)

    def volume_up(self):
        self.device.set_volume(self.device.get_volume() + 10)

    def channel_down(self):
        self.device.set_channel(self.device.get_channel() - 1)

    def channel_up(self):
        self.device.set_channel(self.device.get_channel() + 1)


class AdvancedRemote(Remote):
    def mute(self):
        self.device.set_volume(0)


class Device(ABC):

    def __init__(self):
        self.is_enable = False
        self.volume = 0
        self.channel = 0

    def is_enabled(self): return self.is_enable
    def enable(self): self.is_enable = True
    def disable(self): self.is_enable = False
    def get_volume(self): return self.volume
    def set_volume(self, percent): self.volume = percent
    def get_channel(self): return self.channel
    def set_channel(self, channel): self.channel = channel


class Tv(Device):
    pass


class Radio(Device):
    pass


if __name__ == '__main__':

    tv = Tv()
    remote = Remote(tv)
    remote.toggle_power()

    radio = Radio()
    remote = AdvancedRemote(radio)

    remote.volume_up()
    print(radio.volume)  # 10

    remote.mute()
    print(radio.volume)  # 0
