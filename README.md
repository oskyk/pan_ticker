# pan_ticker
This hi-end, hi-fi, hi-tech ticker for the Pantos multi-blockchain cryptocurrency token uses several codings and much algorithm to access top-secret data from the Bitpanda website, process these data into floating points and display the unencrypted bits in HD on your command line. Use at own risk. 

tl;dr: It's a super-simple price ticker for PAN.

While running, it will check every five seconds for a price change on PAN using the Bitpanda ticker. If there has been a change, it displays the current time followed by the new price and whether the change is positive or negative. If the change is big (>= 0.001 EUR), it displays an extra message to grab your attention. 

Example output:

```
14:25:20        0.0522  (-)
14:30:20        0.0516  (-)
-------------------- Big change -------------------- 
14:35:21        0.0498  (-)
14:40:23        0.0504  (+)
14:45:23        0.0507  (+)
```

PHP version can be found here:
https://gist.github.com/cloudminingpools/251d1eab4462a1108dba8c9129f151f0

If this or anything on my GitHub helped you, informed you or made you smile, or if you've just got some superfluous BTC lying around, feel free to drop a penny into this bitcoin fountain to help a guy through university: `385GUu3BjjpkijKS2aFU2t4NqvmFXdnX9x` 

Thanks for reading!
