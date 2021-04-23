import sys
import getopt
import os

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
            "ComplexCircuitOverview",
            "CircuitSummary"
        ],
    # "current_scenes.py":
    #     [
    #         "IntroCurrentPart",
    #         "IntroduceACDC",
    #         "IntroCharge",
    #         "ElementaryCharge",
    #         "SimpleCircuit",
    #         "Amperes",
    #         "BackToSimpleCircuit"
    #     ],
    # "current_scenes_new.py":
    #         [
    #             "IntroCurrentPart",
    #             "IntroduceACDC",
    #             "SimpleCircuit",
    #             "ACvsDC"
    #         ],
    "current_scenes_final.py":
        [
            "IntroCurrentPart",
            "CurrentOverview"
        ],
    "ohms_law_final.py":
        [
            "IntroOhmsLawPart",
            "OhmsLawIntro",
            "CurrentCalculation",
            "CircuitsTable"
        ],
    "phasors.py":
        [
            "IntroPhasorsPart",
            "ImaginaryVoltageCircuit",
            "ACvsDC",
            "ACDCApplications",
            "SineWaveCharacteristics",
            "EulersFormulaIntro",
            "VideoRecommendEulerIdentity",
            "EulersFormula"
        ]
    # "ohms_law.py":
    #     [
    #         "IntroOhmsLawPart",
    #         "OhmsLawIntro",
    #         "CurrentCalculation",
    #         "VoltageResistanceQuestion",
    #         "HydraulicCircuitOverview",
    #         "HaganPouiseuilleOhmsLaw"
    #     ]
}

for file, scenes in scenes_map.items():
    for scene in scenes:
        print("executing: custom_render.py " + scene + " --no_delete")
        os.system("custom_render.py " + scene + " --no_delete")