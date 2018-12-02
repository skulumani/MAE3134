all: HW0 HW1 HW2 HW3 HW4 HW5 HW6

HW0: ./homework/HW0/Hw0.tex
	latexmk -pdf -jobname=./homework/HW0/Hw0 ./homework/HW0/Hw0.tex

HW1: ./homework/HW1/Hw1.tex
	latexmk -pdf -jobname=./homework/HW1/Hw1 ./homework/HW1/Hw1.tex

HW2: ./homework/HW2/HW2.tex
	latexmk -pdf -jobname=./homework/HW2/HW2 ./homework/HW2/HW2.tex

HW3: ./homework/HW3/HW3.tex
	latexmk -pdf -jobname=./homework/HW3/HW3 ./homework/HW3/HW3.tex

HW4: ./homework/HW4/hw4.tex
	latexmk -pdf -jobname=./homework/HW4/hw4 ./homework/HW4/hw4.tex

HW5: ./homework/HW5/hw5.tex
	latexmk -pdf -jobname=./homework/HW5/hw5 ./homework/HW5/hw5.tex

HW6: ./homework/hw6/hw6.tex
	latexmk -pdf -jobname=./homework/hw6/hw6 ./homework/hw6/hw6.tex

clean:
	latexmk -c -jobname=./homework/HW0/Hw0
	latexmk -c -jobname=./homework/HW1/Hw1
	latexmk -c -jobname=./homework/HW2/HW2
	latexmk -c -jobname=./homework/HW3/HW3
	latexmk -c -jobname=./homework/HW4/hw4
	latexmk -c -jobname=./homework/HW5/hw5
	latexmk -c -jobname=./homework/hw6/hw6
