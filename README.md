# AlienWorlds Auto Claim TLM - Community version

The premium version is developing. Its functionality will be announced soon. It's safer, more stable, more accurate,
faster, lighter for multiple accounts. The auto script will be located **in this [private repository](https://github.com/autoalmosteverything/AlienWorldsPremium) only available to those
who have received my invitation (from now, I will call "Right of Access", RoA).** In particular, when buying RoA, you
can download it anytime, use it for any account on any computer, without limitation (except sharing). I will support the
first-time setup and always update and fix bugs in the future.

**For those of you who have donated money, WAXP, BTC** when I develop the community version, **I will give free RoA**.
This is a recognition of your support. Thank you!

**For those who want to use the premium version**, I will announce the price for each milestone of development. Expected
from **$ 20 for the early versions, later the price will increase**. Please note that **you purchased RoA, not a
license**.

### [English - Tiếng Việt bên dưới]

TLM is listed on Binance. read more on [CoinMarketCap](https://coinmarketcap.com/vi/currencies/alien-worlds/).

###### Functions:

1. Claim TLM.
2. Captcha warning by notification and sound.
3. Automatically solve captcha by using:

   3.1. 2Captcha, [Register here](https://2captcha.com?from=11528745).

   3.2. CapMonster, [Register here](https://capmonster.cloud/).

   3.3. Anti-captcha will be added in the next update.

4. Handle the expired captcha to try again, max 2 times.
5. Get username, resource information (from Wax wallet), and .<img src="https://www.svgrepo.com/show/196054/premium.svg" width="20" height="20" title="In premium version"> **delay time (based current land and tools)**.
6. Handle `out of CPU, NET and RAM` error:
   - Always check resource before mine.
   - Wait until the used resource amount returns under 100%.
7. Handle `fail to fetch` error: try to login again.
8. .<img src="https://www.svgrepo.com/show/196054/premium.svg" width="20" height="20" title="In premium version"> **Prevent falling into an endless loop when mining.**
9. Handle `transaction is expired` error: try to claim again.
10. Smoothly run by auto ignoring other errors.
11. Support proxy.
12. Logging.
13. .<img src="https://www.svgrepo.com/show/196054/premium.svg" width="20" height="20" title="In premium version"> **Auto get/refresh cookies for multi-account.**
14. .<img src="https://www.svgrepo.com/show/196054/premium.svg" width="20" height="20" title="In premium version"> **Multi-account with real browser profiles.**
15. .<img src="https://www.svgrepo.com/show/196054/premium.svg" width="20" height="20" title="In premium version"> **Support first setup (free), edit code (1$ / 10 lines).**

###### Tutorial:

v1.0 [View on Youtube](https://www.youtube.com/watch?v=NWUMdimjPPE)

- Claim TLM.

v1.1 [View on Youtube](https://www.youtube.com/watch?v=qvD0Kp5Sp30)

- Update new wait & click mechanism to reduce wait time and increase click position and timing accuracy.
- Automatically solve captcha by using 2Captcha.
- Handle the expired captcha to try again, max 2 times.
- Smoothly run by auto ignoring other errors.

v1.2 [View on Youtube](https://youtu.be/6XfwxT-w4_I)

- Get username, resource information (from Wax wallet).
- Handle `out of CPU, NET and RAM` error:
   - Always check resource before mine.
   - Wait until the used resource amount returns under 100%.

v1.3 [View on Youtube](https://www.youtube.com/watch?v=kiVkAjCedSU)

- Handle `transaction is expired` error: try to claim again.

v1.4 [View on Youtube]()

- Switch to one time login instead of the loop of turn off/turn on browser.
- Handle `fail to fetch` error: try to login again.
- .<img src="https://www.svgrepo.com/show/196054/premium.svg" width="20" height="20" title="In premium version"> **Get delay time (based current land and tools).**
- .<img src="https://www.svgrepo.com/show/196054/premium.svg" width="20" height="20" title="In premium version"> **Prevent falling into an endless loop when mining.**
- Add CapMonster as 2nd anti-captcha service.
- Support proxy.
- Add logging function.

v1.5 Release soon

- .<img src="https://www.svgrepo.com/show/196054/premium.svg" width="20" height="20" title="In premium version"> **Auto get/refresh cookies for multi-account.**
- .<img src="https://www.svgrepo.com/show/196054/premium.svg" width="20" height="20" title="In premium version"> **Multi-account with real browser profiles.**

###### Please do step by step to use:

1. Install language **Python 3.9.x** https://www.python.org/downloads/.

[![SC2 Video](http://i3.ytimg.com/vi/_CoijjMXvYY/hqdefault.jpg)](https://www.youtube.com/watch?v=_CoijjMXvYY)

2. Install modules  **requests**, **selenium**, **win10toast** `python -m pip install requests selenium win10toast`.

[![SC2 Video](http://i3.ytimg.com/vi/SQQRYAMl8Jk/hqdefault.jpg)](https://www.youtube.com/watch?v=SQQRYAMl8Jk)

3. (_Optional_) Install IDE **PyCharm** https://www.jetbrains.com/pycharm/.

[![SC2 Video](http://i3.ytimg.com/vi/FqEXepao0go/hqdefault.jpg)](https://www.youtube.com/watch?v=FqEXepao0go)

4. (_Optional_) Download **Chrome WebDriver** https://chromedriver.chromium.org/.
5. Run script.
6. (_Optional_) Edit script for your personal use. Contact me for more functions.

###### Note:

1. **Do not resize** the browser's window.

### [Tiếng Việt - English above]

TLM đã lên sàn Binance. Xem thêm trên [CoinMarketCap](https://coinmarketcap.com/vi/currencies/alien-worlds/).

###### Tính năng:

1. Nhận TLM.
2. Cảnh báo captcha bằng thông báo và âm thanh.
3. Tự động giải captcha bằng:

   3.1. 2Captcha, [Đăng ký tại đây](https://2captcha.com?from=11528745).

   3.2. CapMonster, [Đăng ký tại đây](https://capmonster.cloud/).

   3.3. Anti-captcha sẽ được thêm vào trong bản cập nhật tới.

4. Xử lý captcha quá hạn để thử lại, tối đa 2 lần.
5. Lấy thông tin người chơi, tài nguyên (từ ví Wax), và .<img src="https://www.svgrepo.com/show/196054/premium.svg" width="20" height="20" title="In premium version"> **thời gian đợi (dựa trên đất hiện tại cũng như công cụ đang sử
   dụng)**.
6. Xử lý lỗi `out of CPU, NET, and RAM`: đợi đến khi lượng tài nguyên đã sử dụng trở về dưới 100%.
7. Xử lỹ lỗi `fail to fetch`: cố gắng đăng nhập lại.
8. .<img src="https://www.svgrepo.com/show/196054/premium.svg" width="20" height="20" title="In premium version"> **Chống treo khi khai thác.**
9. Xử lý lỗi `transaction is expired`: cố gắng nhận lại.
10. Chạy mượt bằng cách tự bỏ qua các lỗi khác.
11. Hỗ trợ proxy.
12. Ghi log.
13. .<img src="https://www.svgrepo.com/show/196054/premium.svg" width="20" height="20" title="In premium version"> **Tự động lấy/làm mới cookies cho nhiều tài khoản.**
14. .<img src="https://www.svgrepo.com/show/196054/premium.svg" width="20" height="20" title="In premium version"> **Chạy nhiều tài khoản với hồ sơ người dùng trình duyệt thật.**
15. .<img src="https://www.svgrepo.com/show/196054/premium.svg" width="20" height="20" title="In premium version"> **Hỗ trợ cài đặt lần đầu (miễn phí), sửa code (1$ / 10 dòng).**

###### Hướng dẫn:

v1.0 [Xem trên Youtube](https://www.youtube.com/watch?v=NWUMdimjPPE)

- Nhận TLM.

v1.1 [Xem trên Youtube](https://www.youtube.com/watch?v=qvD0Kp5Sp30)

- Cập nhật cơ chế đợi và click nhằm giảm thời gian đợi, tăng độ chính xác của vị trí và thời điểm click.
- Tự động giải captcha bằng 2Captcha.
- Xử lý captcha quá hạn để thử lại, tối đa 2 lần.
- Chạy mượt bằng cách tự bỏ qua các lỗi khác.

v1.2 [Xem trên Youtube](https://youtu.be/6XfwxT-w4_I)

- Lấy thông tin người chơi, tài nguyên (từ ví Wax).
- Xử lý lỗi `out of CPU, NET, and RAM`: 
   - Kiểm tra tài nguyên trước khi khai thác. 
   - Đợi cho đến khi lượng tài nguyên đã sử dụng trở về dưới 100%.

v1.3 [Xem trên Youtube](https://www.youtube.com/watch?v=kiVkAjCedSU)

- Xử lý lỗi `transaction is expired`: cố gắng nhận lại.

v1.4 [View on Youtube]()

- Chuyển sang đăng nhập 1 lần thay vì vòng lặp mở/tắt trình duyệt.
- Thêm dịch vụ giải captcha thứ hai: CapMonster.
- Xử lý lỗi `fail to fetch` error: cố gắng đăng nhập lại.
- .<img src="https://www.svgrepo.com/show/196054/premium.svg" width="20" height="20" title="In premium version"> **Lấy thời gian đợi (dựa trên đất hiện tại cũng như công cụ đang sử dụng).**
- .<img src="https://www.svgrepo.com/show/196054/premium.svg" width="20" height="20" title="In premium version"> **Chống treo khi khai thác.**
- Hỗ trợ proxy.
- Thêm tính năng ghi log.

v1.5 Sẽ phát hành sớm

- .<img src="https://www.svgrepo.com/show/196054/premium.svg" width="20" height="20" title="In premium version"> **Tự động lấy/làm mới cookies cho nhiều tài khoản.**
- .<img src="https://www.svgrepo.com/show/196054/premium.svg" width="20" height="20" title="In premium version"> **Chạy nhiều tài khoản với hồ sơ người dùng trình duyệt thật.**

###### Vui lòng thực hiện theo các bước sau:

1. Cài đặt ngôn ngữ **Python 3.9.x** https://www.python.org/downloads/.

[![SC2 Video](http://i3.ytimg.com/vi/_CoijjMXvYY/hqdefault.jpg)](https://www.youtube.com/watch?v=_CoijjMXvYY)

2. Cài đặt modules **requests**, **selenium**, **win10toast** `python -m pip install requests selenium win10toast`.

[![SC2 Video](http://i3.ytimg.com/vi/SQQRYAMl8Jk/hqdefault.jpg)](https://www.youtube.com/watch?v=SQQRYAMl8Jk)

3. (_Tự chọn_) Cài đặt IDE **PyCharm** https://www.jetbrains.com/pycharm/.

[![SC2 Video](http://i3.ytimg.com/vi/FqEXepao0go/hqdefault.jpg)](https://www.youtube.com/watch?v=FqEXepao0go)

4. (_Tự chọn_) Tải **Chrome WebDriver** https://chromedriver.chromium.org/.
5. Thực thi mã.
6. (_Tự chọn_) Sửa mã cho mục đích sử dụng cá nhân của bạn. Liên hệ tôi để có thêm tính năng mới!

###### Chú ý:

1. **Không thay đổi** kích thước của sổ trình duyệt.

# Auto Almost Everything

- Email: autoalmosteverything.2021@gmail.com
- Youtube: https://www.youtube.com/c/AutoAlmostEverything
- Github: https://github.com/autoalmosteverything
- Facebook: https://www.facebook.com/autoalmosteverything