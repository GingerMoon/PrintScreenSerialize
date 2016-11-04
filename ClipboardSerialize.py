from PIL import ImageGrab
from pynput.keyboard import Key, Listener

def on_press(key):
	print('{0} press'.format(key))


def on_release(key):
    on_release.count += 1
    #print('{0} release'.format(key))
    if key == Key.esc:
        # Stop listener
        return False
    if(key == Key.print_screen):
    	im = ImageGrab.grabclipboard()
    	name = 'C:/screenshots/' + str(on_release.count) + '.png'
        im.save(name,'PNG')
on_release.count = 10

# Collect events until released
with Listener(on_release=on_release) as listener:
    listener.join()


#https://pypi.python.org/pypi/clipboard/0.0.4
#http://omz-software.com/pythonista/docs/ios/Image.html#module-Image
#https://pypi.python.org/pypi/pyscreenshot
#http://stackoverflow.com/questions/7045264/how-do-i-read-a-jpg-or-png-from-the-windows-clipboard-in-python-and-vice-versa
#https://pypi.python.org/pypi/pynput/1.0