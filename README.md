# ldPlayer
Một số hàm thực hiện lệnh để thao tác với ldplayer
Thêm file ldplayer.py vào dự án của bạn và sử dụng như bên dưới :D

```python
import ldplayer
obj = ldplayer.LDPlayer() # tìm tới folder có đường dẫn giống như này F:\LDPlayer\LDPlayer9 và set vào envrionment variable hoặc truyền vào hàm __init__


obj.createNewDevice('fb_device') # tạo device có tên là fb_device 
obj.modifyDevice(deviceName="fb_device", width=720, height=1280, dpi=320, cpu=2, memory=2048) # sửa device có tên là fb_device
obj.launchDevice(deviceName="fb_device") # mở device có tên là fb_device
obj.quit(deviceName="fb_device") # tắt device có tên là fb_device
obj.quitAll() # tắt tất cả các device
obj.copy("new_device", fromDeviceName="LDPlayer") # copy device từ LDPlayer sang new_device
obj.remove(deviceName="new_device") # xóa device new_device

print(obj.getDeviceIndexByName(deviceName="hex_GUL2")) # lấy index của device hex_GUL2
print(obj.getDeviceNameByIndex(deviceIndex=1)) # lấy tên của device có index 0
if obj.waitForDeviceRunning(deviceName="hex_GUL2", timeout_wait=120): # chờ máy khởi động vào giao diện android
    print('Device is running')
else:
    print('Device is not running')


obj.getSerialNo(deviceName="hex_GUL2") # lấy serial number của device hex_GUL2 để kết nối với adb
# output example: emulator-5556 (dùng trong case cần exec chỉ định như adb -s emulator-5556 shell input keyevent 3)
```
