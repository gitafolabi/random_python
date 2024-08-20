import wifi_qrcode_generator.generator

qr_code = wifi_qrcode_generator.generator.wifi_qrcode(
    ssid='Home WiFi', hidden=False, authentication_type='WPA', password='password'
)
qr_code.print_ascii()
qr_code.make_image().save('qr.png')
