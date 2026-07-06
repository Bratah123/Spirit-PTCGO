# Custom Avatar Thumbnails

Place your custom avatar thumbnail PNG textures in this directory.

### Specifications
* **Recommended Resolution:** **`128x128`** pixels (standard thumbnail size for PTCGO customizer list items).
* **Aspect Ratio:** `1:1` (Square).
* **File Format:** PNG (Transparency should be used to make the background mesh-neutral).
* **Naming:** Use lowercase letters, numbers, and underscores, matching your corresponding main piece filename but ending with the exact **`_thumb`** suffix.

### Mapping Suffix
To link a thumbnail image to your custom avatar piece, name the thumbnail exactly the same as the main piece, but append `_thumb` to the end of the filename.

* **Main Piece:** `m_leather_jacket.png`
* **Corresponding Thumbnail:** `m_leather_jacket_thumb.png`

*Note: The compilation tool will automatically process and bundle your custom thumbnails into the main `en_US_avatar_thumbs` bundle cache on server startup.*
