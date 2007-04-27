PLUGIN=nagios-plugins-various
FILES=check_afsspace  check_bos  check_cpu.pl  check_mailq  check_mem  check_rxdebug  check_udebug
VERSION=1.0
DIST_DIR=$(PLUGIN)-$(VERSION)
DIST_FILES=$(PLUGIN).spec ${FILES} Makefile

dist:
	rm -rf $(DIST_DIR) $(DIST_DIR).tar.gz
	mkdir $(DIST_DIR)
	cp $(DIST_FILES) $(DIST_DIR)
	tar cfz $(DIST_DIR).tar.gz $(DIST_DIR)

install:
	mkdir -p $(DESTDIR)
	install -m 755 $(FILES) $(DESTDIR)

clean:
	rm -f *~
