# Сэвлэг үргээх: knowledge center for agents

**In short:** This folder holds everything made for one family's first-haircut ceremony (үсний найр / сэвлэг үргээх ёслол) in Mongolia. Read this file first. It says who the user is, the facts about the event, the rules for new work, where each file is, and how to rebuild the printouts. Raw research is in `knowledge/`.

Last updated: 2026-10-13.

---

## 1. The user and the event

- The user is **Mongolian**, the **father**, and not a native English speaker.
- He is hosting his **son's** first-haircut ceremony **at home in Mongolia** for **about 50 guests**.
- He is the **MC (хөтлөгч, host of the program)** himself.
- He asked for this because "Mongolians don't have an exact rulebook" for the ceremony. He wants facts from many sources, not one opinion.
- **Still unknown (as of 2026-10-13):**
  - the date;
  - the start time (a lama will give it);
  - the son's хий нас (traditional age: 1 at birth, +1 at each Lunar New Year);
  - who the first cutter is (usually a person born in the child's ивээл жил, the "friendly" zodiac years);
  - whether a hired ерөөлч (blessing reciter) or морин хуурч (horse-head fiddle player) will come.
  The printouts leave blank lines for these.

## 2. Rules for any agent working here

### Talking to the user
- Write chat replies in **plain, simple English**: short sentences, everyday words, no idioms.
- Explain each technical term in a few words the first time you use it.
- If a reply is long, start with a 2–3 line "in short" summary.

### Anything printed or shown to family and guests
- Write it **fully in Mongolian Cyrillic**. This covers run sheets, tickets, cards, helper sheets and guest pages.
- Do not use English instructions with Mongolian quotes. The user once said: *"i thought i was said it in mongolian?"*

### Spell-check every Mongolian text before you send it
Use the user's own tool, **monspell**:

```sh
# Check the visible text of an HTML file; prints only the misspelled words.
sed -e 's/<[^>]*>/ /g' FILE.html | grep -E "[А-Яа-яӨөҮү]" \
  | ~/.cargo/bin/monspell -l --dict-dir ~/projects/monspell-upstreams/dict-mn/mn_MN
# Second dictionary (FST speller) if needed:
#   --fst ~/projects/monspell-upstreams/spellers/khk.bhfst
```

- **Known false alarm:** monspell flags the separate word "руу" / "рүү" ("to, towards") as wrong, but "лүү" passes. These words are correct, so ignore the flag. The user said to skip reporting this bug for now.
- Fixes already made after monspell: Бууршгүй, Сааршгүй, Үйлд уран, Хуульд шударга.

### Gender
- The child is a **boy**. Boy rules apply:
  - the first cut is on the **right temple**;
  - boys' ages are **odd**, counted in хий нас (3 or 5);
  - use "хүү", "хүүгийнхээ".
- The ticket file can also print a girl version (see section 4).

### Working style
- The user likes **readable print sizes**. He rejected a 1-page timetable because the text was too small (about 7pt). Keep body text at 10pt or larger.
- **Do not run `rm` with shell variables.** It was blocked. Write to a new file name instead.
- **The repo is public:** https://github.com/abadrangui/sevleg (branch `main`). Anything you commit and push, anyone can read. Do not add phone numbers, addresses, guest names or the son's name unless the user asks.
- `knowledge/raw/facebook/` holds notes from public Facebook posts, including post links. The user chose to publish them as they are (2026-10-13).
- **Facebook rules for browser agents:** read-only by default. The user later allowed joining a few public groups, if the agent goes slowly and politely so the account is not blocked. The agent used a limit of 5 one-click public groups at most. It joined none, and there were no warnings.

## 3. Map of the repo

| Path | What it is |
|---|---|
| `reports/Mongolian first haircut ceremony.md` | **Main guide (English, ~15k words, 97 cited sources).** It covers the plan, the order of the day, timing, the first cutter, taboos, food, drinks, clothes, gifts, blessings, costs, regional versions, conflicts between sources, and questions for elders. **Start here for any ceremony fact.** |
| `research_notes/Mongolian first haircut ceremony/*.md` | Notes from 5 research agents, with a source link on every claim (164 unique sources). Files: `core_ritual_meaning_timing`, `regional_ethnic_variations`, `food_and_table`, `clothes_gifts_blessings_planning`, `facebook_community`. |
| `knowledge/README.md` | Index of the raw material, with a source URL for each file. |
| `knowledge/raw/facebook/facebook-posts.md` | Raw notes from about 25 posts in the public group "Сэвлэг үргээх ёсон" (~101k members). Has real menus, guest counts and prices in ₮ (tögrög) from 2025–2026, plus the lama-vs-big-party debate. |
| `knowledge/raw/facebook/facebook-blessings.md` | Raw blessing (ерөөл) texts found on Facebook, with links. |
| `knowledge/raw/blessing-texts/*.txt` | Clean Mongolian blessing verses used for the tickets (code list in `knowledge/README.md`). |
| `knowledge/raw/web-pages/*.txt` | Plain-text copies of Mongolian, English and Chinese web pages used in the research. |
| `knowledge/raw/papers/*.txt` | Text of 3 academic papers (2025). |
| `knowledge/raw/print-text/*.txt` | The visible text of the tickets and the Mongolian run sheet, for quick reading or search. |
| `knowledge/artifacts/*.html` | Source files of the 3 web pages published on claude.ai (section 5). |
| `print/` | Printable files: HTML source plus the finished PDFs (section 4). |
| `print/assets/` | The official Roblox logo (2022) and Robux coin (2019 gold) SVGs, from Wikimedia Commons. |
| `tools/h2t.py` | Small script that turns saved HTML pages into plain text: `python3 -I tools/h2t.py page.html` writes `page.html.txt`. |

## 4. Printables

All are A4. HTML is the source; the PDF is what gets printed.

| File | What it is | Notes |
|---|---|---|
| `print/run-sheet-mn.html` → `run-sheet-mn.pdf` | **The MC run sheet, in Mongolian. 4 pages.** | p1: setup (people, items, rules), with blank lines for date, хий нас and lama's time. p2–3: a compact timetable with 3 columns (time / what happens / "Таны хэлэх үг" = what you say). p4: the cutting order. |
| `print/run-sheet-mn-3page-backup.html` | Older, longer layout of the same run sheet | Kept as a backup. |
| `print/run-sheet-en.html` → `.pdf` | English version of the run sheet | For reference only. The family uses the Mongolian one. |
| `print/yerool-tickets.html` → `ereel-tasalbar-boy.pdf`, `ereel-tasalbar-girl.pdf` | **20 blessing tickets** (10 per page, cut apart) for guests who did not prepare a blessing. Page 3 has a card for the first cutter and a card for the elder. | Tickets 1–13 are traditional texts. Tickets 14–20 were newly written. Gender comes from the URL ending: `#boy` (default) or `#girl`. |
| `print/robux-card.html` → `robux-card.pdf` | **Gift card for the son (age 5): 800 Robux.** Official ROBLOX logo, Robux coin, 8 coins each marked "100", and "8 × 100 = 800". | One A4 sheet folded in half. The back half is upside down on purpose. The back has "Яаж авах вэ?" (3 steps), "Хэнд / Хэнээс" lines, a "Код" box for the real code, and a note for adults: redeem at roblox.com/redeem. The user asked to remove the "$10" label: **show only 800 Robux, never a dollar price.** Official logos are fine because this is one card for his own son. |
| `print/robux-card-generic.html` → `.pdf` | The same card without official logos | Older version. |

### Timetable in the run sheet (example times; it assumes a 10:00 start)

| Time | Step |
|---|---|
| 07:00 | Morning prep: fresh цагаалга (milk rice with curd and raisins) and food, set the table, charge the clippers, put tickets by the door |
| 08:30 | Purify the scissors over juniper (арц) or incense (хүж); tie a blue хадаг (silk scarf) to the handle |
| 09:00 | Brief the helpers; dress the boy in his deel (traditional robe) |
| 09:30 | Guests arrive; elders sit at the хоймор (the honour seat at the back) |
| 10:00 | Opening speech; first airag (fermented mare's milk) to the eldest guest |
| 10:15 | First cut: wooden knife touch, then scissors at the **right temple**; the boy tastes milk |
| 10:25 | Family cuts (grandparents, parents, aunts and uncles) |
| 10:40 | Guests cut, going sunwise (clockwise), ~40 sec each (~35 min for 40 people) |
| 11:15 | Long closing blessing; the ritual ends before noon |
| 11:30 | Feast: цагаалга first, then food; airag, **no vodka** |
| 12:30 | Songs, photos, games |
| 13:00 | Optional full shave; **all** hair goes into the хадаг |
| 13:30 | Thank-you gifts (special gift for the first cutter); closing words |
| 14:00 | Guests leave; fold the хадаг with the hair and keep it in a chest forever |

**If the lama gives another start time,** move every row by the same amount. Keep the ritual part before noon.

### How to rebuild a PDF

```sh
cd print
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu \
  --no-pdf-header-footer --virtual-time-budget=8000 --allow-file-access-from-files \
  --print-to-pdf="$PWD/run-sheet-mn.pdf" "file://$PWD/run-sheet-mn.html"
# Girl tickets: use "file://$PWD/yerool-tickets.html#girl" and --print-to-pdf=".../ereel-tasalbar-girl.pdf"
# Preview pages as PNG to check the layout:
pdftoppm -r 70 -png run-sheet-mn.pdf /tmp/preview
```

Check the page count after each change (`pdfinfo FILE.pdf | grep Pages`). The run sheet must stay at 4 pages and the tickets at 3.

## 5. Published web pages (private, on claude.ai)

| Page | URL | Source file |
|---|---|---|
| Facebook findings (English): "Сэвлэг Field Notes" | https://claude.ai/artifact/4hE4c2vw4Yrotrv6yRBBtu | `knowledge/artifacts/facebook-findings-en.html` |
| Facebook findings (Mongolian): "Ээжүүдийн үсний найрын туршлага" | https://claude.ai/artifact/46BBjdMJgqswVdBLmro14D | `knowledge/artifacts/facebook-findings-mn.html` |
| Guest blessing guide (Mongolian): "Даахинд хэлэх ерөөл" | https://claude.ai/artifact/W6tBw6pibj7T4p9YKB51e1 | `knowledge/artifacts/blessing-guide-mn.html` |

To change a published page, read it first with the Artifact tool (`action: "read"`, the URL), then publish to the same URL. The copies here may be older than the live pages.

## 6. Ceremony facts in brief (details and sources in the report)

These are the points most sources agree on. Where they differ, the report has a "Where sources disagree" section with a 3-step rule for choosing.

- **Core rite.** On a good morning, a respected person makes the first cut with scissors tied with a хадаг. The child tastes milk. Then every guest cuts a small lock, says a blessing (ерөөл) and gives a gift. The hair is **kept for life**, never thrown away. In one Facebook thread, 7 of 9 parents kept all of it, even the shaved rest, in the pouch. One said "if a strand ends up in a bird's nest, that is very bad".
- **Who cuts first (Khalkh).** The grandfather, the father, or the oldest respected guest. Many families today choose a person born in the child's ивээл жил.
- **Age.** Boys at an odd хий нас (3 or 5); girls at an even one (2 or 4). Sources conflict a little on this.
- **Day.** Ask a lama. In general: the waxing moon (lunar days 1–15), Monday or Friday, before noon. Avoid Thursday ("хүний хишиг өдөр").
- **Order of cuts for a boy.** Right temple, then left temple, then the crown. Guests go sunwise, elders first.
- **Food.** **Цагаалга** is the one dish every source requires; guests taste it first. A biscuit plate (тавгийн идээ), if used, has an odd number of layers; 3 is common at home (about 60k₮ for the boov). Ууц (sheep's back) and бууз/хуушуур (dumplings) are a family choice; families disagree.
- **Drinks.** Airag is welcome. **No vodka or hard liquor.**
- **Return gifts.** A thank-you gift for each person who cut the hair, often milk or dairy food plus a small gift; something special for the first cutter. Small gifts for visiting children.
- **Home costs from 2025–2026 Facebook posts.** About 1.5M–4.8M₮ at home (one post: 1.5M₮ for 25 people; another: 3.85M₮ for 35 people). Ерөөлч plus fiddler: 250k–300k₮. Catering a buffet for 50 people: about 1.75M₮. Many hosts say guests eat less than you think. One host planned for 50 and 35 came.
- **Practical tips from parents.**
  - Hire a separate photographer; the host is too busy to take photos.
  - Slice fruit small.
  - Get a reliable helper to serve.
  - Let the child hear the clippers buzz before the day.
  - Order the deel early.

## 7. History of requests (2026-10-11 to 2026-10-13)

1. **Deep research** from many groups and sources, including **Facebook groups** through the user's logged-in Chrome. Result: the report, the research notes, and the Facebook pages.
2. **"How many total?"** and **blessing count.** He wanted 12–20 printed blessing tickets for guests who did not prepare one. Result: 20 tickets.
3. **Spell-check with monspell.** It found 4 fixes (section 2).
4. **Hour-by-hour guide** for the father as MC. The first version had English instructions. He wanted it **in Mongolian**, so it was rebuilt fully in Mongolian.
5. **Compress the timetable** from 3 pages to 2 (or 1). The 1-page version was too small to read, so it is **2 pages**.
6. **Roblox gift card** worth "$10" that a 5-year-old understands. Then: use the **official** Roblox logo and coin icon. Then: **remove the $10, keep only 800 Robux.**
7. **Commit everything**, write this knowledge file for other agents, and push to the public GitHub repo. Asked if raw Facebook notes and copied articles should be public, the user said: push all.

## 8. Likely next tasks

- When the date, lama's time, хий нас and first cutter are known: fill them into `print/run-sheet-mn.html` and the tickets' page 3, shift the times, rebuild the PDFs and run monspell.
- A guest list or a cutting-order list with real names.
- An invitation (in Mongolian).
- A shopping list and budget for ~50 guests at home. The report has a sample budget under "A sample budget for about 50 guests at home".
- A thank-you message for guests after the day.
