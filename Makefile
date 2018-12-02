all: HW0 HW1 HW2 HW3 HW4 HW5 HW6 HW7 HW8 HW9 bode midterm final

HW0: ./homework/HW0/Hw0.tex
	latexmk -pdf -cd ./homework/HW0/Hw0.tex

HW1: ./homework/HW1/Hw1.tex
	latexmk -pdf -cd ./homework/HW1/Hw1.tex

HW2: ./homework/HW2/HW2.tex
	latexmk -pdf -cd ./homework/HW2/HW2.tex

HW3: ./homework/HW3/HW3.tex
	# cd homework/HW3
	latexmk -pdf -cd ./homework/HW3/HW3.tex

HW4: ./homework/HW4/hw4.tex
	latexmk -pdf -cd ./homework/HW4/hw4.tex

HW5: ./homework/HW5/hw5.tex
	latexmk -pdf -cd ./homework/HW5/hw5.tex

HW6: ./homework/hw6/hw6.tex
	latexmk -pdf -cd ./homework/hw6/hw6.tex

HW7: ./homework/HW7/hw7.tex
	latexmk -pdf -cd ./homework/HW7/hw7.tex

HW8: ./homework/hw7/hw7.tex
	latexmk -pdf -cd ./homework/hw7/hw7.tex

HW9: ./homework/hw9/hw9.tex
	latexmk -pdf -cd ./homework/hw9/hw9.tex

bode: ./bode_plot/bode_plot.tex
	latexmk -pdf -cd ./bode_plot/bode_plot.tex

midterm: ./exams/midterm/midterm.tex
	latexmk -pdf -cd ./exams/midterm/midterm.tex

final: ./exams/final/final.tex
	latexmk -pdf -cd ./exams/final/final.tex

clean:
	latexmk -c -cd ./homework/HW0/Hw0
	latexmk -c -cd ./homework/HW1/Hw1
	latexmk -c -cd ./homework/HW2/HW2
	latexmk -c -cd ./homework/HW3/HW3
	latexmk -c -cd ./homework/HW4/hw4
	latexmk -c -cd ./homework/HW5/hw5
	latexmk -c -cd ./homework/hw6/hw6
	latexmk -c -cd ./homework/HW7/hw7
	latexmk -c -cd ./homework/hw7/hw7
	latexmk -c -cd ./homework/hw9/hw9
	latexmk -c -cd ./exams/midterm/midterm
	latexmk -c -cd ./exams/final/final
	latexmk -c -cd ./bode_plot/bode_plot
