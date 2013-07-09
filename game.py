

class IllegalRoll(Exception):
    pass


class GameOver(IllegalRoll):
    pass


class Game:
    """
    Keeps track of score in a single game.
    Usage:
        g = Game()
        g.full_game([10, 3, 7, 6, 1, 10, 10, 10, 2, 8, 9, 0, 7, 3, 10, 10, 10])
    See also g.roll()
    """

    # state variables
    _active_multipliers = [1, 1]
    _frame_i = 1
    _roll_in_frame_i = 0
    _pins_in_this_frame = 0
    _award_rolls_i = 0
    _score = 0

    def roll(self, pins_down):
        """
        Records each roll and calculates new score immediately.
        """

        if 0 > pins_down or pins_down > 10:
            raise IllegalRoll('not in range 0 .. 10')

        self._prepare_state()
        #self.print_state()
        self._add_to_score(pins_down)
        #print self.get_score()

    def _prepare_state(self):
        """
        Count frames and rolls.
        """
        self._roll_in_frame_i += 1
        if self._roll_in_frame_i > 2:
            self._frame_i += 1
            self._roll_in_frame_i = 1

        if self._frame_i > 10 + self._award_rolls_i:
            raise GameOver('cannot open more then 10 + {} frames!'.format(self._award_rolls_i))

        if self._roll_in_frame_i == 1:
            self._pins_in_this_frame = 0

    def _add_to_score(self, pins_down):
        """
        Handles total score. Also keeps track of strike and spare conditions.
        """
        multiplier = self._active_multipliers.pop(0)
        self._active_multipliers.append(1)
        self._score += pins_down * multiplier
        self._pins_in_this_frame += pins_down
        if self._pins_in_this_frame > 10:
            raise IllegalRoll('cannot down more then 10 pins in a frame!')

        if self._pins_in_this_frame == 10:
            if self._roll_in_frame_i == 1:
                if self._frame_i < 10:
                    self._active_multipliers[0] += 1
                    self._active_multipliers[1] += 1
                if self._frame_i == 10:
                    self._award_rolls_i = 2
            else:
                if self._frame_i < 10:
                    self._active_multipliers[0] += 1
                if self._frame_i == 10:
                    self._award_rolls_i = 1
            self._roll_in_frame_i = 2


    def get_score(self):
        return self._score

    def is_game_over(self):
        if self._award_rolls_i:
            return False
        if self._frame_i == 10 and self._roll_in_frame_i == 2:
            return True
        return False

    def print_state(self):
        print "frame: {}".format(self._frame_i)
        print "roll: {}".format(self._roll_in_frame_i)


    def full_game(self, rolls):
        """
            A simple shorthand, calls self.roll() repeatedly.
            Returns total score.
        """
        for roll in rolls:
            self.roll(roll)
        return self.get_score()



