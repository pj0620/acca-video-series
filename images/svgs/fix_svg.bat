set svg_file=%1%
set temp_file="temp.svg"

cairosvg %svg_file% -f svg -o %temp_file%
move %temp_file% %svg_file%