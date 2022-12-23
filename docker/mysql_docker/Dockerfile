FROM mysql

#RUN /bin/bash -c "/usr/bin/mysqld_safe &" &&\
#	sleep 5 &&\
#	mysql -u root -e "CREATE DATABASE sppmdb" &&\
#	mysql -u root sppmdb < dump.sql

ADD init_db.sh /tmp/init_db.sh
#ADD dump.sql /tmp/dump.sql
#RUN ["chmod", "+x", "/tmp/dump.sql"]
RUN ["chmod", "+x", "/tmp/init_db.sh"]
RUN /tmp/init_db.sh
