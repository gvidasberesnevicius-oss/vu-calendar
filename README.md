# VU calendar timezone fix

Automatically fetches a VU `.ics` feed and tags floating `DTSTART`/`DTEND` event times with `Europe/Vilnius` so Outlook Mac does not shift events by 3 hours.

## Setup
1. Create a **public** GitHub repository and upload all files, preserving `.github/workflows/update.yml` and `update_calendar.py`.
2. Repository **Settings → Secrets and variables → Actions → Variables → New repository variable**: name `VU_ICS_URL`, value = your original VU `.ics` subscription URL.
3. Repository **Settings → Actions → General → Workflow permissions**: select **Read and write permissions** and save (if allowed).
4. Repository **Settings → Pages → Build and deployment → Source: Deploy from a branch**; branch `main`, folder `/docs`, Save. (If `/docs` is not offered, first run the workflow to generate `docs/calendar.ics`, then return.)
5. **Actions → Update VU calendar → Run workflow**. Check that it succeeds and `docs/calendar.ics` appears.
6. Subscribe to `https://YOUR-USERNAME.github.io/YOUR-REPO/calendar.ics` in Outlook Web via **Add calendar → Subscribe from web**.
7. Check events in Outlook Web and Mac, then hide/remove the old VU subscription and the temporary test import to avoid duplicates.

**Privacy:** GitHub Pages requires public access to the calendar file. Course times, names and locations will be publicly accessible. Do not use this approach if you need the schedule to remain private.

**Timing:** The workflow is scheduled every 6 hours (GitHub can delay scheduled workflows). Outlook refreshes subscribed calendars on its own schedule. Changes may therefore appear later.

**Note:** VU calendar links can change each semester. Update `VU_ICS_URL` for the new semester.
