import sys
import getopt
import os

scenes_dir = "episodes/ep1/"
scenes_map = {
    "hook.py":
        [
            "ComplexNumbersTitle",
            "ApplicationsOfComplexNumbers",
            "EEApplication",
            "ComplexQuantitiesPaper",
            "PoleZeroPlot",
            "CompareToClassroom",
            "NoPrerequisites"
        ],
    "circuits_scenes.py":
        [
            "WhatIsCircuit",
            "IntroduceCircuit",
            "CircuitDefinition",
            "CompsDisplay",
            "ComplexCircuitOverview"
        ],
    "current_scenes.py":
        [
            "IntroCurrentPart",
            "IntroduceACDC",
            "IntroCharge",
            "ElementaryCharge",
            "SimpleCircuit",
            "Amperes",
            "BackToSimpleCircuit"
        ],
    "ohms_law.py":
        [
            "IntroOhmsLawPart",
            "OhmsLawIntro",
            "CurrentCalculation"
        ]
}

def get_commands(quality_arg, quality_ending):
    commands = []
    for file, scenes in scenes_map.items():
        for scene in scenes:
            commands += ["python manim.py " + scenes_dir + file + " " + scene + " " + quality_arg + " -o " + scene
                         + quality_ending]
    return commands

def main(argv):
    # get quality selection from input arguments
    quality = "HIGH"
    try:
        opts, args = getopt.getopt(argv, "hq:", ["quality="])
    except getopt.GetoptError:
        print('render_all.py -q <QUALITY>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('render_all.py -q <QUALITY>')
            sys.exit()
        elif opt in ("-q", "--quality"):
            quality = arg.upper()
    if quality not in ("LOW", "HIGH"):
        print("invalid quality " + quality)
        sys.exit(2)

    quality_arg = "--high_quality"
    if quality == "LOW":
        quality_arg = "-l"

    quality_ending = "1080"
    if quality == "LOW":
        quality_ending = "480"

    for command in get_commands(quality_arg, quality_ending):
        print("executing: " + command)
        os.system(command)


if __name__ == "__main__":
    main(sys.argv[1:])
