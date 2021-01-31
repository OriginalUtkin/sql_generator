ALTER TABLE "issue"
    ADD FOREIGN KEY ("process_id")
    REFERENCES "process" ("process_id");
