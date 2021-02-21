from adafruit_magtag.magtag import MagTag
import time
DATA_SOURCE_BTC = "https://api.coinbase.com/v2/prices/BTC-USD/buy.json"
DATA_LOCATION_BTC = ['data', 'amount']

DATA_SOURCE_LTC = "https://api.coinbase.com/v2/prices/LTC-USD/buy.json"
DATA_LOCATION_LTC = ['data', 'amount']

DATA_SOURCE_ETH = 'https://api.coinbase.com/v2/prices/ETH-USD/buy.json'
DATA_LOCATION_ETH = ['data', 'amount']


magtag = MagTag(
    url=DATA_SOURCE_BTC,
    json_path=DATA_LOCATION_BTC,
)

#def WifiReconnectionSys():
    #if magtag.network.isconnected() == False:
            #magtag.network.connect()
            #enter_light_sleep(30)

magtag.peripherals.neopixel_disable = True
magtag.network.connect()
#WifiReconnectionSys()
requests = magtag.network.requests


magtag.add_text(
    text_position=(
        (magtag.graphics.display.width // 2) - 1,
        (magtag.graphics.display.height // 2) - 1,
    ),
    text_scale=2,
    text_anchor_point=(0.5, 0.5),
)
#=-=-=-Debugging Code=-=-=-=
#try:
#    value = magtag.fetch()
#    magtag.peripherals.play_tone(513, 5)
#    print("Response is", value)
#except (ValueError, RuntimeError) as e:
#    print("Some error occured, retrying! -", e)
#BTC, ETH, LTC
button_colors = ((219, 146, 0), (180, 57, 255), (226, 226, 226), (180, 0, 255))
button_tones = (1047, 1318, 1568, 1724)


def ButtonPressed():
    for i, b in enumerate(magtag.peripherals.buttons):
        if not b.value:
            magtag.peripherals.neopixel_disable = False
            magtag.peripherals.neopixels.fill(button_colors[i])
            magtag.peripherals.play_tone(button_tones[i], 0.25)
            return i
        else:
            continue
last_button = 4
current_price = "yomma"
previous_price = "yomomma"

while 69:
    #last_button = 4
    while not magtag.peripherals.any_button_pressed:
    #WifiReconnectionSys()
        if last_button == 0:
            response = requests.get('https://api.coinbase.com/v2/prices/BTC-USD/buy.json')
            data = response.json()
            price = data['data']['amount']
            magtag.set_text('Bitcoin: $%s' % price)
            time.sleep(30)
            magtag.enter_light_sleep(15)
        elif last_button == 1:
            response = requests.get('https://api.coinbase.com/v2/prices/ETH-USD/buy.json')
            data = response.json()
            price = data['data']['amount']
            magtag.set_text('Ethereum: $%s' % price)
            time.sleep(30)
            magtag.enter_light_sleep(15)
        elif last_button == 2:
            response = requests.get('https://api.coinbase.com/v2/prices/LTC-USD/buy.json')
            data = response.json()
            price = data['data']['amount']
            magtag.set_text('Litecoin: $%s' % price)
            time.sleep(30)
            magtag.enter_light_sleep(15)
        elif last_button == 3:
            last_button = 4
            magtag.refresh()
        else:
            magtag.set_text("Menu!")
            magtag.peripherals.neopixel_disable = False
            magtag.peripherals.neopixels.fill((201, 253, 201))
            time.sleep(30)
            magtag.enter_light_sleep(10)
    last_button = int(ButtonPressed())


    #elif magtag.peripherals.button_d_pressed:
        #response = requests.get('https://api.coinbase.com/v2/prices/LTC-USD/buy.json')
        #data = response.json()
        #price = data['data']['amount']
        #magtag.set_text('Litecoin: $%s' % price)
        #enter_light_sleep(300)
