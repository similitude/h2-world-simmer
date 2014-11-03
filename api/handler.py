import os
import subprocess


class H2WorldServiceHandler(object):
    def query(self, sql):
        """
        Executes the SQL query against the database and returns the results.
        """
        cmd = 'java -cp %s/bin/h2*.jar org.h2.tools.Shell -url jdbc:h2:%s ' \
              '-sql "%s"' % (os.environ['H2_HOME'], os.environ['H2_DATA'], sql)
        return subprocess.call(cmd)

    def city_language(self, city):
        """
        Looks up the most-spoken language in the given city based on its country
        along with the percentage of residents that speak it.
        """
        sql = '''SELECT language, percentage FROM countrylanguage WHERE
            countrycode = (SELECT countrycode FROM city WHERE name = '%s')
            ORDER BY percentage DESC LIMIT 1;''' % city
        # No need to protect against SQL injection, since the DB is transient.
        result = self.query(sql)
        return '%s (%s)' % result.splitlines()[1].split('\s+|\s+')