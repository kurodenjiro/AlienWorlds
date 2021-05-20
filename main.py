# Auto Almost Everything
# Youtube Channel https://www.youtube.com/c/AutoAlmostEverything
# Please read README.md carefully before use

# Solve captcha by using 2Captcha, register here https://2captcha.com?from=11528745.

from datetime import datetime
import os, time, re
import urllib.parse as urlparse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Proxy
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from Modules import update, notification, log, captcha

app = 'Alien Worlds'
app_path = 'https://play.alienworlds.io'
login_path = 'https://all-access.wax.io'
wallet_path = 'https://wallet.wax.io'

# Browser config
opts = Options()
opts.binary_location = 'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe'  # <-- Change to your Chromium browser path, replace '\' with '\\'.
isBrave = True
if opts.binary_location.split('\\')[-1].split('.')[0].lower() != 'brave':
    isBrave = False
isNetBox = True
if opts.binary_location.split('\\')[-1].split('.')[0].lower() != 'netboxbrowser':
    isNetBox = False
opts.add_experimental_option('excludeSwitches', ['enable-automation'])
opts.add_experimental_option('useAutomationExtension', False)
opts.add_argument('−−mute−audio')
cap = DesiredCapabilities.CHROME.copy()
cap['platform'] = 'WINDOWS'
cap['version'] = '10'
proxy = 'YourProxy'  # <-- To use proxy, replace 'YourProxy' by proxy string, ex: 18.222.190.66:81
if proxy != '' and proxy != 'YourProxy':
    proxies = Proxy({
        'httpProxy': proxy,
        'ftpProxy': proxy,
        'sslProxy': proxy,
        'proxyType': 'MANUAL',
    })
    proxies.add_to_capabilities(cap)
    opts.add_argument('--ignore-ssl-errors=yes')
    opts.add_argument('--ignore-certificate-errors')
if isNetBox:
    chromedriver_path = '.\\Drivers\\chromedriver87.exe'
else:
    chromedriver_path = '.\\Drivers\\chromedriver89.exe'

# Account config
waxio_cookies = [
    {
        'name': 'token_id',
        # Replace by your token id -->
        'value': 'YourTokenID',
        # <-- Replace by your token id
        'domain': 'all-access.wax.io',
        'path': '/',
    },
    {
        'name': 'session_token',
        # Replace by your session token -->
        'value': 'YourSessionToken',
        # <-- Replace by your session token
        'domain': '.wax.io',
        'path': '/',
    },
]

log.screen_n_file('\n\n-+- -A- -U- -T- -O- -+- -A- -L- -M- -O- -S- -T- -+- -E- -V- -E- -R- -Y- -T- -H- -I- -N- -G- -+-',
                  False)
now = datetime.now()
log.screen_n_file('\n Script starts at ' + f'{now:%d/%m/%Y %H:%M:%S}', False)
log.file('Wax token ID is ' + waxio_cookies[0]['value'], False)
log.file('Wax session token is ' + waxio_cookies[1]['value'], False)

# Captcha config
autoCaptcha = True  # <-- Change to True if you want to use 2captcha to solve the captcha.
if autoCaptcha:
    captchaServiceName = 'CapMonster'  # <--- 2Captcha, CapMonster
    # Replace by your API Key -->
    rc = captcha.Captcha(captchaServiceName, 'YourSolvingCaptchaServiceAPIKey')
    # <-- Replace by your API Key
    log.file(captchaServiceName + ' API Key is ' + rc.getAPIKey(), False)

log.screen_n_file('', False)


# Draw on canvas
def CanvasDraw(browser, xoffset, yoffset):
    canvas = browser.find_element_by_xpath("//canvas[contains(@id, '#canvas')]")
    action = ActionChains(browser)
    action.move_to_element(canvas)
    action.move_by_offset(xoffset=xoffset, yoffset=yoffset)
    action.click()
    action.perform()
    # log.screen(' [*] Click to (%d, %d)' % (xoffset, yoffset))


