exec(open('/home/pi/devel/rpipySSD1306/start.py').read())
import classMixer_v1
mixr = classMixer_v1.Mixer(disp)
mixr._update_rects()
mixr._write_levels()
