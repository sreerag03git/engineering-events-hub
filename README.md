# HELM — Engineering Student Events Command Deck

Live site: hackathons, competitions, fests, conferences & awards for engineering students (all fields), through June 2028. Past events auto-hide; deadlines count down live.

## How auto-update works
- `index.html` has a baked-in seed list of events.
- `events_feed.json` (`{ "updated":"YYYY-MM-DD", "events":[ ...event objects... ] }`) holds events found AFTER the seed. The page fetches it on load and merges any event whose `id` isn't already present.
- A weekly scheduled Claude hunt re-searches the web for newly announced competitions, appends them to `events_feed.json`, and commits. The live site shows them automatically.

## Event schema (append to events_feed.json -> events[])
id, name, org, type(hackathon|competition|conference|fest|award), region(india|gcc|europe|americas|asia|global), flag, country, city, start(YYYY-MM-DD|null), end, dateText, year(2026|2027|2028), free(bool), field(software|robotics|mechanical|aerospace|civil|electrical|chemical|marine|cyber|any), what, desc, fee, url, deadlines[{t,d?,txt}], est:true, tier?, defence?, rolling?.
Rules: only events a student can enter/present/compete in (no visitor-only trade shows); dates today -> June 2028; dedupe by id; projected dates est:true; bump updated.
