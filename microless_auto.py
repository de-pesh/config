import requests
import cloudscraper
from bs4 import BeautifulSoup
from windows_toasts import Toast, ToastDisplayImage, WindowsToaster

def Check_Changes(URL):
    scraper = cloudscraper.create_scraper()  # returns a CloudScraper instance
# Or: scraper = cloudscraper.CloudScraper()  # CloudScraper inherits from requests.Session
    ct = scraper.get(URL).text
    soup = BeautifulSoup(ct,"html.parser")
    # page = requests.get(URL)
    # soup = BeautifulSoup(page.content, "html.parser")
    # print(soup)
    data = soup(text="Dubai_Deals")
    print(data, end=" ")
    if(len(data) == 0):
        
        toaster = WindowsToaster('Price Alert')
        newToast = Toast()
        newToast.AddImage(ToastDisplayImage.fromPath('C:\\Users\\PREMIER COMPUTERS\\Desktop\\trash\\alert.png'))
        newToast.text_fields = ['Click to check']
        # Inline lambda function. This could also be an actual function
        newToast.launch_action = URL
        # Send it
        toaster.show_toast(newToast)
        print("NOT OK")
    else:
        print("OK")

url_list = ["https://uae.microless.com/product/hp-color-laser-179fnw-wireless-all-in-one-laser-printer-with-mobile-printing-built-in-ethernet-4zb97a/", "https://uae.microless.com/product/canon-i-sensys-lbp-6030b-laser-printer-18ppm-mono-printing-speed-monochrome-laser-beam-printing-725-cartridge-up-to-2400-x-600-dpi-wifi-mobile-printing-8468b006aa/", "https://uae.microless.com/product/ricoh-fi-8170-color-duplex-document-scanner-70-ppm-simplex-scanning-speed-600-dpi-resolution-100-sheets-adf-capacity-network-enabled-clear-image-capture-black-white-pa03810-b051/", "https://uae.microless.com/product/hp-mfp-137fnw-multifunction-laser-printer-print-copy-scan-20ppm-printing-speed-ethernet-interface-150-sheets-input-capacity-128-mb-ram-size-white-6hu12ab19-4zb84a/", "https://uae.microless.com/product/hp-color-laserjet-pro-wireless-all-in-one-laser-printer-m183fw/", "https://uae.microless.com/product/hp-color-laser-150a-home-office-printer-white-4zb94a/", "https://uae.microless.com/product/logitech-g233-prodigy-wired-gaming-headset-black-cyan-981-000703/", "https://uae.microless.com/product/epson-ecotank-l6290-a4-wi-fi-duplex-all-in-one-ink-jet-printer-4800-x-1200-dpi-resolution-15-5ipm-print-speed-7500-pages-lcd-screen-adf-capability-spill-free-ink-refilling-black-l6290/", "https://uae.microless.com/product/hp-cp5225dn-laserjet-professional-color-laser-printer-600-x-600-dpi-20-ppm-print-speed-automatic-duplex-printing-two-line-lcd-display-350-sheets-input-capacity-usb-2-0-eth/", "https://uae.microless.com/product/hp-color-laserjet-enterprise-mfp-m776dn-a3-functions-print-copy-scan-hi-speed-usb-2-0-gigabit-ethernet-network-up-to-1200-x-1200-dpi-up-to-46ppm-black-and-colour-laser-printer-t3u55a/", "https://uae.microless.com/product/brother-wireless-all-in-one-inkjet-printer-17-0-9-5ipm-mono-color-mobile-wireless-printing-1-200-x-6-000dpi-resolution-refill-ink-tank-system-replaceable-ultra-high-yield-ink-black-dcp-t520w/", "https://uae.microless.com/product/hp-m480f-color-laserjet-enterprise-multifunction-printer-up-to-29ppm-print-speed-auto-duplex-4-3-color-touch-50-sheet-adf-250-sheets-input-tray-print-copy-scan-fax-white-3qa55a/", "https://uae.microless.com/product/hp-laserjet-pro-4003dw-a4-laser-printer-lcd-display-up-to-40ppm-print-speed-1200x1200-dpi-resolution-up-to-80000-pages-duty-cycle-2-4-5-ghz-wi-fi-bluetooth-white-2z610a/", "https://uae.microless.com/product/fellowes-powershred-lx25-cross-cut-shredder-11-5l-bin-capacity-shred-up-to-6-sheets-4x37mm-cross-cut-size-advanced-safety-lock-technology-black-lx25/", "https://uae.microless.com/product/epson-ecotank-l15150-a3-wi-fi-duplex-aio-ink-tank-printer-25-ipm-print-speed-2400x1200-dpi-scan-resolution-50-pages-adf-250-sheets-tray-capacity-usb-eth-wifi-wi-fi-direct-black-c11ch72403da/", "https://uae.microless.com/product/epson-ecotank-multifunction-mono-printer-c11cg27404by-m2140/", "https://uae.microless.com/product/fellowes-powershred-p-30c-cross-cut-shredder-4-gallon-bin-15l-shreds-up-to-6-sheets-4x34mm-cut-size-p-4-security-level-black-p30c/", "https://uae.microless.com/product/epson-ecotank-l3260-a4-color-3-in-1-printer-with-wi-fi-direct-lcd-screen-1200-dpix2400-dpi-resolution-33ppm-print-speed-200-dpi-scan-speed-100-sheets-paper-tray-black-c11cj66414/", "https://uae.microless.com/product/hp-color-laserjet-pro-mfp-3303fdw-printer-print-speed-up-to-25-ppm-ethernet-usb-wi-fi-dynamic-security-enabled-100-sheets-output-tray-4-3-diagonal-color-tft-display-499m8a/", "https://uae.microless.com/product/epson-ecotank-office-ink-tank-printer-black-l5590/", "https://uae.microless.com/product/epson-ecotank-l3252-home-ink-tank-multifunction-printer-a4-color-3-in-1-printer-with-wifi-and-smartpanel-app-connectivity-c11cj67424/", "https://uae.microless.com/product/epson-ecotank-l4260-wi-fi-duplex-aio-ink-tank-printer-borderles-printing-up-to-a4-size-auto-duplex-5760x1440-dpi-resolution-10-5ipm-5-0ipm-print-speed-spill-free-ink-refilling-black-c11cj63415/", "https://uae.microless.com/product/zebra-zd621-barcode-desktop-label-printer-thermal-transfer-printing-300dpi-print-resolution-152-mm-s-printing-speed-118-mm-label-width-bluetooth-ethernet-connectivity-gray-zd6a043-30ef00ez/", "https://uae.microless.com/product/canon-i-sensys-mf655cdw-all-in-one-color-laser-printer-print-copy-scan-12-7cm-colored-touchscreen-18-21-ppm-a4-print-speed-up-to-1200-x-1200-dpi-print-resolution-white-655dw/", "https://uae.microless.com/product/hp-color-laserjet-pro-4303dw-a4-colour-laser-multifunction-printer-print-copy-scan-adf-duplex-print-speed-up-to-35-33-ppm-4-3-wled-display-usb-ethernet-wi-fi-white-5hh65a/", "https://uae.microless.com/product/canon-pixma-g3410-megatank-inkjet-printer-1-2-lcd-display-up-to-8-8-5-0-ipm-print-speed-cis-flatbed-photo-document-scanner-2-fine-cartridges-print-technology-black-g3410/", "https://uae.microless.com/product/xerox-b225-multifunction-printer-up-to-36ppm-printing-speed-250-sheets-standard-media-capacity-600dpi-resolution-copy-print-scan-ethernet-wifi-usb-connectivity-white-b225-dni/", "https://uae.microless.com/product/epson-tm-t20iii-012-ethernet-pos-receipt-printer-ep-c31ch51012a0/", "https://uae.microless.com/product/hp-officejet-pro-9730-wide-format-all-in-one-printer-print-copy-scan-up-to-34-ppm-print-speed-automatic-duplex-printing-up-to-4800x1200-optimized-dpi-1200x1200-rendered-dpi-white-537p5c/", "https://uae.microless.com/product/canon-i-sensys-mf453dw-mono-laser-printer-print-copy-scan-up-to-38-ppm-print-speed-1200-x-1200-max-dpi-resolution-12-7cm-lcd-colour-touch-screen-white-5161c007/"]


for url in url_list:
    Check_Changes(url)


toaster = WindowsToaster('Check Completed')
newToast = Toast()
newToast.AddImage(ToastDisplayImage.fromPath('C:\\Users\\PREMIER COMPUTERS\\Desktop\\trash\\ok.png'))
newToast.text_fields = ['All products reviewed']
toaster.show_toast(newToast)