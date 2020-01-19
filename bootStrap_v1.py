exec(open('/home/pi/devel/rpipySSD1306/start.py').read())
import classMixer
mixr = classMixer.Mixer(disp)
mixr._update_rects()
mixr._write_levels()
