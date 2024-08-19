# ldPlayer
Một số hàm thực hiện lệnh để thao tác với ldplayer
Thêm file ldplayer.py vào dự án của bạn và sử dụng như bên dưới :D

```python
import ldplayer
obj = ldplayer.LDPlayer() # tìm tới folder có đường dẫn giống như này F:\LDPlayer\LDPlayer9 và set vào envrionment variable hoặc truyền vào hàm __init__

obj.createNewDevice('line') # tạo device có tên là line 
obj.modifyDevice(deviceName="line", width=720, height=1280, dpi=320, cpu=2, memory=2048) # sửa device có tên là line
obj.launchDevice(deviceName="line") # mở device có tên là line
obj.quit(deviceName="line") # tắt device có tên là line
obj.quitAll() # tắt tất cả các device
```