# Claim TLM
def ClaimTLM():
    func = 'Claim TLM'

    # Start browser
    browser = webdriver.Chrome(desired_capabilities=cap, options=opts, executable_path=chromedriver_path)
    browser.set_page_load_timeout(60)
    browser.set_window_position(0, 0)
    if isBrave:
        browser.set_window_size(854, 720)
    else:
        browser.set_window_size(854, 676)

    # Login to Wax.io
    isLoggedIn = False
    try:
        browser.get(login_path)
        time.sleep(1)
        for cookie in waxio_cookies:
            browser.delete_cookie(cookie['name'])
            browser.add_cookie(cookie)
        browser.get(login_path)
        time.sleep(2)
        if 'Redirecting you to WAX Cloud Wallet' in browser.page_source or wallet_path in browser.current_url:
            isLoggedIn = True
            log.screen_n_file('[+] Logged-in to WAX.io.')
            notification.notify(app, 'Logged-in to WAX.io.')
        else:
            log.screen_n_file('[-] Can not login to WAX.io. Please check your cookies.')
            notification.notify(app, 'Can not login to WAX.io. Please check your cookies.')
    except Exception as ex:
        log.screen_n_file('[!] %s has exception: %s!' % (app, ex))
        notification.notify(app, '%s has exception: %s!' % (app, ex))

    if isLoggedIn:
        haveException = False
        isCaptchaExpired = False
        while True:
            if haveException:
                log.screen_n_file('', False)
                log.screen_n_file('[*] Restart game because of exception.')
                notification.notify(app, 'Restart game because of exception.')
            elif isCaptchaExpired:
                log.screen_n_file('', False)
                log.screen_n_file('[*] Restart game because of unstable anti-captcha service.')
                notification.notify(app, 'Restart game because of unstable anti-captcha service.')
            haveException = False
            isCaptchaExpired = False

            # Login to game
            gameTab = browser.current_window_handle
            try:
                browser.get(app_path)
                time.sleep(2)
                if isBrave:
                    while True:
                        try:
                            browser.switch_to.window(gameTab)
                            CanvasDraw(browser, 0, 93)  # Click to Login button
                            time.sleep(0.2)
                            if len(browser.window_handles) > 1:
                                break
                        except:
                            pass
                    time.sleep(2)
                    log.screen('[*] Preventing fail to fetch error... Feel free and wait for notification!', True)
                    notification.notify(app,
                                        'Preventing fail to fetch error... Feel free and wait for notification!')
                    for i in range(5):
                        time.sleep(1)
                        CanvasDraw(browser, 210, -125)
                        time.sleep(1)
                        CanvasDraw(browser, 0, 93)
                        time.sleep(1)
                        CanvasDraw(browser, -230, -225)  # Click to Home button.
                        time.sleep(1)
                        CanvasDraw(browser, 150, -95)
                else:
                    time.sleep(20)
                    CanvasDraw(browser, 0, 93)  # Click to Login button
                    time.sleep(20)
                log.screen_n_file('[+] Logged-in to AlienWorlds.')
                notification.notify(app, 'Logged-in to AlienWorlds.')
            except Exception as ex:
                log.screen_n_file('[!] %s has exception: %s!' % (app, ex))
                notification.notify(app, '%s has exception: %s!' % (app, ex))

            # Loop forever
            gameTab = browser.current_window_handle
            if isLoggedIn:
                while True:
                    delay_time = 600  # Delay time between two claims.
                    verify_time = 90  # Max time for verify the sign. Default is 1.5 minutes.
                    try:
                        log.screen_n_file('', False)
                        log.screen_n_file(func.upper())

                        # Get resource info
                        username = ''
                        cpu = 100
                        isOutofCPU = False
                        net = 100
                        isOutofNET = False
                        ram = 100
                        isOutofRAM = False

                        browser.execute_script('''
                            window.open(arguments[0], '_blank');
                        ''', wallet_path)
                        for handle in browser.window_handles:
                            browser.switch_to.window(handle)
                            if wallet_path in browser.current_url:
                                break
                        time.sleep(5)
                        try:
                            browser.find_element_by_xpath("//div[contains(@class, 'open-right')]").click()
                            time.sleep(1)
                            username = browser.find_element_by_xpath(
                                "//div[contains(@class, 'my-1 text-bold text-1-75rem')]").text
                            browser.find_element_by_xpath("//button[contains(text(), 'Resources')]").click()
                            time.sleep(1)
                            cards = browser.find_elements_by_tag_name('text')
                            cpu = int(re.findall('\d+', cards[0].text)[0])
                            net = int(re.findall('\d+', cards[2].text)[0])
                            ram = int(re.findall('\d+', cards[4].text)[0])
                        except:
                            pass
                        if cpu >= 100:
                            isOutofCPU = True
                        if net >= 100:
                            isOutofNET = True
                        if ram >= 100:
                            isOutofRAM = True

                        log.screen_n_file(
                            '  [+] Get resource information:\n   Username: %s\n   CPU: %d%%\n   NET: %d%%\n   RAM: %d%%' % (
                                username, cpu, net, ram))
                        notification.notify(app,
                                            'Username: %s\nCPU: %d%%\nNET: %d%%\nRAM: %d%%' % (username, cpu, net, ram))

                        browser.close()
                        time.sleep(1)
                        browser.switch_to.window(gameTab)

                        # Do new claim
                        if not (isOutofCPU or isOutofNET or isOutofCPU):
                            isTransactionExpired = False

                            while True:
                                if not isTransactionExpired:
                                    CanvasDraw(browser, 270, -100)  # Click to Mine button
                                    time.sleep(5)  # <-- Wait for to mine preparation screen
                                    CanvasDraw(browser, 0, 190)  # Click to Mine button
                                    time.sleep(5)
                                    while True:
                                        try:
                                            browser.switch_to.window(gameTab)
                                            CanvasDraw(browser, 0, 50)  # Click to Claim button if 1 button
                                            CanvasDraw(browser, -70,
                                                       60)  # Click to Claim button if 2 buttons, included Change Land button.
                                            time.sleep(0.2)
                                            if len(browser.window_handles) > 1:
                                                break
                                        except:
                                            pass

                                isTransactionExpired = False

                                time.sleep(5)
                                if len(browser.window_handles) > 1:
                                    signTab = None
                                    for handle in browser.window_handles:
                                        browser.switch_to.window(handle)
                                        if login_path in browser.current_url:
                                            signTab = handle
                                            break
                                    browser.switch_to.window(signTab)

                                # Sign to transaction
                                if autoCaptcha:
                                    log.screen_n_file('  [+] Automatically solve captcha.')

                                    tryTime = 2  # Retry 2 times if captcha is expired
                                    while True:
                                        try:
                                            recaptcha = browser.find_element_by_xpath(
                                                "//iframe[contains(@title, 'reCAPTCHA')]")
                                            sitekey = ''
                                            for query in urlparse.urlparse(
                                                    recaptcha.get_attribute('src')).query.split(
                                                '&'):
                                                if 'k=' in query:
                                                    sitekey = query.split('=')[1]
                                            token = rc.reCaptcha(sitekey, browser.current_url)
                                            if token != 'Expired':
                                                log.screen_n_file(
                                                    '    [+] Captcha response is %s.' % (
                                                            token[:7] + '...' + token[-7:]))
                                                # Run callback function
                                                browser.execute_script('''
                                                    function call_cbf(token) {
                                                        let widgetId = 0;
                                                        let widget = ___grecaptcha_cfg.clients[widgetId];
                                                        let callback = undefined;
                                                        for (let k1 in widget) {
                                                            let obj = widget[k1];
                                                            if (typeof obj !== "object") continue;
                                                            for (let k2 in obj) {
                                                                if (obj[k2] === null) continue;
                                                                if (typeof obj[k2] !== "object") continue;
                                                                if (obj[k2].callback === undefined) continue;
                                                                callback = obj[k2].callback;
                                                                break
                                                            }
                                                            if (callback === undefined) break;
                                                        }
                                                        callback.bind(this);
                                                        callback(token);
                                                    }
                                                    call_cbf(arguments[0]);
                                                ''', token)
                                                time.sleep(1)
                                                browser.find_element_by_xpath(
                                                    "//button[contains(@class, 'button button-secondary button-large text-1-5rem text-bold mx-1')]").click()
                                                time.sleep(10)
                                                browser.switch_to.window(gameTab)
                                                for i in range(-5, 5):
                                                    for j in range(-5, 5):
                                                        CanvasDraw(browser, 210 + i, -115 + j)  # Click to Close button
                                                time.sleep(2)
                                                CanvasDraw(browser, 0, 50)  # Click to Claim button if 1 button
                                                CanvasDraw(browser, -70,
                                                           60)  # Click to Claim button if 2 buttons, included Change Land button.
                                                time.sleep(5)
                                                if len(browser.window_handles) > 1:
                                                    isTransactionExpired = True
                                                    log.screen_n_file('  [-] Transaction is expired.')
                                                break
                                            else:
                                                # Try to solve captcha again
                                                browser.execute_script('''
                                                    window.grecaptcha.reset();
                                                ''')
                                                time.sleep(1)
                                                tryTime -= 1
                                                log.screen_n_file(
                                                    '    [-] Captcha is expired! %d times left to try.' % tryTime)
                                                notification.notify(app,
                                                                    'Captcha is expired! %d times left to try.' % tryTime)
                                                if tryTime <= 0:
                                                    browser.close()
                                                    time.sleep(1)
                                                    isCaptchaExpired = True
                                                    break
                                        except:
                                            pass
                                        time.sleep(0.2)
                                else:
                                    log.screen_n_file('  [+] Manually solve captcha.')
                                    notification.sound()
                                    notification.notify(app, 'Please solve captcha!')
                                    while True:
                                        try:
                                            time.sleep(0.2)
                                            if len(browser.window_handles) == 1:
                                                break
                                        except:
                                            pass
                                    time.sleep(5)
                                    browser.switch_to.window(gameTab)
                                    CanvasDraw(browser, 210, -115)  # Click to Close button
                                    time.sleep(2)
                                    CanvasDraw(browser, 0, 50)  # Click to Claim button if 1 button
                                    CanvasDraw(browser, -70,
                                               60)  # Click to Claim button if 2 buttons, included Change Land button.
                                    time.sleep(5)
                                    if len(browser.window_handles) > 1:
                                        isTransactionExpired = True

                                browser.switch_to.window(gameTab)
                                if isCaptchaExpired:
                                    break
                                if isTransactionExpired:
                                    continue

                                log.screen_n_file('  [+] Claimed. Wait for %f minutes.' % (round(delay_time / 60, 2)))
                                notification.notify(app, 'Claimed. Wait for %f minutes.' % (round(delay_time / 60, 2)))
                                time.sleep(verify_time)
                                CanvasDraw(browser, -230, -225)  # Click to Home button.
                                time.sleep(2)
                                break
                        else:
                            if isOutofCPU:
                                delay_time = 600
                                log.screen_n_file(
                                    '  [-] Out of CPU (%d%%). Wait for %f minutes.' % (
                                        cpu, (round(delay_time / 60, 2))))
                                notification.notify(app, 'Out of CPU (%d%%). Wait for %f minutes.' % (
                                    cpu, (round(delay_time / 60, 2))))
                            elif isOutofNET:
                                delay_time = 600
                                log.screen_n_file(
                                    '  [-] Out of NET (%d%%). Wait for %f minutes.' % (
                                        net, (round(delay_time / 60, 2))))
                                notification.notify(app, 'Out of NET (%d%%). Wait for %f minutes.' % (
                                    net, (round(delay_time / 60, 2))))
                            elif isOutofRAM:
                                delay_time = 600
                                log.screen_n_file(
                                    '  [-] Out of RAM (%d%%). Wait for %f minutes.' % (
                                        ram, (round(delay_time / 60, 2))))
                                notification.notify(app, 'Out of RAM (%d%%). Wait for %f minutes.' % (
                                    ram, (round(delay_time / 60, 2))))
                            delay_time += verify_time
                        if isCaptchaExpired:
                            delay_time = 300
                            log.screen_n_file(
                                '  [-] Captcha is expired at multi-time. Anti-captcha service is not stable now. Wait for %f minute then restart.' % (
                                    round(delay_time / 60, 2)))
                            notification.notify(app,
                                                'Captcha is expired at multi-time. Anti-captcha service is not stable now. Wait for %f minute then restart.' % (
                                                    round(delay_time / 60, 2)))
                            delay_time += verify_time
                        time.sleep(delay_time - verify_time)
                        if isCaptchaExpired:
                            break
                    except Exception as ex:
                        haveException = True
                        log.screen_n_file('[!] %s has exception: %s. Restart now!' % (app, ex))
                        notification.notify(app, '%s has exception: %s. Restart now!' % (app, ex))
                        time.sleep(1)
                        break


if update.check():
    log.screen_n_file('[*] New version is released. Please download it! Thank you.')
    notification.notify(app, 'New version is released. Please download it! Thank you.')
    os.system('start https://www.youtube.com/c/AutoAlmostEverything')
else:
    ClaimTLM()
