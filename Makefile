.PHONY: clean draw

system :=


main.pdf: build/googlemaps/leetcode.eps \
          build/amazon/leetcode.eps \
          build/facebook/leetcode.eps \
	  build/airbnb/leetcode.eps
	latexmk -gg -pdflua main.tex

clean:
	rm -rf build
	latexmk -C
	rm -f *.bbl *.run.xml *~
	rm -rf systems/venv

draw: systems/venv/bin/activate
	$(call generate_diagram,$(system))

build/airbnb/leetcode.eps: systems/venv/bin/activate
	$(call generate_diagram,airbnb/leetcode)

build/facebook/leetcode.eps: systems/venv/bin/activate
	$(call generate_diagram,facebook/leetcode)

build/googlemaps/leetcode.eps: systems/venv/bin/activate
	$(call generate_diagram,googlemaps/leetcode)

build/amazon/leetcode.eps: systems/venv/bin/activate
	$(call generate_diagram,amazon/leetcode)

systems/venv/bin/activate:
	python -m venv systems/venv
	. systems/venv/bin/activate && \
	pip install --upgrade pip && \
	pip install -e systems[dev]

define generate_diagram
	mkdir -p build
	. systems/venv/bin/activate && \
	python systems/systems/$1.py build/$1
	inkscape build/$1.svg -o build/$1.eps
endef
