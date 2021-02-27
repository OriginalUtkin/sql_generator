ALTER TABLE "issue"
    ADD FOREIGN KEY ("process_id_test")
    REFERENCES "process" ("process_id");
