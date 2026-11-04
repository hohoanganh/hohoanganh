<div align="center">
  <img src="assets/banner.png" alt="Hồ Hoàng Anh (Anh MakerX) — Hardware Engineer: thiết kế mạch, firmware nhúng, công cụ kiểm thử cho sản xuất" width="100%">
</div>

<p align="center">
  <a href="https://hohoanganh.github.io/ak-mcu-base/play/"><b>Chạy thử firmware trên trình duyệt</b></a> ·
  <a href="https://github.com/hohoanganh/ak-mcu-base">ak-mcu-base</a> ·
  <a href="https://www.tiktok.com/@hohoanganh1">TikTok</a>
</p>

<p align="center">
  <a href="https://github.com/hohoanganh/hohoanganh/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-0366d6" alt="license MIT"></a>
  <a href="https://github.com/hohoanganh?tab=followers"><img src="https://img.shields.io/github/followers/hohoanganh?logo=github&amp;label=theo%20d%C3%B5i" alt="người theo dõi"></a>
  <a href="https://github.com/hohoanganh/ak-mcu-base/stargazers"><img src="https://img.shields.io/github/stars/hohoanganh/ak-mcu-base?logo=github&amp;label=ak-mcu-base" alt="sao ak-mcu-base"></a>
  <a href="https://www.tiktok.com/@hohoanganh1"><img src="https://img.shields.io/badge/TikTok-%40hohoanganh1-000000?logo=tiktok" alt="TikTok"></a>
  <br>
  <img src="https://img.shields.io/badge/C-firmware-555555?logo=c" alt="C">
  <img src="https://img.shields.io/badge/Rust-nh%C3%BAng-000000?logo=rust" alt="Rust">
  <img src="https://img.shields.io/badge/STM32-L1%20%C2%B7%20G0-03234B?logo=stmicroelectronics" alt="STM32">
  <img src="https://img.shields.io/badge/ESP32-Espressif-E7352C?logo=espressif&amp;logoColor=white" alt="ESP32">
  <img src="https://img.shields.io/badge/nRF52-Nordic-00A9CE?logo=nordicsemiconductor&amp;logoColor=white" alt="nRF52">
  <img src="https://img.shields.io/badge/Modbus-RTU%20%C2%B7%20TCP-0366d6" alt="Modbus RTU / TCP">
  <a href="https://claude.com/claude-code"><img src="https://img.shields.io/badge/built%20with-Claude%20Code-d97757?logo=claude&amp;logoColor=white" alt="built with Claude Code"></a>
</p>

## Giới thiệu

Tôi là **Hồ Hoàng Anh**, kỹ sư phần cứng. Tôi thiết kế mạch điện tử, viết firmware cho vi điều khiển và làm công cụ
kiểm thử cho sản xuất. Trang này là những thứ tôi làm ngoài giờ, chủ yếu quanh firmware nhúng.

| Mảng | Công việc |
|---|---|
| **Phần cứng** | Schematic, PCB, 3D, Render design đưa sản phẩm từ ý tưởng tới sản xuất |
| **Firmware** | STM32, ESP32, nRF52; Modbus RTU, bootloader, OTA |
| **Công cụ** | Tool test cho phát triển sản phẩm, và dây chuyển sản xuất |

## Dự án nổi bật

### [ak-mcu-base](https://github.com/hohoanganh/ak-mcu-base): nền firmware cho STM32L151

<a href="https://hohoanganh.github.io/ak-mcu-base/play/">
  <img src="https://raw.githubusercontent.com/hohoanganh/ak-mcu-base/main/docs/demo-tour.gif" alt="Bộ demo trên AK Base Kit: đồng hồ, game, 3D, video, máy hiện sóng" width="404" align="right">
</a>

Nền firmware bare-metal dựng lại từ [AK Base Kit](https://github.com/the-ak-foundation/ak-base-kit-stm32l151) của
AK Foundation: kernel hướng sự kiện không cần RTOS, bootloader có quay lui, cập nhật firmware qua UART và RS485.

- **Chạy thử:** [17 màn hình của kit](https://hohoanganh.github.io/ak-mcu-base/play/) trong trình duyệt, không cần kit
- **Xem bên trong:** [dừng firmware, chạy từng message](https://hohoanganh.github.io/ak-mcu-base/play/inside.html)
- **Lập trình kéo thả:** [nối khối, bấm Chạy](https://hohoanganh.github.io/ak-mcu-base/play/blocks.html)
- **Demo có gì:** [từng màn hình, kèm ảnh động](https://github.com/hohoanganh/ak-mcu-base/blob/main/docs/demo-kit.md)
- **Tải firmware:** [Releases](https://github.com/hohoanganh/ak-mcu-base/releases)

<br clear="right">

Vài điểm đáng xem:

- **Một mã nguồn, ba nơi chạy.** Cùng mã C chạy trên chip, trong unit test trên máy tính và trong trình duyệt
  (WebAssembly), vì ranh giới với bo mạch được giữ thật mỏng.
- **Firmware tự kể lại sự cố.** HardFault, FATAL, watchdog và task treo được ghi vào EEPROM, báo lại ở lần khởi động sau.
- **Bootloader chịu được mất điện.** Unit test giả lập cắt điện ở 1366 điểm trong lúc cài; lần nào cũng khôi phục được.
- **Ảnh trong tài liệu không phải ảnh chụp.** Chúng được dựng từ chính mã vẽ của firmware, nên không lệch với thực tế.

## Cộng đồng

Các dự án ở đây đứng trên nền của [AK Foundation](https://github.com/the-ak-foundation), nhóm làm phần mềm nhúng tại
Việt Nam. Nếu bạn mới học lập trình hướng sự kiện cho vi điều khiển, hãy bắt đầu từ
[chương trình đào tạo](https://github.com/the-ak-foundation/embedded-training-program) của họ.

## Liên hệ

- Góp ý hoặc báo lỗi: mở issue ở dự án tương ứng, ví dụ [ak-mcu-base](https://github.com/hohoanganh/ak-mcu-base/issues).
- TikTok: [@hohoanganh1](https://www.tiktok.com/@hohoanganh1)

<p align="center">
  <img src="https://hits.sh/github.com/hohoanganh.svg?style=flat-square&label=profile%20views&color=007ec6" alt="Lượt xem trang">
</p>
