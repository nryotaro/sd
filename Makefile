main.pdf: build/googlemaps/leetcode.eps build/amazon/leetcode.eps
	latexmk -gg -pdflua main.tex

clean:
	rm -rf build
	latexmk -C
	rm -f *.bbl *.run.xml *~
	rm -rf systems/venv

build/googlemaps/leetcode.eps: systems/venv/bin/activate
	@$(call generate_diagram,googlemaps/leetcode)

build/amazon/leetcode.eps: systems/venv/bin/activate
	@$(call generate_diagram,amazon/leetcode)

systems/venv/bin/activate:
	python -m venv systems/venv
	. systems/venv/bin/activate
	pip install -e systems[dev]

define generate_diagram
	. systems/venv/bin/activate
	mkdir -p build
	python systems/systems/$1.py build/$1
	inkscape build/$1.svg -o build/$1.eps
endef
