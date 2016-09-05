# MorsePy

[![MorsePy Demo](morsepy.gif "MorsePy Demo")][http://elucidation.github.io/MorsePy/]

`morse.py` contains a simple set of python functions to translate alphanumeric characters to morse code and back

`morse_sound.py` generates base 64 encoded strings of the dit and dah sounds for use in the HTML5 page.

The wave sounds are a 800Hz tone, 100ms and 300ms for dit and dah respectively, at a framerate of 4.410 Khz.

## Example output for morse.py

```
--------------------------------------------------------------
Original: THIS IS NUMBER 1 TEST.
   Morse: - .... .. ...  .. ...  -. ..- -- -... . .-.  .----  - . ... - .-.-.-
and Back: THIS IS NUMBER 1 TEST.
Valid? Yes
--------------------------------------------------------------
--------------------------------------------------------------
Original: WHAT IS THE MEANING OF LIFE, THE UNIVERSE, AND EVERYTHING?
   Morse: .-- .... .- -  .. ...  - .... .  -- . .- -. .. -. --.  --- ..-.  .-.. .. ..-. . --..--  - .... .  ..- -. .. ...- . .-. ... . --..--  .- -. -..  . ...- . .-. -.-- - .... .. -. --. ..--..
and Back: WHAT IS THE MEANING OF LIFE, THE UNIVERSE, AND EVERYTHING?
Valid? Yes
--------------------------------------------------------------
--------------------------------------------------------------
Original: WIERD CHARS # IS !@#$%^&*()<> BLOOP 
   Morse: .-- .. . .-. -..  -.-. .... .- .-. ...    .. ...  -.-.-- .--.-. ...-..- .-... -.--. -.--.-  -... .-.. --- --- .--.  
and Back: WIERD CHARS  IS !@$&() BLOOP 
Valid? No
--------------------------------------------------------------
```

## Dit/Dah output


### Dit

```
UklGRpYDAABXQVZFZm10IBAAAAABAAEAOhEAAHQiAAACABAAZGF0YXIDAAAAACU6lTBz7sHAtdzCIYA/TBOg0B7FLv5cOcAxNvAPwTPbMiCzPwcV39FuxFv8hzjgMvzxacG52Zse2T++FifTycOK+qY39jPF89HBR9j+HPI/cBh51DHDufi6NgE1kPVGwt3WWxv+Px0a1NWmwur2wjUBNl73yMJ81bIZ/D/EGzfXKMId9b809jYt+VbDJNQEGO0/Zh2j2LbBUvOxM983/vrxw9TSURbRPwEfF9pSwYrxmTK9OND8mcSO0ZkUqD+WIJPb+sDF73Yxjzmi/kzFUtDdEnE/JSIX3a/AA+5IMFU6dAAMxiDPHREtP6wjot5ywEXsES8PO0cC2Mb3zVkP3D4sJTPgQsCL6tAtvTsZBLDH2sySDX4+pCbM4R/A1eiFLF486wWUyMbLyQsTPhQoauMJwCXnMSvzPLsHg8m+yv0Jmz18KQ/lAcB55dQpez2JCX7KwckvCBY92yq55gbA0+NvKPY9VguDy8/IXwaEPDEsaegYwDPiASdkPiANlMzox44E5jt+LR3qOMCZ4Islxj7oDq/NDce8Ajw7wi7W62XABd8NJBo/rBDVzj7G6QCFOvwvk+2fwHndhyJhP20SBNB7xRf/wjkrMVTv5sDz2/sgmz8qFD7RxMRE/fM4UTIY8TrBddpnH8g/4xWC0hrEcvsYOGwz4PKcwf/YzR3oP5cXz9N8w6H5MTd9NKr0CsKR1y0c+j9HGSXV6sLR9z82gjV39oXCLNaHGv8/8RqE1mXCA/ZCNX02RfgNw8/U2xj3P5Yc7NftwTf0OjRsNxX6osN70ysX4T80HlzZgsFu8iYzUDjn+0PEMNJ1Fb4/zR/U2iTBp/AJMig5uf3xxO/QuxOOP14hVNzTwOPu4DD0OYz/q8W4z/0RUT/pItvdj8Aj7a4vtDpeAXHGis47EAY/bSRq31jAZ+tyLmc7MANDx2fNdg6uPukl/+AvwK/pLC0PPAIFIchPzK4MSj5dJ5riE8D859wrqjzTBgrJQcvjCtg9ySg85ATATuaEKjg9ogj/yT7KFglaPSwq4+UCwKXkIym6PXAK/8pGyUcHzzyHK5DnDsAC47knLz47DArMWsh2BTc82SxC6SfAZeFHJpc+BA4gzXnHpQOSOyEu+epNwM7fzSTxPsoPQM6kxtIB4jpgL7TsgMA+3ksjPz+NEWvP28U=
```

#### Dah

```
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
```