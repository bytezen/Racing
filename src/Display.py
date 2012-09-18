'''
Created on Sep 18, 2012

@author: spellrh
'''
import pyglet
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

FPS = 60


def getSmoothConfig():
    """
    Sets up a configuration that allows of smoothing\antialiasing of the window.
    The return of this is passed to the config parameter of the created window.
    """
    try:
        # Try and create a window config with multisampling (antialiasing)
        config = pyglet.gl.Config(sample_buffers=1, samples=4,
                        depth_size=16, double_buffer=True)
    except pyglet.window.NoSuchConfigException:
        print "Smooth contex could not be aquiried."
        config = None
    return config



class Display(pyglet.window.Window):
    '''
    classdocs
    '''
    
    def __init__(self):
        super(Display, self).__init__(fullscreen=False,
                                           caption='pyglet sprite test')
                                            #, config=getSmoothConfig()) 

        # Schedule the update of this window, so it will advance in time.  If we
        # don't, the window will only update on events like mouse motion.
        pyglet.clock.schedule_interval(self.update, 1.0/FPS)

        # Set the background color:
        pyglet.gl.glClearColor(0,0,1,0)

        # Used for optimized sprite *drawing*.  It holds vertex lists, not Sprite objects.
        self.sprite_batch = pyglet.graphics.Batch()
        # Used for sprite *updating*, holds our Sprite objects.
        self.sprites = []

        # A label to draw how many sprites we have:
        self.spriteLabel = pyglet.text.Label(str(len(self.sprites)), font_name='Courier',
                                  font_size=36, x=self.width/2, y=32)

        # Setup debug framerate display:
        self.fps_display = pyglet.clock.ClockDisplay()

        # Run the application
        pyglet.app.run()

    #----------------------------
    # Scheduled Events:
    # via pyglet.clock.schedule_interval in __init__

    def update(self, dt):
        """
        Do all upating here:
        """
        logging.info("...updating")
        

    #----------------------------
    # Window() events:
    # Overridden Window() methods:

    def on_draw(self):
        """
        Do all drawing here.
        """
        self.clear()

        # Draw all our sprites:
        #self.sprite_batch.draw()

        # Draw text:
        #self.fps_display.draw()
        #self.spriteLabel.draw()
        
        logging.info("...drawing")

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Interaction with mouse.
        LMB creates sprite, RMB deletes sprite.
        
        if button == 1:
            # Create,... a SPRITE, added to our render batch:
            sprite = Sprite(self, x, y, batch=self.sprite_batch)
            self.sprites.append(sprite)
        else:
            if len(self.sprites):
                # Make sure it's deleted:
                self.sprites[-1].delete()
                self.sprites.pop()
        """
        logging.info("the mouse was pressed")                
            
        
if __name__ == '__main__':
    D = Display()
        