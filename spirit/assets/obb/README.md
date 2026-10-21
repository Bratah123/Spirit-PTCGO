# Android OBB

This folder is intentionally empty. **Server developers have to provide their own .OBB file** (Can be found in the APK download of the client)

The Android client checks `{assetURL}obb/<name>` on every launch. If the size or MD5 differs from its local
OBB, it downloads the file from this server
