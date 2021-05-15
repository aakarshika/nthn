CREATE TABLE IF NOT EXISTS "settlittapp_question" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "q_code" varchar(200) NULL, "q_description" text NULL, "q_total_votes" integer NOT NULL, "q_created_date" datetime NOT NULL, "q_updated_date" datetime NOT NULL, "q_pub_date" datetime NOT NULL, "q_created_by_id" integer NOT NULL REFERENCES "settlittapp_user" ("id") DEFERRABLE INITIALLY DEFERRED, "q_photo_id" integer NOT NULL REFERENCES "settlittapp_photo" ("id") DEFERRABLE INITIALLY DEFERRED, "q_updated_by_id" integer NOT NULL REFERENCES "settlittapp_user" ("id") DEFERRABLE INITIALLY DEFERRED, "q_text" varchar(200) NULL);
CREATE INDEX "settlittapp_question_q_created_by_id_287cf328" ON "settlittapp_question" ("q_created_by_id");