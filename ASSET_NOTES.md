# Photo assets

The displayed portrait is the **unaltered original photo** in `assets/fd4eb84492676633e52dae3667c98f34.png`. A CSS clipping polygon isolates the person. His identity, facial features, clothes, and original photo pixels are preserved. No generated portrait is used.

The twelve campaign images use CSS crops of the original artwork PNGs. Only their square creative images are displayed. Their outer frames, icons, hanging captions, and drop shadows are native HTML/CSS, and all portfolio headings and body/caption text are editable HTML.

`assets/studio-background.png` is a cleaned reconstruction of the studio background from `assets/74012fa0ca7113588fbf0c6433798057.png`. It was edited with the built-in image-generation tool to remove lettering and yellow panels. Obscured room details were reconstructed, so it is not a pixel-identical original background. The final accepted prompt was:

> Use case: precise-object-edit
> Asset type: native HTML/CSS portfolio background photograph
> Input image: the supplied image is the edit target.
> Primary request: clean the photograph by removing every Arabic and English text overlay at the top and all four large solid yellow rectangular panels. Fill these removed overlays with the continuation of the original purple-lit bedroom/studio underneath.
> Constraints: preserve identical 16:9 framing, camera position, perspective, original dark purple lighting and exposure, wall and shelf geometry, books, plant, framed posters, laptop at lower left, bedding, blinds on the left, wardrobe on the right, and visible room detail. Use the visible source as the faithful basis for obscured areas. This is cleanup of the existing photograph, not a redesigned or newly staged scene. No person, new objects, yellow panels, graphic overlays, headings, or captions. Preserve typography physically present within original posters or books as scene detail.

Original source artwork and all twenty original videos remain in `assets/`. No media depends on Canva's servers at runtime.
