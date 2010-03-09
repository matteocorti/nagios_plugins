PLUGIN=nagios-plugins-various
FILES=check_cpu.pl check_mailq check_mem check_dhcp.pl check_open_files.pl
VERSION=1.5
DIST_DIR=$(PLUGIN)-$(VERSION)
DIST_FILES=$(PLUGIN).spec ${FILES} Makefile

dist:
	rm -rf $(DIST_DIR) $(DIST_DIR).tar.gz
	mkdir $(DIST_DIR)
	cp $(DIST_FILES) $(DIST_DIR)
	tar cfz $(DIST_DIR).tar.gz $(DIST_DIR)

install:
	mkdir -p  $(RPM_BUILD_ROOT)/usr/lib/nagios/plugins/contrib/
	install -m 755 $(FILES)  $(RPM_BUILD_ROOT)/usr/lib/nagios/plugins/contrib/

clean:
	rm -f *~
