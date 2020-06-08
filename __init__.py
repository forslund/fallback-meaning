from mycroft.skills.core import FallbackSkill


class MeaningFallback(FallbackSkill):
    """
    A Fallback skill to answer the question about the
    meaning of life, the universe and everything.
    """
    def initialize(self):
        """Registers the fallback skill."""
        # Warning:
        # This sets the fallback priority to 1, making it happen before
        # all other fallbacks, even padatious intents.
        # This is good for this example but BAD in general,
        # a fallback prio between 11 and 89 is good for most skills.

        self.register_fallback(self.handle_fallback, 1)

        # Any other initialize code goes here

    def handle_fallback(self, message):
        """Answers the ultimate question

        What is the meaning of life, the universe and everything.
        """
        utterance = message.data.get("utterance")

        # get keywords for current language
        what = self.dialog_renderer.render('query')
        meaning = self.dialog_renderer.render('meaning')
        life = self.dialog_renderer.render('life')
        universe = self.dialog_renderer.render('universe')
        everything = self.dialog_renderer.render('everything')

        if (what in utterance and
                meaning in utterance and
                (life in utterance or universe in utterance
                    or everything in utterance)):
            self.speak('42')
            return True  # Indicate that the utterance was handled
        else:
            return False


def create_skill():
    return MeaningFallback()
