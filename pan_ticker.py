import copy, datetime, json, time
from urllib.request import Request, urlopen
from six.moves.urllib_parse import quote_plus

pan_price_old = 0 # initiate
first_loop_done = 0

while True:
    time_now = str(datetime.datetime.now().strftime('%H:%M:%S')) 
    req = Request('https://kg7jyq8yn3nzcwzxnl7r.bitpanda.com/v1/ticker', headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    webpage_json = json.loads(webpage)
    pan_price_new = float(webpage_json['PAN']['EUR'])
    if abs(pan_price_new - pan_price_old) > 0.001 and first_loop_done != 0:
        print(20*'-' + ' Big change ' + 20*'-')
    if pan_price_new != pan_price_old:
        if first_loop_done == 0:
            sign = ''
            first_loop_done = 1
        elif pan_price_new - pan_price_old > 0:
            sign = '(+)'
        else:
            sign = '(-)'
        print(time_now + '\t' + str(pan_price_new) + '\t' + sign)
    time.sleep(5)
    pan_price_old = pan_price_new