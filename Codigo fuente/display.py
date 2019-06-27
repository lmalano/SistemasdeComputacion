
#!/usr/bin/env python
import time
import requests
from datetime import datetime
from io import open

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, LCD_FONT, SINCLAIR_FONT, UKR_FONT

#opcion = '2'

def minute_change(device):
    '''When we reach a minute change, animate it.'''
    hours = datetime.now().strftime('%H')
    minutes = datetime.now().strftime('%M')

    def helper(current_y):
        with canvas(device) as draw:
            text(draw, (0, 1), hours, fill="white", font=proportional(CP437_FONT))
            text(draw, (15, 1), ":", fill="white", font=proportional(TINY_FONT))
            text(draw, (17, current_y), minutes, fill="white", font=proportional(CP437_FONT))
        time.sleep(0.1)
    for current_y in range(1, 9):
        helper(current_y)
    minutes = datetime.now().strftime('%M')
    for current_y in range(9, 1, -1):
        helper(current_y)


def animation(device, from_y, to_y):
    '''Animate the whole thing, moving it into/out of the abyss.'''
    hourstime = datetime.now().strftime('%H')
    mintime = datetime.now().strftime('%M')
    current_y = from_y
    while current_y != to_y:
        with canvas(device) as draw:
            text(draw, (0, current_y), hourstime, fill="white", font=proportional(CP437_FONT))
            text(draw, (15, current_y), ":", fill="white", font=proportional(TINY_FONT))
            text(draw, (17, current_y), mintime, fill="white", font=proportional(CP437_FONT))
        time.sleep(0.1) #0.1
        current_y += 1 if to_y > from_y else -1
        
def fechaCompleta():
	dia = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
	mes = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
	fecha = dia[datetime.now().weekday()] + " " + datetime.now().strftime('%d') + " de " + mes[datetime.now().month - 1] + " de " + datetime.now().strftime('%Y')
	return fecha


def getTemperatura():
    city = "Laguna Larga"
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=e2597d5e0dd6a8056a9a0649407fe807&units=metric'.format(city)
    res = requests.get(url)
    data = res.json()
    temp = "Laguna Larga: " + str(data['main']['temp']) + " C"
    return temp
    
def getOpcion():
	with open("/proc/hello", "r") as bye:
		opcion = bye.readline()
	#print(opcion)
	return opcion

def main(device):
    # The time ascends from the abyss...
    #animation(device, 8, 1)
	
    toggle = False  # Toggle the second indicator every second
    while True: #SE EJECUTA DE POR VIDA
		opcion = getOpcion()
		if opcion == "1":
			toggle = not toggle
			sec = datetime.now().second
			if sec == 59:
				# When we change minutes, animate the minute change
				minute_change(device)
			#elif sec == 30:
			#	# Half-way through each minute, display the complete date/time,
				# animating the time display into and out of the abyss.
			#	full_msg = fechaCompleta()
			#	animation(device, 1, 8)
			#	show_message(device, full_msg, fill="white", font=proportional(CP437_FONT))
			#	animation(device, 8, 1)
			#elif sec == 15:
			#	full_msg = getTemperatura()
			#	animation(device, 1, 8)
			#	show_message(device, full_msg, fill="white", font=proportional(CP437_FONT))
			#	animation(device, 8, 1)
			else:
				# Do the following twice a second (so the seconds' indicator blips).
				# I'd optimize if I had to - but what's the point?
				# Even my Raspberry PI2 can do this at 4% of a single one of the 4 cores!
				hours = datetime.now().strftime('%H')
				minutes = datetime.now().strftime('%M')
				with canvas(device) as draw:
					text(draw, (0, 1), hours, fill="white", font=proportional(CP437_FONT))
					text(draw, (15, 1), ":" if toggle else " ", fill="white", font=proportional(TINY_FONT))
					text(draw, (17, 1), minutes, fill="white", font=proportional(CP437_FONT))
				time.sleep(0.5)
			#FIN OPCION 1
		elif opcion == "2":
			full_msg = getTemperatura()
			show_message(device, full_msg, fill="white", font=proportional(CP437_FONT))
		#FIN OPCION 2
		elif opcion == "3":
			# Half-way through each minute, display the complete date/time,
			# animating the time display into and out of the abyss.
			full_msg = fechaCompleta()
			show_message(device, full_msg, fill="white", font=proportional(CP437_FONT))
		else:
		    show_message(device, "Opcion no valida pana", fill="white", font=proportional(CP437_FONT))

# Setup for Banggood version of 4 x 8x8 LED Matrix (https://bit.ly/2Gywazb)
serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=4, block_orientation=0, blocks_arranged_in_reverse_order=False)
device.contrast(5)




try:
    if __name__ == "__main__":
        main(device)
except KeyboardInterrupt:
    show_message(device, "Adios...", fill="white", font=proportional(UKR_FONT))
