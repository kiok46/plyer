from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from plyer import sysinfo
from kivy.properties import StringProperty


Builder.load_string('''
<SysinfoInterface>:
    GridLayout:
        cols: 2
        Label:
            text: "Platform"
        Label:
            text: root.platform_
        Label:
            text: "System"
        Label:
            text: root.system_
        Label:
            text: "Processor"
        Label:
            text: root.processor_
        Label:
            text: "Version"
        Label:
            text: root.version_
        Label:
            text: "Architecture"
        Label:
            text: root.architecture_
        Label:
            text: "Device"
        Label:
            text: root.device_
        Label:
            text: "Manufacturer"
        Label:
            text: root.manufacturer_

''')


class SysinfoInterface(BoxLayout):

    platform_ = StringProperty()
    system_ = StringProperty()
    processor_ = StringProperty()
    version_ = StringProperty()
    architecture_ = StringProperty()
    device_ = StringProperty()
    manufacturer_ = StringProperty()

    def __init__(self, **kwargs):
        super(SysinfoInterface, self).__init__(**kwargs)
        self.update()

    def update(self):
        self.get_platform()
        self.get_system()
        self.get_processor()
        self.get_version()
        self.get_architecture()
        self.get_device_name()
        self.get_manufacturer()

    def get_platform(self):
        self.platform_ = sysinfo.platform_info()

    def get_system(self):
        self.system_ = sysinfo.system_info()

    def get_processor(self):
        self.processor_ = sysinfo.processor_info()

    def get_version(self):
        temp = sysinfo.version_info()
        self.version_ = "{} {} {}".format(temp[0], temp[1], temp[2])

    def get_architecture(self):
        self.architecture_ = sysinfo.architecture_info()

    def get_device_name(self):
        self.device_ = sysinfo.device_info()

    def get_manufacturer(self):
        self.manufacturer_ = sysinfo.manufacturer_name()


class SysinfoApp(App):

    def build(self):
        return SysinfoInterface()

if __name__ == "__main__":
    app = SysinfoApp()
    app.run()

