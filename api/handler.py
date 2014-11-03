import os
import subprocess


class H2WorldServiceHandler(object):
    def query(self, sql):
        """
        Executes the SQL query against the database and returns the results.
        """
        env = os.environ
        cmd = 'java -cp %s/bin/h2-%s.jar org.h2.tools.Shell -url jdbc:h2:%s/world' % (
            env['H2_HOME'], env['H2_VERSION'], env['H2_DATA'])
        return subprocess.check_output(cmd.split() + ['-sql', sql])

    def cityLanguage(self, city):
        """
        Looks up the most-spoken language in the given city based on its country
        along with the percentage of residents that speak it.
        """
        # TODO(orlade): Handle case of city in multiple countries.
        sql = '''SELECT language, percentage FROM countrylanguage WHERE
            countrycode = (SELECT countrycode FROM city WHERE name = '%s')
            ORDER BY percentage DESC LIMIT 1;''' % city
        # No need to protect against SQL injection, since the DB is transient.

        result = self.query(sql)
        values = map(lambda s: s.strip(), result.splitlines()[1].split('|'))
        return '{0} ({1}%)'.format(*values)
