# Custom landing-page artwork

Add a 16:9 PNG here to make it available in **Admin Dashboard → Dynamic
Pages → Browse game artwork**. A 1920×1080 source is recommended.

Spirit uses the PNG filename as the Unity asset name, normalizes it to lowercase,
and adds `_landingpage` when needed. For example:

```text
summer-event.png  →  LandingPage/summer_event_landingpage
```

The server compiles every PNG in this folder into
`bundleCache/en_US_LandingPage_Custom` at startup. The dashboard's **Rescan
bundles** button performs the same check, and **Add custom artwork** uploads a
file here and rebuilds the bundle immediately.

Images that are not exactly 16:9 are center-cropped. The compiler then packs the
visible image into the original game's 2048×2048 LandingPage texture layout, so
the browser preview and Unity client use the same crop.

The first build needs one original `en_US_LandingPage_*` bundle as a template.
Place an original cache under `original_game_cache`, configure `PTCGO_CACHE_DIR`,
or install game artwork through the dashboard first.
