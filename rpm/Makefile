NAME=nagios-plugins-ethz
VERSION=`cat VERSION`
DIST_DIR=$(NAME)-$(VERSION)
DIST_FILES=AUTHORS COPYING ChangeLog Makefile NEWS README TODO VERSION $(NAME).spec

dist:
	rm -rf $(DIST_DIR) $(DIST_DIR).tar.gz
	mkdir $(DIST_DIR)
	cp $(DIST_FILES) $(DIST_DIR)
	tar cfz $(DIST_DIR).tar.gz $(DIST_DIR)

clean:
	rm -f *~
