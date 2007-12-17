PLUGIN=nagios-plugins-various
FILES=check_afsspace  check_bos  check_cpu.pl  check_mailq  check_mem  check_rxdebug  check_udebug check_dhcp.pl
VERSION=1.2
DIST_DIR=$(PLUGIN)-$(VERSION)
DIST_FILES=$(PLUGIN).spec ${FILES} Makefile check_procs.f8 check_procs.rh4

dist:
	rm -rf $(DIST_DIR) $(DIST_DIR).tar.gz
	mkdir $(DIST_DIR)
	cp $(DIST_FILES) $(DIST_DIR)
	tar cfz $(DIST_DIR).tar.gz $(DIST_DIR)

install:
	mkdir -p  $(RPM_BUILD_ROOT)/usr/lib/nagios/plugins/contrib/
	install -m 755 $(FILES)  $(RPM_BUILD_ROOT)/usr/lib/nagios/plugins/contrib/
	install -m 755 check_procs  $(RPM_BUILD_ROOT)/usr/lib/nagios/plugins/contrib/

clean:
	rm -f *~
