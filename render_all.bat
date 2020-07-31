@echo off

set quality=HIGH_QUALITY

:: 1080p60
if "%quality%"=="HIGH_QUALITY" (
    python manim.py episodes\ep1\hook.py ComplexNumbersTitle --high_quality -o ComplexNumbersTitle1080
    python manim.py episodes\ep1\hook.py ApplicationsOfComplexNumbers --high_quality -o ApplicationsOfComplexNumbers1080
    python manim.py episodes\ep1\hook.py EEApplication --high_quality -o EEApplication1080
    python manim.py episodes\ep1\hook.py ComplexQuantitiesPaper --high_quality -o ComplexQuantitiesPaper1080
    python manim.py episodes\ep1\hook.py PoleZeroPlot --high_quality -o PoleZeroPlot1080
    python manim.py episodes\ep1\hook.py CompareToClassroom --high_quality -o CompareToClassroom1080
    python manim.py episodes\ep1\hook.py NoPrerequisites --high_quality -o NoPrerequisites1080

    python manim.py episodes\ep1\circuits_scenes.py WhatIsCircuit --high_quality -o WhatIsCircuit1080
    python manim.py episodes\ep1\circuits_scenes.py IntroduceCircuit --high_quality -o IntroduceCircuit1080
    python manim.py episodes\ep1\circuits_scenes.py CircuitDefinition --high_quality -o CircuitDefinition1080
    python manim.py episodes\ep1\circuits_scenes.py CompsDisplay --high_quality -o CompsDisplay1080
    python manim.py episodes\ep1\circuits_scenes.py ComplexCircuitOverview --high_quality -o ComplexCircuitOverview1080

    python manim.py episodes\ep1\current_scenes.py IntroCurrentPart --high_quality -o IntroCurrentPart1080
    python manim.py episodes\ep1\current_scenes.py IntroduceACDC --high_quality -o IntroduceACDC1080
    python manim.py episodes\ep1\current_scenes.py IntroCharge --high_quality -o IntroCharge1080
    python manim.py episodes\ep1\current_scenes.py ElementaryCharge --high_quality -o ElementaryCharge1080
    python manim.py episodes\ep1\current_scenes.py SimpleCircuit --high_quality -o SimpleCircuit1080
    python manim.py episodes\ep1\current_scenes.py Amperes --high_quality -o Amperes1080
)

::480p15
if "%quality%"=="LOW_QUALITY" (
    python manim.py episodes\ep1\hook.py ComplexNumbersTitle -l
    python manim.py episodes\ep1\hook.py ApplicationsOfComplexNumbers -l
    python manim.py episodes\ep1\hook.py EEApplication -l
    python manim.py episodes\ep1\hook.py ComplexQuantitiesPaper -l
    python manim.py episodes\ep1\hook.py PoleZeroPlot -l
    python manim.py episodes\ep1\hook.py CompareToClassroom -l
    python manim.py episodes\ep1\hook.py NoPrerequisites -l

    python manim.py episodes\ep1\circuits_scenes.py IntroduceCircuit -l
    python manim.py episodes\ep1\circuits_scenes.py CircuitDefinition -l
    python manim.py episodes\ep1\circuits_scenes.py CompsDisplay -l
    python manim.py episodes\ep1\circuits_scenes.py ComplexCircuitOverview -l
)