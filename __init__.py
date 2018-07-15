# TODO: Add an appropriate license to your skill before publishing.  See
# the LICENSE file for more information.

# Below is the list of outside modules you'll be using in your skill.
# They might be built-in to Python, from mycroft-core or from external
# libraries.  If you use an external library, be sure to include it
# in the requirements.txt file so the library is installed properly
# when the skill gets installed later by a user.

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG
import os

# Each skill is contained within its own class, which inherits base methods
# from the MycroftSkill class.  You extend this class as shown below.

class LaptopControlSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(LaptopControlSkill, self).__init__(name="LaptopControlSkill")
        
    @intent_handler(IntentBuilder("").require("Start").require("Program"))
    def handle_start_program_intent(self, message):
        if message.data["Program"] == "thunderbird":
            os.system("su - johanna -c 'thunderbird &'")
        elif message.data["Program"] == "spotify":
            os.system("su - johanna -c 'spotify &'")
        elif message.data["Program"] == "office":
            os.system("su - johanna -c 'lowriter &'")
        elif message.data["Program"] == "gimp":
            os.system("su - johanna -c 'gimp &'")
        elif message.data["Program"] == "notes":
            os.system("su - johanna -c 'nixnote2 &'")
        elif message.data["Program"] == "browser":
            os.system("su - johanna -c 'vivaldi &'")
        elif message.data["Program"] == "inkscape":
            os.system("su - johanna -c 'inkscape &'")
        elif message.data["Program"] == "calculator":
            os.system("su - johanna -c 'galculator &'")
        else:
            self.speak_dialog("program.not.found")
            return
        self.speak_dialog("program.started", data={"program": message.data["Program"]})

    @intent_handler(IntentBuilder("").require("Stop").require("Program"))
    def handle_stop_program_intent(self, message):
        if message.data["Program"] == "thunderbird":
            os.system("su - johanna -c 'killall thunderbird &'")
        elif message.data["Program"] == "spotify":
            os.system("su - johanna -c 'killall spotify &'")
        elif message.data["Program"] == "office":
            os.system("su - johanna -c 'killall lowriter &'")
        elif message.data["Program"] == "gimp":
            os.system("su - johanna -c 'killall gimp &'")
        elif message.data["Program"] == "notes":
            os.system("su - johanna -c 'killall nixnote2 &'")
        elif message.data["Program"] == "browser":
            os.system("su - johanna -c 'killall vivaldi &'")
        elif message.data["Program"] == "inkscape":
            os.system("su - johanna -c 'killall inkscape &'")
        elif message.data["Program"] == "calculator":
            os.system("su - johanna -c 'killall galculator &'")
        else:
            self.speak_dialog("program.not.found")
            return
        self.speak_dialog("program.stopped", data={"program": message.data["Program"]})



    # The "stop" method defines what Mycroft does when told to stop during
    # the skill's execution. In this case, since the skill's functionality
    # is extremely simple, there is no need to override it.  If you DO
    # need to implement stop, you should return True to indicate you handled
    # it.
    #
    # def stop(self):
    #    return False

# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return LaptopControlSkill()
