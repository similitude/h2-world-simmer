import os
from hamcrest.core.assert_that import assert_that
from api.handler import H2WorldServiceHandler


def test_query_system():
    """
    Performs a full system test, invoking a local instance of the H2 database.

    Set environment variable CI=true in continuous integration to skip.
    """
    # Do not run system tests for continuous integration.
    if os.environ.get('CI'):  # pragma: no cover
        return

    result = H2WorldServiceHandler().query('SELECT * FROM country')
    assert_that()