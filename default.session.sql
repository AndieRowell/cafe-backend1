-- DROP TABLE "alembic_version";

-- DROP TABLE "tokens";

-- DROP TABLE "users";

-- UPDATE users SET is_superuser = True
-- WHERE users.id = 1;

DELETE FROM collection_tracker_drinks
WHERE collection_tracker_drinks.id = 2;
