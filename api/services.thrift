/**
 * The API for querying the H2 World database.
 */

service H2WorldService {

  /**
   * Executes the SQL query against the database and returns the results.
   */
  string query(1:string sql)

  /**
   * Looks up the most-spoken language in the given city based on its country,
   * along with the percentage of residents that speak it.
   */
  string cityLanguage(1:string city)

}
