# 🐢 Turtlesim Catch Turtle Project

Bu proje, ROS 2 kullanarak Turtlesim üzerindeki kaplumbağaları otomatik olarak yakalayan bir sistem içerir. Birden fazla düğümü (node) tek bir merkezden yönetmek için bir **Bringup** paketi kullanılmıştır.

## 📁 Klasör Yapısı ve Görevler

* **turtlesim_bringup/:** Projenin ana fırlatıcı (launch) paketidir.
    * **launch/:** Sistem başlangıç dosyalarını içerir.
        * `catch_turtle_app.launch.py`: Tüm sistemi başlatan ana dosya.
* **turtlesim_py_pkg/:** Kaplumbağa hareket mantığını içeren Python düğümleri.
* **turtlesim_interfaces/:** Özel mesaj ve servis tanımları.

## 🚀 Çalıştırma Talimatları

Sistemi başlatmak için terminalinizde şu komutları sırasıyla çalıştırın:

```bash
cd ~/turtlesim_ws
colcon build --packages-select turtlesim_bringup
source install/setup.bash
ros2 launch turtlesim_bringup catch_turtle_app.launch.py




Aşağıdaki videoda sistemin çalışma şekli gösterilmektedir:

Screencast from 23-12-2025 23:52:39.webm
