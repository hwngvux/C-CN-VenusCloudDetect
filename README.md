# CDCN-VenusCloudDetect
## 1.Giới thiệu 
Code bài tập lớn môn Chuyên Đề Công nghệ. 

Tách mây ti từ ảnh vệ tinh Venus. 

Sử dụng ngôn ngữ Python.

## 2.Cài đặt
Cài đặt python3. Dùng IDLE hoặc notebook jupyter của Anaconda để chạy code.

## 3.Hướng dẫn 
Sau khi có được ảnh mây level 1 từ band 15.

Ta dùng lệnh trên console để resize ảnh level 1 vừa có và so sánh với ảnh level 2
```bash
gdalwarp -of GTiff -s_srs epsg:4326 -t_srs epsg:4326 -ts 4786 6348 input.tif output.tif
```
