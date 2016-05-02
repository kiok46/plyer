class Sysinfo(object):
    ''' Sysinfo facade.
    '''

    def system_info(self):
        # returns the name of system.
        return self._system_info()

    def platform_info(self):
        # returns platform name including version.
        return self._platform_info()

    def processor_info(self):
        # returns the processor details
        return self._processor_info()

    def version_info(self):
        # returns release, version and ptype.
        return self._version_info()

    def architecture_info(self):
        # returns architecture of device.
        return self.architecture_info()

    def device_name(self):
        # returns name of the device.
        return self._device_name()

    def manufacturer_name(self):
        # returns the manufacturer's name
        return self._manufacturer_name()

    # private

    def _system_info(self):
        raise NotImplementedError()

    def _platform_info(self):
        raise NotImplementedError()

    def _processor_info(self):
        raise NotImplementedError()

    def _version_info(self):
        raise NotImplementedError()

    def _architecture_info(self):
        raise NotImplementedError()

    def _device_name(self):
        raise NotImplementedError()

    def _manufacturer_name(self):
        raise NotImplementedError()
