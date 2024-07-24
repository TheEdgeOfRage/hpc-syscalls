# makefile
# pavle, 2019-05-12 18:11
#

.phony: all latex biber clean

all: latex biber

biber: seminarski.tex
	biber seminarski

latex: seminarski.tex
	xelatex -shell-escape -halt-on-error -interaction=nonstopmode seminarski.tex

clean:
	rm -f *.aux *.lof *.log *.lot *.toc *.bbl *.blg *-blx.bib *.run.xml *.bcf *.out *.pdf *.acn *.acr *.alg *.fdb_latexmk *.fls *.glg *.glo *.gls *.ist
