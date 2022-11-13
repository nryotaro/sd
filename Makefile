.PHONY: clean

main.pdf: build/airbnb/leetcode.eps \
          build/amazon/leetcode.eps \
          build/googlemaps/leetcode.eps \
          build/facebook/leetcode.eps \
          build/netflix/leetcode.eps \
          build/notification/leetcode.eps \
          build/twitter/leetcode.eps \
          build/uber/leetcode.eps \
          main.bib \
          main.tex
	latexmk -gg -pdflua main.tex

clean:
	rm -rf build
	latexmk -C
	rm -f *.bbl *.run.xml *~
	rm -rf systems/venv

build/airbnb/leetcode.eps: systems/venv/bin/activate systems/systems/airbnb/leetcode.py
	$(call draw_diagram,airbnb/leetcode)

build/facebook/leetcode.eps: systems/venv/bin/activate systems/systems/facebook/leetcode.py
	$(call generate_diagram,facebook/leetcode)

build/googlemaps/leetcode.eps: systems/venv/bin/activate systems/systems/googlemaps/leetcode.py
	$(call generate_diagram,googlemaps/leetcode)

build/amazon/leetcode.eps: systems/venv/bin/activate systems/systems/amazon/leetcode.py
	$(call generate_diagram,amazon/leetcode)

build/netflix/leetcode.eps: systems/venv/bin/activate systems/systems/netflix/leetcode.py
	$(call draw_diagram,netflix/leetcode)

build/notification/leetcode.eps: systems/venv/bin/activate systems/systems/notification/leetcode.py
	$(call draw_diagram,notification/leetcode)

build/twitter/leetcode.eps: systems/venv/bin/activate systems/systems/twitter/leetcode.py
	$(call draw_diagram,twitter/leetcode)

build/uber/leetcode.eps: systems/venv/bin/activate systems/systems/uber/leetcode.py
	$(call draw_diagram,uber/leetcode)

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

define draw_diagram
	mkdir -p $(shell dirname build/$1)
	. systems/venv/bin/activate && \
	python systems/systems/$1.py build/$1.svg
	inkscape build/$1.svg -o build/$1.eps
endef
