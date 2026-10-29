# Dreams-Site

Static website for Dreams for Apple TV. Intended production base:
`https://egormerkushev.ru/dreams/`.

## Current state

The landing page presents the tvOS app with footage and screenshots captured
from Dreams. The App Store release is still in preparation.
The App Store version is not published. Changes under `website/dreams/` on
`main` trigger deployment automatically; a manual trigger is also available.
Pages and policies are drafts until checked and published; do not set App Store
URLs to these addresses before their public content has been verified.

- `website/dreams/index.html` — upcoming Apple TV app overview.
- `website/dreams/support/index.html` — public support contact and basic help.
- `website/dreams/privacy/index.html` — tvOS app, support email and website policy.
- `app-store/privacy/` — EN/RU app policy text for Apple TV Privacy Policy.
- `.github/workflows/deploy-website.yml` — FTPS deployment, adapted from `7of10`.

EN/RU content lives in semantic sections. `?lang=en` / `?lang=ru` select the
language; otherwise the browser language is used. No cookies, browser storage,
analytics, remote fonts or third-party scripts are included. With JavaScript off,
both language sections remain available. Initial styling uses system fonts.

## Local preview and checks

No dependencies, package installation or build step:

```sh
python3 -m http.server 8795 --bind 127.0.0.1 --directory website
python3 scripts/check-site.py
node --check website/dreams/language.js
```

Open `http://127.0.0.1:8795/dreams/?lang=en` or `?lang=ru`.
The structural check validates page titles, language content and internal asset/
page links. Browser checks and hosting verification remain separate evidence.

## Deployment, when requested

The structure follows `~/Development/GitHub/7of10`: static files under a product
subdirectory and FTPS to existing hosting. No Sites hosting registration or new
hosting account is used. GitHub Actions deploys changes on `main` and can also
be started manually.

Configure an environment named `FTP` in this repository:

| Kind | Name | Value |
| --- | --- | --- |
| Variable | `FTP_HOST` | `server209.hosting.reg.ru` (verify against current hosting) |
| Variable | `FTP_PORT` | `21` |
| Variable | `FTP_USER` | Hosting username |
| Variable | `FTP_REMOTE_ROOT` | `/www/egormerkushev.ru/dreams` |
| Secret | `FTP_PASSWORD` | Hosting password |

Secrets do not transfer automatically from `7of10`. Do not copy them into source.
The workflow verifies TLS certificates/hostnames, forces encrypted transfer,
creates only the intended product directory, uploads without deletion, and checks
all published files against the source commit over HTTPS. It never targets the
7of10 directory. The reference hosting certificate setup must be verified when
first deploying. Run the workflow only after content/design approval.

## Store preparation

Planned URLs (not yet published):

- Marketing: `https://egormerkushev.ru/dreams/`
- Support: `https://egormerkushev.ru/dreams/support/`
- Privacy: `https://egormerkushev.ru/dreams/privacy/`

App Store Connect: Dreams TV, app `6826786729`, tvOS only. Use
`app-store/privacy/en-US.txt` / `ru.txt` for the platform's Apple TV Privacy Policy
text after reviewing the wording. Apple Standard EULA is linked from the footer;
no custom EULA is authored. Public support contact: Egor Merkushev,
`egor.merkushev@yandex.ru`. The separately provided App Review telephone is not
published in this repository. EU trader disclosure is a separate ASC setting.

App behavior baseline: [Dreams tvOS source `5936633`](https://github.com/SoundBlaster/Dreams/tree/5936633762c5a380c7af11b7f3162d46504e4f0a/tvOS).
The policy is scoped to the TV app; macOS agent integrations are excluded. The
hosting policy must be checked against actual logging/retention practices before
publication. Support-email handling is distinguished from collection by the app.

## Next stages

1. Final site design and app screenshots, replacing this minimal layout.
2. Review public support/privacy copy and actual hosting/email practices.
3. Configure FTP environment and manually publish/verify production files.
4. Set working URLs and approved policy text in App Store Connect; complete
   EN/RU store metadata and screenshots.

The existing Apache-2.0 `LICENSE` is retained; see third-party notices for the
adapted MIT deployment workflow. Site licensing does not replace the app's EULA.
