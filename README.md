# Abdelnasser GM — Native HTML5 portfolio

![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)
[![Hosting: GitHub Pages](https://img.shields.io/badge/Hosting-GitHub%20Pages-222222?logo=github)](https://pages.github.com/)

The portfolio is now a native HTML5, CSS, and JavaScript website. All page headings, Arabic/English biography, skills, and social-post captions are real selectable text. Sections have natural content height; CSS Grid rearranges the video and social-post cards for phones and tablets. No full-page slides, Canva embed, or framework is used.

## Open

Open `index.html` directly, or run `npm start` and visit http://127.0.0.1:4173. No package installation is needed.

## Edit

- `index.html`: editable page content and semantic HTML sections.
- `styles.css`: yellow outlined typography, purple background, portrait clipping, paper cards, and responsive layouts.
- `script.js`: lazy muted video previews, accessible video dialog with native controls, and back-to-top.
- `assets/`: local original portrait/campaign images, videos, posters, fonts, and the cleaned studio background.

You can edit the HTML directly. Alternatively, edit `tools/build_native.py` and run `python tools/build.py` to regenerate it. Regeneration overwrites direct changes to `index.html`. The media mapping is in `tools/media.json`.

The portrait uses the exact original photo pixels, isolated using CSS clipping. Campaign images are individually cropped from the original artwork using CSS; their surrounding frames and captions are native elements. Text that is part of the campaign creative itself remains in its image, as with any portfolio showing graphic design work. See `ASSET_NOTES.md` for the background cleanup details.

## Layout and controls

- Desktop: four videos and four social cards per row.
- Tablet: two social cards per row.
- Phone: two videos per row, one social card per row, readable biography and skills.
- Select a video to play it with sound, seeking, and fullscreen controls.
- Escape closes the video dialog and returns focus.
- Reduced-motion preferences disable automatic previews.

## Hosting

### Publish to GitHub Pages

1. Create an empty **public** repository on GitHub, for example `portfolio`. Leave the options to add a README, license, and gitignore unchecked.
2. From this folder, run the following commands, replacing `YOUR_USERNAME` and `YOUR_REPOSITORY` with your actual values:

   ```powershell
   git add .
   git commit -m "Prepare portfolio for GitHub Pages"
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
   git push -u origin main
   ```

3. In the repository, open **Settings → Pages → Build and deployment → Source**, and select **GitHub Actions**.
4. Open **Actions → Deploy portfolio to GitHub Pages → Run workflow** and run it on `main`. If the initial push failed before Pages was enabled, rerun that workflow.
5. After deployment succeeds, the live URL appears in **Settings → Pages** and in the workflow deployment. For a repository called `portfolio`, the usual address is `https://YOUR_USERNAME.github.io/portfolio/`.

Every subsequent push to `main` validates and deploys the site automatically. Pull requests run validation without publishing. The workflow uploads only the website files and `assets/`; no Node server is needed on GitHub Pages. Relative asset URLs support both repository sites and account sites.

To add a live deployment-status badge, replace the two placeholders in this snippet and paste it near the top of this README:

```markdown
[![Deploy portfolio to GitHub Pages](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY/actions/workflows/pages.yml/badge.svg)](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY/actions/workflows/pages.yml)
```

GitHub Pages setup reference: [Using custom workflows with GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).

### Validate locally

```powershell
npm run check
python tools/check.py --static
```

For the additional local video seeking check, start `npm start` in another terminal and run `python tools/check.py` without `--static`.

You can also upload `index.html`, `styles.css`, `script.js`, and the full `assets/` directory to another static web host. `server.js` is an optional local preview server with video range-request support.

Source design: https://abdelnassergmportfolio.my.canva.site/
