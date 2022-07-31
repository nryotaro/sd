

main.pdf: diagrams/googlemaps/leetcode.eps
	latexmk -gg -pdflua main.tex

clean:
	rm diagrams/googlemaps/*.eps
	rm diagrams/googlemaps/*.svg
	latexmk -C
	rm *.bbl *.run.xml *~
	rm -rf diagrams/venv

diagrams/googlemaps/leetcode.eps: diagrams/venv/bin/activate
	@$(call generate_diagram,googlemaps/leetcode)

diagrams/venv/bin/activate:
	python -m venv diagrams/venv
	. diagrams/venv/bin/activate
	pip install diagrams

define generate_diagram
	. diagrams/venv/bin/activate
	python diagrams/$1.py diagrams/$1
	inkscape diagrams/$1.svg -o diagrams/$1.eps
endef
