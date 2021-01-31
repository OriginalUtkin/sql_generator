CREATE TABLE "process" (
  "process_id" int PRIMARY KEY,
  "booking_id" int,
  "ticket_id" int,
  "created_at" timestamp DEFAULT (now()),
  "updated_at" timestamp
);
