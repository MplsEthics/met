
usage:
	@echo "make [clean|talk]"

clean:
	rm -f talk.html
	rm -rf ui/

talk: talk.rst
	rst2s5.py talk.rst talk.html

