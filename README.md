# 🐢 Turtlesim Catch Turtle Project

Bu proje, ROS 2 kullanarak Turtlesim üzerindeki kaplumbağaları otomatik olarak yakalayan bir sistem içerir. Birden fazla düğümü (node) tek bir merkezden yönetmek için bir **Bringup** paketi kullanılmıştır.

##  Klasör Yapısı ve Görevler

* **turtlesim_bringup/:** Projenin ana fırlatıcı (launch) paketidir.
    * **launch/:** Sistem başlangıç dosyalarını içerir.
        * `catch_turtle_app.launch.py`: Tüm sistemi başlatan ana dosya.
* **turtlesim_py_pkg/:** Kaplumbağa hareket mantığını içeren Python düğümleri.
* **turtlesim_interfaces/:** Özel mesaj ve servis tanımları.

## Çalıştırma Talimatları

Sistemi başlatmak için terminalinizde şu komutları sırasıyla çalıştırın:

```bash
cd ~/turtlesim_ws
colcon build --packages-select turtlesim_bringup
source install/setup.bash
ros2 launch turtlesim_bringup catch_turtle_app.launch.py



## Aşşağıdaki videoda launch dosyasının çalışmasının sonucu düğümlerin eş zamanlı çalışma şekli gösterilmektedir:
https://github.com/user-attachments/assets/a6a4bb74-40b3-47a6-ac5a-34f620962de7
