import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Starting Template"

ENEMY_SCALING_PLAYER = 0.5
ENEMY_SCALING_COIN = 0.2
ENEMY_COUNT = 50

SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_ENEMY = 0.5
SPRITE_SCALING_PROJECTILE = 0.7
BULLET_SPEED = 5

class Enemy(arcade.Sprite):
    """
    This class represents the coins on our screen. It is a child class of
    the arcade library's "Sprite" class.
    """

    def reset_pos(self):

        # Reset the coin to a random spot above the screen
        self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                         SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):

        # Move the coin
        self.center_y -= 1

        # See if the coin has fallen off the bottom of the screen.
        # If so, reset it.
        if self.top < 0:
            self.reset_pos()


class MyGame(arcade.Window):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.AMAZON)

        # If you have sprite lists, you should create them here,
        # and set them to None

               # Variables that will hold sprite lists
        self.player_sprite_list = None
        self.enemy_sprite_list = None
        self.projectile_sprite_list = None

        # Set up the player info
        self.player_sprite = None

    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        # Create your sprites and sprite lists here

        # Sprite lists
        self.player_sprite_list = arcade.SpriteList()
        self.enemy_sprite_list = arcade.SpriteList()
        self.projectile_sprite_list = arcade.SpriteList()

        # Set up the player
        # Character image from kenney.nl
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 400
        self.player_sprite.center_y = 50
        self.player_sprite_list.append(self.player_sprite)


        # Set up enemy
        for i in range(1, ENEMY_COUNT):
            enemy = Enemy(":resources:images/items/coinGold.png", SPRITE_SCALING_ENEMY)
        # Set its position to a random height and off screen right
            enemy.left = random.randint(0, SCREEN_WIDTH)
            enemy.top = random.randint(0, SCREEN_HEIGHT)

            self.enemy_sprite_list.append(enemy)
 
        # Set up projectile
        self.projectile_sprite = arcade.Sprite(":resources:images/space_shooter/laserBlue01.png", SPRITE_SCALING_PROJECTILE)
        self.projectile_sprite_list.append(self.projectile_sprite)
   
        # All sprite list
        self.all_sprites = arcade.SpriteList()

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()

        # Call draw() on all your sprite lists below
        self.enemy_sprite_list.draw()
        self.player_sprite_list.draw()
        self.projectile_sprite_list.draw()

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        self.enemy_sprite_list.update()
        self.projectile_sprite_list.update()

                # Generate a list of all sprites that collided with the player.
        hit_list = arcade.check_for_collision_with_list(self.projectile_sprite,
                                                        self.enemy_sprite_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for enemy in hit_list: 
            enemy.remove_from_sprite_lists()

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        http://arcade.academy/arcade.key.html
        """
        # self.projectile_sprite.center_y = self.projectile_sprite.center_y + 5

                # Create a bullet
        self.projectile_sprite = arcade.Sprite(":resources:images/space_shooter/laserBlue01.png", SPRITE_SCALING_PROJECTILE)

        # The image points to the right, and we want it to point up. So
        # rotate it.
        self.projectile_sprite.angle = 90

        # Give the bullet a speed
        self.projectile_sprite.change_y = BULLET_SPEED

        # Position the bullet
        self.projectile_sprite.center_x = self.player_sprite.center_x
        self.projectile_sprite.bottom = self.player_sprite.top

        # Add the bullet to the appropriate lists
        self.projectile_sprite_list.append(self.projectile_sprite)

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        self.player_sprite.center_x = x

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass


def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
