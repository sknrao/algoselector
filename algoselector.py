# Copyright 2021 Spirent Communications.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Tool to suggest which ML approach is more applicable for
a particular data and usecase.
"""


from __future__ import print_function
import signal
import sys
from pypsi import wizard as wiz
from pypsi.shell import Shell

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class AlgoSelectorWizard(object):
    """
    Class to create wizards
    """
    def __init__(self):
        """
        Perform Initialization.
        """
        self.shell = Shell()
        self.main_values = {}
        self.supervized_values = {}
        self.unsupervized_values = {}
        self.reinforced_values = {}
        self.wiz_main = None
        self.wiz_main_l1 = None
        self.wiz_main_l2_a = None
        self.wiz_main_l2_b = None
        self.wiz_main_l3 = None
        self.wiz_main_l4 = None
        self.wiz_supervized = None
        self.wiz_unsupervized = None
        self.wiz_reinforced = None


    ############# All the Wizards ##################################
    def main_wizard_l1(self):
        """
        The Main Wizard
        """
        self.wiz_main_l1 = wiz.PromptWizard(
            name=bcolors.OKBLUE+"Do you Need ML - Data Availability"+bcolors.ENDC,
            description="",
            steps=(
                # The list of input prompts to ask the user.
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="data_availability",
                    # Display name
                    name=bcolors.HEADER+"Do you have access to data about different situations, or that describes a lot of examples of situations"+bcolors.ENDC,
                    # Help message
                    help="Y/N/U - Yes/No/Unknown",
                    validators=(wiz.required_validator),
                    default='Y',
                ),
            )
        )

    def main_wizard_l2_a(self):
        """
        The Main Wizard
        """
        self.wiz_main_l2_a = wiz.PromptWizard(
            name=bcolors.OKBLUE+"Do you Need ML - Data Creation"+bcolors.ENDC,
            description="",
            steps=(
                # The list of input prompts to ask the user.
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="data_creativity",
                    # Display name
                    name=bcolors.HEADER+"Will a system be able to gather a lot of data by trying sequences of actions in many different situations and seeing the results"+bcolors.ENDC,
                    # Help message
                    help="Y/N/U - Yes/No/Unknown",
                    validators=(wiz.required_validator),
                    default='Y',
                ),
            )
        )
    
    def main_wizard_l2_b(self):
        """
        The Main Wizard
        """
        self.wiz_main_l2_b = wiz.PromptWizard(
            name=bcolors.OKBLUE+"Do you Need ML - Data Programmability"+bcolors.ENDC,
            description="",
            steps=(
                # The list of input prompts to ask the user.
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="data_programmability",
                    # Display name
                    name=bcolors.HEADER+"Can a program or set of rules decide what actions to take based on the data you have about the situations"+bcolors.ENDC,
                    # Help message
                    help="Y/N/U - Yes/No/Unknown",
                    validators=(wiz.required_validator),
                    default='Y',
                ),
            )
        )


    def main_wizard_l3(self):
        """
        The Main Wizard
        """
        self.wiz_main_l3 = wiz.PromptWizard(
            name=bcolors.OKBLUE+"Do you Need ML - Data Knowledge"+bcolors.ENDC,
            description="",
            steps=(
                # The list of input prompts to ask the user.
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="data_knowledge",
                    # Display name
                    name=bcolors.HEADER+"Could a knowledgeable human decide what actions to take based on the data you have about the situations"+bcolors.ENDC,
                    # Help message
                    help="Y/N/U - Yes/No/Unknown",
                    validators=(wiz.required_validator),
                    default='Y',
                ),
            )
        )

    def main_wizard_l4(self):
        """
        The Main Wizard
        """
        self.wiz_main_l4 = wiz.PromptWizard(
            name=bcolors.OKBLUE+"Do you Need ML - Data Pattern"+bcolors.ENDC,
            description="",
            steps=(
                # The list of input prompts to ask the user.
                wiz.WizardStep(
                    # ID where the value will be stored
                    id="data_pattern",
                    # Display name
                    name=bcolors.HEADER+"Could there be patterns in these situations that the humans haven't recognized before"+bcolors.ENDC,
                    # Help message
                    help="Y/N/U - Yes/No/Unknown",
                    validators=(wiz.required_validator),
                    default='Y'
                ),
            )
        )

    def supervized_wizard(self):
        """
        The Supervized Learning Wizard
        """

    def unsupervized_wizard(self):
        """
        The Un-Supervized Learning Wizard
        """

    def reinforced_wizard(self):
        """
        The Reinforced Learning Wizard
        """

    ############### All the Run Operations ######################
    def run_mainwiz(self):
        """
        Run the Main Wizard
        """
        self.main_wizard_l1()
        self.main_l1_values = self.wiz_main_l1.run(self.shell)
        if self.main_l1_values['data_availability'].lower() == 'y':
            self.main_wizard_l2_b()
            self.main_l2b_values = self.wiz_main_l2_b.run(self.shell)
            if self.main_l2b_values['data_programmability'].lower() == 'y':
                print(bcolors.FAIL+"ML is not required - Please consider alternate approaches\n"+bcolors.ENDC)
            else:
                self.main_wizard_l3()
                self.main_l3_values = self.wiz_main_l3.run(self.shell)
                if self.main_l3_values['data_knowledge'].lower() == 'y':
                        print(bcolors.OKGREEN+"Looks like you need ML, let's continue"+bcolors.ENDC)
                else:
                    self.main_wizard_l3()
                    self.main_l3_values = self.wiz_main_l3.run(self.shell)
                    if self.main_l3_values['data_pattern'].lower() == 'y':
                        print(bcolors.OKGREEN+"Looks like you need ML, let's continue"+bcolors.ENDC)
                    else:
                        print(bcolors.FAIL+"ML is not required - Please consider alternate approaches\n"+bcolors.ENDC)
        else:
            self.main_wizard_l2_a()
            self.main_l2a_values = self.wiz_main_l2_a.run(self.shell)
            if self.main_l2a_values['data_creativity'].lower() == 'y':
                print(bcolors.OKGREEN+"Looks like you need ML, let's continue"+bcolors.ENDC)
            else:
                print(bcolors.FAIL+"ML is not required - Please consider alternate approaches\n"+bcolors.ENDC)
        
    def run_learningtype_wizard(self):
        """
        Depending on the Main wizard values, run specific
        learning wizard
        """

    def run_supwiz(self):
        """
        Run Supervized learning Wizard.
        """

    def run_unsupwiz(self):
        """
        Run UnSupervized Learning Wizard.
        """

    def run_reinforcedwiz(self):
        """
        Run Reinforced Learning Wizard
        """

def signal_handler(signum, frame):
    """
    Signal Handler
    """
    print("\n You interrupted, No Suggestion will be provided!")
    print(signum, frame)
    sys.exit(0)

def main():
    """
    The Main Function
    """
    try:
        algowiz = AlgoSelectorWizard()
        algowiz.run_mainwiz()
    #    algowiz.run_learningtype_wizard()
    except(KeyboardInterrupt, MemoryError):
        print("Some Error Occured - No Suggestion can be provided")

    print("Thanks for using the Algoselector-Wizard, " +
            "Hope our suggestion will be useful")

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    main()
