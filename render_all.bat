@echo off

set quality=LOW_QUALITY

:: 1080p60
if "%quality%"=="HIGH_QUALITY" (
    python manim.py episodes\ep1\hook.py ComplexNumbersTitle --high_quality
    python manim.py episodes\ep1\hook.py ApplicationsOfComplexNumbers --high_quality
    python manim.py episodes\ep1\hook.py EEApplication --high_quality
    python manim.py episodes\ep1\hook.py ComplexQuantitiesPaper --high_quality
    python manim.py episodes\ep1\hook.py PoleZeroPlot --high_quality
    python manim.py episodes\ep1\hook.py CompareToClassroom --high_quality
    python manim.py episodes\ep1\hook.py NoPrerequisites --high_quality

    python manim.py episodes\ep1\circuits_scenes.py IntroduceCircuit --high_quality
    python manim.py episodes\ep1\circuits_scenes.py CircuitDefinition --high_quality
    python manim.py episodes\ep1\circuits_scenes.py CompsDisplay --high_quality
    python manim.py episodes\ep1\circuits_scenes.py ComplexCircuitOverview --high_quality
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