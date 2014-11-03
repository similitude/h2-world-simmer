"""
Tests for the H2 World database service.

Note: To load the World database content, download world.sql from
https://raw.githubusercontent.com/similitude/h2-world-docker/master/world.sql
and run:

java -cp $H2_HOME/bin/h2-*.jar org.h2.tools.RunScript \
    -url jdbc:h2:$H2_DATA/world -script /path/to/world.sql
"""
import os
from hamcrest.core.assert_that import assert_that
from hamcrest.core.core.isequal import equal_to
from api.handler import H2WorldServiceHandler


def test_query_system():
    """
    Performs a full system test, invoking a local instance of the H2 database.

    Set environment variable CI=true in continuous integration to skip.
    """
    if os.environ.get('CI'):
        return

    result = H2WorldServiceHandler().query('SELECT * FROM country')
    assert_that(len(result.splitlines()), equal_to(241))


def test_cityLanguage_system():
    """
    Performs a full system test, invoking a local instance of the H2 database.

    Set environment variable CI=true in continuous integration to skip.
    """
    if os.environ.get('CI'):
        return

    result = H2WorldServiceHandler().cityLanguage('Melbourne')
    assert_that(result, equal_to('English (81.2%)'))

    result = H2WorldServiceHandler().cityLanguage('Kandy')
    assert_that(result, equal_to('Singali (60.3%)'))
