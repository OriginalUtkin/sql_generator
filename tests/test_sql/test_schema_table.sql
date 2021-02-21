CREATE TABLE "process" (
  "process_id" int PRIMARY KEY,
  "booking_id" int DEFAULT 10,
  "state" process_state DEFAULT "verification" NOT NULL,
  "created_at" timestamp DEFAULT (now()),
  "updated_at" timestamp,
);
