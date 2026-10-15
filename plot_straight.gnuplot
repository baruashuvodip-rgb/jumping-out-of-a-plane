set term pdfcairo color enhanced font "Times-New-Roman,14" size 5,3
set output "fall_without_parachute_plot.pdf"
set xlabel "{/Times-New-Roman-Italic Time (seconds)}"
set ylabel "{/Times-New-Roman-Italic Position (meters)}"
plot "para_jump_straight_output.txt" using 1:2 notitle with lines lw 2
unset output