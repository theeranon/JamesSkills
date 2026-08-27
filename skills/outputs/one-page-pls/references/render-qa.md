# Render And Fit QA

Run these checks on every topic file, not only the first artifact.

## Render target

- A4 landscape, `297mm x 210mm`
- one PDF page or one viewport-height HTML page
- print background enabled
- IBM Plex Sans Thai loaded before capture or PDF export

Use an available browser renderer such as Playwright, Chromium, or Chrome. Wait for `document.fonts.ready` before measuring or capturing.

## Machine checks

In the rendered page, verify:

```javascript
const page = document.querySelector('.page');
const style = getComputedStyle(document.body);
({
  widthFits: page.scrollWidth <= page.clientWidth,
  heightFits: page.scrollHeight <= page.clientHeight,
  viewportWidthFits: document.documentElement.scrollWidth <= document.documentElement.clientWidth,
  viewportHeightFits: document.documentElement.scrollHeight <= document.documentElement.clientHeight,
  fontDeclared: style.fontFamily.includes('IBM Plex Sans Thai'),
  fontLoaded: document.fonts.check('16px "IBM Plex Sans Thai"'),
  unresolvedTokens: /\[\[|\]\]|TODO|PLACEHOLDER/.test(document.body.innerText)
});
```

Required result: all four fit checks and both font checks are true; `unresolvedTokens` is false. A requested PDF must contain exactly one page.

## Visual checks

- Inspect the complete rendered page at readable size.
- Thai marks, tables, dates, and source notes are not clipped or overlapped.
- The page has a clear reading order and no unnecessary scrolling.
- Body copy remains at least `9pt`; source notes remain at least `8pt`.
- Rectangular radius is at most `6px`; circles are reserved for genuinely circular marks.
- Metadata stays plain text. Pills and chips appear only for a real interactive control, which a static one-page artifact normally does not need.
- No colored left rail, decorative gradient, ripple, rainbow sections, ornamental cards, or separate Latin typeface.
- No conversation residue, AI instructions, production notes, copied requirements, or client data from another job.

## Semantic checks

Compare the rendered artifact with the source inventory:

- exactly one topic appears in the file
- every material decision, action, risk, and evidence item is present or explicitly linked
- owners, numbers, and dates still match the source
- inferred content is labeled rather than presented as fact

Any failed check blocks delivery for that file without blocking work on the other topic files.
