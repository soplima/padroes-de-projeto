from abc import ABC, abstractmethod

# Classe abstrata que define a interface para dispositivos (TV, Rádio, etc.)
class Device(ABC):
    # Métodos abstratos que precisam ser implementados pelas classes filhas
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

# Implementação da classe TV, que herda de Device
class TV(Device):
    def __init__(self):
        self._enabled = False  # TV começa desligada
        self._volume = 50  # Volume inicial da TV

    def is_enabled(self) -> bool:
        return self._enabled  # Retorna o estado de ligamento da TV

    def enable(self) -> None:
        print("TV: Ligando")  # Exibe mensagem quando a TV é ligada
        self._enabled = True  # Marca a TV como ligada

    def disable(self) -> None:
        print("TV: Desligando")  # Exibe mensagem quando a TV é desligada
        self._enabled = False  # Marca a TV como desligada

    def get_volume(self) -> int:
        return self._volume  # Retorna o volume atual da TV

    def set_volume(self, volume: int) -> None:
        # Ajusta o volume da TV, garantindo que ele esteja entre 0 e 100
        print(f"TV: Ajustando volume para {volume}")
        self._volume = max(0, min(volume, 100))

# Implementação da classe Radio, que também herda de Device
class Radio(Device):
    def __init__(self):
        self._enabled = False  # Rádio começa desligado
        self._volume = 30  # Volume inicial do rádio

    def is_enabled(self) -> bool:
        return self._enabled  # Retorna o estado de ligamento do rádio

    def enable(self) -> None:
        print("Rádio: Ligando")  # Exibe mensagem quando o rádio é ligado
        self._enabled = True  # Marca o rádio como ligado

    def disable(self) -> None:
        print("Rádio: Desligando")  # Exibe mensagem quando o rádio é desligado
        self._enabled = False  # Marca o rádio como desligado

    def get_volume(self) -> int:
        return self._volume  # Retorna o volume atual do rádio

    def set_volume(self, volume: int) -> None:
        # Ajusta o volume do rádio, garantindo que ele esteja entre 0 e 100
        print(f"Rádio: Ajustando volume para {volume}")
        self._volume = max(0, min(volume, 100))

# Classe RemoteControl que gerencia a interação com qualquer dispositivo do tipo Device
class RemoteControl:
    def __init__(self, device: Device):
        self._device = device  # O controle remoto recebe um dispositivo para controlar

    def toggle_power(self):
        # Alterna o estado de ligado/desligado do dispositivo
        if self._device.is_enabled():
            self._device.disable()  # Se o dispositivo estiver ligado, desliga
        else:
            self._device.enable()  # Se o dispositivo estiver desligado, liga

    def volume_up(self):
        volume = self._device.get_volume()  # Obtém o volume atual
        self._device.set_volume(volume + 10)  # Aumenta o volume em 10

    def volume_down(self):
        volume = self._device.get_volume()  # Obtém o volume atual
        self._device.set_volume(volume - 10)  # Diminui o volume em 10

# Classe AdvancedRemoteControl que herda de RemoteControl e adiciona mais funcionalidades
class AdvancedRemoteControl(RemoteControl):
    def mute(self):
        # Muta o dispositivo, ou seja, define o volume para 0
        print("Mutando o dispositivo")
        self._device.set_volume(0)  # Ajusta o volume para 0
