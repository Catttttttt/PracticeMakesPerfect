SELECT a.username, a.email, COUNT(ai.item_id) AS items, SUM(i.weight) AS total_weight
FROM accounts a JOIN accounts_items ai on a.id = ai.account_id JOIN items i ON ai.item_id = i.id
GROUP BY a.id
HAVING SUM(i.weight) > 20
ORDER BY total_weight DESC, username ASC;
