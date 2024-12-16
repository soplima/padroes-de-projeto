from abc import ABC, abstractmethod

class Device(ABC):
    @abstractmethod
    def is_enabled(self) -> bool:
        pass

    @abstractmethod
    def enable(self) -> None:
        pass

    @abstractmethod
    def disable(self) -> None:
        pass

    @abstractmethod
    def get_volume(self) -> int:
        pass

    @abstractmethod
    def set_volume(self, volume: int) -> None:
        pass

class TV(Device):
    def __init__(self):
        self._enabled = False
        self._volume = 50

    def is_enabled(self) -> bool:
        return self._enabled

    def enable(self) -> None:
        print("TV: Ligando")
        self._enabled = True

    def disable(self) -> None:
        print("TV: Desligando")
        self._enabled = False

    def get_volume(self) -> int:
        return self._volume

    def set_volume(self, volume: int) -> None:
        print(f"TV: Ajustando volume para {volume}")
        self._volume = max(0, min(volume, 100))


class Radio(Device):
    def __init__(self):
        self._enabled = False
        self._volume = 30

    def is_enabled(self) -> bool:
        return self._enabled

    def enable(self) -> None:
        print("Rádio: Ligando")
        self._enabled = True

    def disable(self) -> None:
        print("Rádio: Desligando")
        self._enabled = False

    def get_volume(self) -> int:
        return self._volume

    def set_volume(self, volume: int) -> None:
        print(f"Rádio: Ajustando volume para {volume}")
        self._volume = max(0, min(volume, 100))

class RemoteControl:
    def __init__(self, device: Device):
        self._device = device

    def toggle_power(self):
        if self._device.is_enabled():
            self._device.disable()
        else:
            self._device.enable()

    def volume_up(self):
        volume = self._device.get_volume()
        self._device.set_volume(volume + 10)

    def volume_down(self):
        volume = self._device.get_volume()
        self._device.set_volume(volume - 10)

class AdvancedRemoteControl(RemoteControl):
    def mute(self):
        print("Mutando o dispositivo")
        self._device.set_volume(0)
