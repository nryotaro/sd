.PHONY: clean

main.pdf: main.bib \
          main.tex \
	  googlemaps.tex \
	  build/airbnb/leetcode.png \
          build/amazon/leetcode.png \
          build/googlemaps/leetcode.png \
          build/facebook/leetcode.png \
          build/netflix/leetcode.png \
          build/notification/leetcode.png \
          build/twitter/leetcode.png \
          build/uber/leetcode.png \
          build/whatsapp/leetcode.png \
          build/zoom.png \
          build/googlemaps.png
	latexmk -pdflua main.tex

clean:
	rm -rf build
	latexmk -C
	rm -f *.run.xml *~
	rm -rf systems/venv

build/airbnb/leetcode.png: systems/venv/bin/activate systems/systems/airbnb/leetcode.py
	$(call draw_diagram,airbnb/leetcode)

build/facebook/leetcode.png: systems/venv/bin/activate systems/systems/facebook/leetcode.py
	$(call generate_diagram,facebook/leetcode)

build/googlemaps/leetcode.png: systems/venv/bin/activate systems/systems/googlemaps/leetcode.py
	$(call generate_diagram,googlemaps/leetcode)

build/amazon/leetcode.png: systems/venv/bin/activate systems/systems/amazon/leetcode.py
	$(call generate_diagram,amazon/leetcode)

build/netflix/leetcode.png: systems/venv/bin/activate systems/systems/netflix/leetcode.py
	$(call draw_diagram,netflix/leetcode)

build/notification/leetcode.png: systems/venv/bin/activate systems/systems/notification/leetcode.py
	$(call draw_diagram,notification/leetcode)

build/twitter/leetcode.png: systems/venv/bin/activate systems/systems/twitter/leetcode.py
	$(call draw_diagram,twitter/leetcode)

build/uber/leetcode.png: systems/venv/bin/activate systems/systems/uber/leetcode.py
	$(call draw_diagram,uber/leetcode)

build/whatsapp/leetcode.png: systems/venv/bin/activate systems/systems/whatsapp/leetcode.py
	$(call draw_diagram,whatsapp/leetcode)
build/zoom.png: systems/venv/bin/activate systems/systems/zoom.py
	$(call draw_diagram,zoom)
build/googlemaps.png: systems/venv/bin/activate systems/systems/googlemaps.py
	$(call draw_diagram,googlemaps)

systems/venv/bin/activate:
	python -m venv systems/venv
	. systems/venv/bin/activate && \
	pip install --upgrade pip && \
	pip install -e systems[dev]

define generate_diagram
	mkdir -p build
	. systems/venv/bin/activate && \
	python systems/systems/$1.py build/$1
endef

define draw_diagram
	mkdir -p $(shell dirname build/$1)
	. systems/venv/bin/activate && \
	python systems/systems/$1.py build/$1.png
endef
