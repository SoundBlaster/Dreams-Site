# Foundation validation — 2026-10-25

Scope: static content/structure for the upcoming tvOS app; final design deferred.

- `python3 scripts/check-site.py`: passes for3 EN/RU pages, titles, viewport tags,
  and all local page/asset links.
- `node --check website/dreams/language.js`: exits0.
- Ruby Psych YAML parse: both GitHub workflow files parse successfully.
- Local HTTP preview on127.0.0.1:8795: the root, EN/RU landing/support/privacy
  queries, CSS and JS each return200 with nonempty bodies (9 requests).
- `git diff --check`: passes.
- The adapted FTPS workflow preserves TLS/hostname checks and has only a manual
  deployment trigger, restricted tomain. Root is guarded to/www/egormerkushev.ru/dreams.
  Password is read throughLFTP_PASSWORD/--env-password, not process arguments;
  see [the lftp manual](https://lftp.yar.ru/lftp-man.html).
- Existing Apache-2.0 repository license is preserved; the adapted7of10 MIT
  workflow has its original license and source identity in third-party notices.

Browser verification was unavailable: the local CUA session reported no iab
browser and returned an empty browser inventory. No rendered layout, responsive
screenshots, screen-reader interaction or JS language-switch behavior is claimed
as observed. HTTP/source checks do not establish those behaviors.

No hosting credentials were read/copied, no hosting account/Site was created,
no production workflow was run, and no App Store metadata was modified. Planned
production URLs remain drafts until publication and HTTP/content verification.
The local preview server is stopped at task teardown. Final design and actual
hosting/email policy review remain the next steps.
