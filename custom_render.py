import os
import sys
import random
import string

scenes_dir = "episodes/ep1/"
output_dir = "media/videos/"
quality_arg = "-l"
quality_ending = "480p15"
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


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


# find file containing scene, and render
scene_to_render = sys.argv[2]
selected_file = None
rand_string = get_random_string(5)
for file, scenes in scenes_map.items():
    if scene_to_render in scenes:
        selected_file = file
        cmd = "python manim.py " + scenes_dir + file + " " + scene_to_render + " " + quality_arg + " -o " + \
              scene_to_render + quality_ending + "_" + rand_string + " -p"
        print("executing: " + cmd)
        os.system(cmd)
        break

if selected_file is None:
    raise Exception("selected scene " + scene_to_render + " not found in " + scenes_dir)

# delete old scene file
video_dir = output_dir + selected_file.replace(".py", "") + "/" + quality_ending
for filename in os.listdir(video_dir):
    if filename.startswith(scene_to_render) and (rand_string not in filename):
        cmd = "del /f " + (video_dir + "/" + filename).replace("/", "\\")
        print("executing " + cmd)
        os.system(cmd)
