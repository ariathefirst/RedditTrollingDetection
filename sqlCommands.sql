// formatted query
SELECT
  name,
  body,
  parent_id,
  id,
  subreddit_id
FROM
  [fh-bigquery:reddit_comments.all]
WHERE
  author = 'Rohirric_Spear'

// unformatted 
SELECT body, name, score FROM [fh-bigquery:reddit_comments.2018_01] WHERE author = 'RavarSC' LIMIT 1000
