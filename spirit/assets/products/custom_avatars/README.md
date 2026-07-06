# Custom Avatar Pieces

Place your custom avatar PNG textures in this directory.

### Specifications
* **Aspect Ratio:** `1:1` (Square) or matching corresponding master texture slots.
* **File Format:** PNG (Transparency must be used to preserve transparency on overlays and clothing details).
* **Recommended Resolutions:**
  * Hair, clothing, hats: `512x512` or `1024x1024` pixels.
  * Eyes, mouth, eyebrows: `256x256` pixels.

### Naming Conventions & Categorization
The server automatically determines the **Gender** and **Customization Group** of your asset based on its **prefix** and **suffix**.

#### 1. Gender Prefix (Required)
* **`f_`**: Female-specific customization pieces (e.g., `f_braids_hair.png`).
* **`m_`**: Male-specific customization pieces (e.g., `m_spiky_hair.png`).

#### 2. Group/Category Suffix (Required)
Add one of the following exact suffixes to assign your asset to the correct customization tab:

| Suffix | Group ID | Category | Examples |
| :--- | :---: | :--- | :--- |
| `_eyes` | `0` | Eyes | `m_blue_eyes.png`, `f_green_eyes.png` |
| `_eyebrows` | `1` | Eyebrows | `m_thick_eyebrows.png`, `f_thin_eyebrows.png` |
| `_face` | `2` | Face / Cheek markings | `f_freckles_face.png` |
| `_facial_hair` | `5` | Beards / Mustaches (Male only) | `m_goatee_facial_hair.png` |
| `_hair` | `6` | Hair / Hairstyles | `m_short_hair.png`, `f_long_hair.png` |
| `_hat` | `7` | Hats / Caps / Beanies | `m_red_cap_hat.png`, `f_sunhat_hat.png` |
| `_jacket` | `8` | Jackets / Outerwear | `m_leather_jacket.png`, `f_hoodie_jacket.png` |
| `_trousers` | `9` | Pants / Shorts / Skirts | `m_jeans_trousers.png`, `f_skirt_trousers.png` |
| `_mouth` | `10` | Mouth / Lip colors | `f_red_lipstick_mouth.png` |
| `_nose` | `11` | Nose shapes | `m_pointy_nose.png` |
| `_shirt` | `12` | Shirts / Underwear / Tops | `m_tshirt_shirt.png`, `f_tanktop_shirt.png` |
| `_shoes` | `13` | Shoes / Boots / Sneakers | `m_sneakers_shoes.png`, `f_heels_shoes.png` |
| `_shape` | `14` | Body Base Mesh | `m_base_shape.png`, `f_base_shape.png` |
| `_skin_color` | `15` | Procedural Skin Tones | *(See Skin Tone section below)* |

---

### Special: Procedural Skin Tones (Group 15)
The client parses skin colors procedurally. To register a custom skin choice that actually tints your avatar's 3D mesh (instead of rendering pitch-black or grey), use the `'x'` separator in the filename followed by a standard **6-digit Hex color code**:

* **Format:** `dummy_skin_colorx_<hex_color_code>_skin_color.png`
* **Examples:**
  * Light skin: `dummy_skin_colorx_ffe0bd_skin_color.png`
  * Tan skin: `dummy_skin_colorx_d4a373_skin_color.png`
  * Dark skin: `dummy_skin_colorx_8d5524_skin_color.png`

*Note: The compilation tool will automatically process, register, and bundle your textures into the main `en_US_avatar` bundle cache on server startup.*
