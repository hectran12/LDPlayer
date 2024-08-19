

import subprocess, os


class exec:
    def __init__(self) -> None:
        return
    """
        execute: execute command
        command: command
        timeout: timeout
        return: tuple (on stdout, on stderr)

    """
    @staticmethod
    def execute (command: str, timeout: int = 100) -> tuple:
        try:
            # exec
            result = subprocess.run(command, 
                                    capture_output=True,
                                    text=True,
                                    check=True,
                                    timeout=timeout,
                                    encoding='utf-8'
                                    )
            
            return result.stdout.strip(), result.stderr.strip()
        
        except subprocess.CalledProcessError as e:
            return None, e.stderr.strip()
    
    @staticmethod
    def execute_powershell (script: str, timeout:int=10) -> tuple:
        try:
            result = subprocess.run(["powershell", "-Command", script], capture_output=True, text=True)

            return result.stdout.strip(), result.stderr.strip()
        except subprocess.CalledProcessError as e:
            return None, e.stderr.strip()
        

class handleException (Exception):
    def __init__ (self, message) -> None:
        super().__init__(message)



class LDPlayer:
    """
        Include two cases:
        1. Set LDPlayer Path folder has file ldconsole.exe, dnconsole.exe 
        2. Set LDPlayer Path folder has file ldconsole.exe, dnconsole.exe to environment variable PATH

        @param ldPlayerPath: LDPlayer Path folder
        @return: None
    """
    def __init__ (self, ldPlayerPath: str = '') -> None:
        self.ldPlayerPath = ldPlayerPath
        if self.ldPlayerPath != '':
            self.ldconsolePath = self.ldPlayerPath + '\\' + 'ldconsole.exe'
            self.dnconsolePath = self.ldPlayerPath + '\\' + 'dnconsole.exe'
        else:
            self.ldconsolePath = 'ldconsole' # default path
            self.dnconsolePath = 'dnconsole' # default path

        if self.ldPlayerPath != '':
            if self.checkVaildPath() == False:
                raise handleException('Invalid path')
            

        self.objLDExec = exec()
        return
    
    """
        Check vaild path of LDPlayer
        @return: True if vaild path, else False
    """
    def checkVaildPath (self) -> bool:
        if os.path.exists(self.ldconsolePath) and os.path.exists(self.dnconsolePath):
            return True
        return False
    
    """
        Create new device
        @param deviceName: device name
        @return: True if success, else False
    """
    def createNewDevice (self, deviceName: str) -> bool:
        try:
            # command: ldconsole add --name deviceName
            stdout, stderr = self.objLDExec.execute([
                self.ldconsolePath,
                'add',
                '--name',
                deviceName
            ])
            
            if stderr != '':
                raise handleException(stderr)
            
            return True
        except Exception as e:
            raise handleException(str(e))

    """
        get all devices
        @return: list devices info
    
    """
    def getAllDevices (self) -> list:
        try:
            # command: ldconsole list2
            stdout, stderr = self.objLDExec.execute([
                self.ldconsolePath,
                "list2"
            ])
            if stderr != '':
                raise handleException(stderr)
            
            if stdout == '':
                return []
            

            listDevicesInfo = []
            for device in str(stdout).split("\n"):
                if device == '': continue
                info = device.split(',')
                index = info[0] 
                title = info[1] 
                top_window_handle = info[2] 
                bind_window_handle = info[3]
                android_started = info[4]
                pid = info[5]
                pid_of_vbox = info[6]

                listDevicesInfo.append({
                    "index": index,
                    "title": title,
                    "top_window_handle": top_window_handle,
                    "bind_window_handle": bind_window_handle,
                    "android_started": android_started, # status of device: 1: on, 0: off
                    "pid": pid,
                    "pid_of_vbox": pid_of_vbox
                })


            return listDevicesInfo

        except Exception as e:
            raise handleException(str(e))
    

    """
        Modify device
        @param deviceName: device name or @param deviceIndex: device index
        @param width: width of device
        @param height: height of device
        @param dpi: dpi of device
        @param cpu: cpu of device
        @param memory: memory of device

        @return: True if success, else error
    
    """
    def modifyDevice (self, deviceName: str = '', 
                      deviceIndex = None, width: int=720, 
                      height: int=1280, dpi: int = 160, 
                      cpu: int = 2, memory: int = 2048,
    ) -> bool:
        
        try:
            # ldconsole.exe modify --name LDPlayer --resolution 720,1280,160 --cpu 2 --memory 2048
            command = []
            command.append(self.ldconsolePath)
            command.append('modify')

            if deviceName != '':
                command.append('--name')
                command.append(deviceName)

            if deviceIndex != None:
                deviceIndex = str(deviceIndex)
                command.append('--index')
                command.append(deviceIndex)

            command.append('--resolution')
            command.append(f'{width},{height},{dpi}')
            command.append('--cpu')
            command.append(str(cpu))
            command.append('--memory')
            command.append(str(memory))

            stdout, stderr = self.objLDExec.execute(command)
            if stderr != '':
                raise handleException(stderr)
            


            return True
        
        except Exception as e:
            raise handleException(str(e))
    """
        Launch device
        @param deviceName: device name or @param deviceIndex: device index
        @return: True if success, else error
    """
    def launchDevice (self, deviceName: str = '', deviceIndex = None) -> bool:
        try:
            command = []
            command.append(self.ldconsolePath)
            command.append('launch')
            
            if deviceName != '':
                command.append('--name')
                command.append(deviceName)
            
            if deviceName != None:
                command.append('--index')
                command.append(str(deviceIndex))


            stdout, stderr = self.objLDExec.execute(command)
            if stderr != '':
                raise handleException(stderr)
            
            return True
        except Exception as e:
            raise handleException(str(e))
    
    """
        Quit all devices
        @return: True if success, else error
    """
    def quitAll (self) -> bool:
        try:
            stdout, stderr = self.objLDExec.execute([
                self.ldconsolePath,
                'quitall'
            ])

            if stderr != '':
                raise handleException(stderr)
            
            return True
        

        except Exception as e:
            raise handleException(str(e))

    """
        Quit device
        @param deviceName: device name or @param deviceIndex: device index
        @return: True if success, else error
    """
    def quit (self, deviceName: str = '', deviceIndex = None) -> bool:
        try:
            command = []
            command.append(self.ldconsolePath)
            command.append('quit')
            if deviceName != '':
                command.append('--name')
                command.append(deviceName)
            
            if deviceIndex != None:
                command.append('--index')
                command.append(str(deviceIndex))

            stdout, stderr = self.objLDExec.execute(command)
            if stderr != '':
                raise handleException(stderr)
            
            return True
        except Exception as e:
            raise handleException(str(e))
            



    


