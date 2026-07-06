import unittest
import os
import shutil
import tempfile
import urllib.request
import urllib.error
import socket
import hashlib
from spirit.server.http_server import AssetHTTPServer, ASSET_PATHS

class TestHTTPAssetRouting(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 1. Create a temporary directory for assets
        cls.temp_dir = tempfile.mkdtemp()
        
        # Create a mock physical card bundle folder
        cls.bundle_folder = os.path.join(cls.temp_dir, "en_US_SWSH12")
        os.makedirs(cls.bundle_folder, exist_ok=True)
        
        cls.data_file = os.path.join(cls.bundle_folder, "__data")
        with open(cls.data_file, "wb") as f:
            f.write(b"MOCK-SWSH12-ASSET-DATA with CAB-698f1293cb9396443b3f13ebe0cec855 inside")

        # Create another custom set bundle folder
        cls.custom_folder = os.path.join(cls.temp_dir, "en_US_CUSTOM")
        os.makedirs(cls.custom_folder, exist_ok=True)
        cls.custom_data_file = os.path.join(cls.custom_folder, "__data")
        with open(cls.custom_data_file, "wb") as f:
            f.write(b"MOCK-CUSTOM-ASSET-DATA with CAB-698f1293cb9396443b3f13ebe0cec855 inside")

        # 2. Add temporary path to global ASSET_PATHS
        ASSET_PATHS.insert(0, cls.temp_dir)

        # 3. Start HTTPServer on a free local port
        # Find a free port dynamically
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('127.0.0.1', 0))
        cls.port = s.getsockname()[1]
        s.close()

        cls.server = AssetHTTPServer(host='127.0.0.1', port=cls.port)
        cls.server.start()

    @classmethod
    def tearDownClass(cls):
        # Stop the server
        cls.server.stop()
        
        # Remove from ASSET_PATHS
        if cls.temp_dir in ASSET_PATHS:
            ASSET_PATHS.remove(cls.temp_dir)

        # Clean up files
        shutil.rmtree(cls.temp_dir, ignore_errors=True)

    def test_routing_physical_bundle_direct(self):
        # Direct physical request (should NOT have CAB replaced since it's not a virtual split)
        url = f"http://127.0.0.1:{self.port}/en_US/en_US_SWSH12_1.unity3d"
        try:
            with urllib.request.urlopen(url, timeout=5) as response:
                self.assertEqual(response.status, 200)
                data = response.read()
                self.assertEqual(data, b"MOCK-SWSH12-ASSET-DATA with CAB-698f1293cb9396443b3f13ebe0cec855 inside")
        except urllib.error.URLError as e:
            self.fail(f"Failed to fetch asset: {e}")

    def test_routing_virtual_type_split_water(self):
        # Virtual type-split request for water (should have CAB replaced dynamically)
        url = f"http://127.0.0.1:{self.port}/en_US/en_US_SWSH12_water_1.unity3d"
        try:
            with urllib.request.urlopen(url, timeout=5) as response:
                self.assertEqual(response.status, 200)
                data = response.read()
                
                # Compute expected virtual CAB name
                h = hashlib.md5(b"SWSH12_water").hexdigest()
                expected_cab = f"CAB-{h}".encode('utf-8')
                
                self.assertIn(expected_cab, data)
                self.assertNotIn(b"CAB-698f1293cb9396443b3f13ebe0cec855", data)
        except urllib.error.URLError as e:
            self.fail(f"Failed to fetch asset: {e}")

    def test_routing_virtual_type_split_colorless(self):
        # Virtual type-split request for colorless (should have CAB replaced dynamically)
        url = f"http://127.0.0.1:{self.port}/en_US/en_US_CUSTOM_colorless_1.unity3d"
        try:
            with urllib.request.urlopen(url, timeout=5) as response:
                self.assertEqual(response.status, 200)
                data = response.read()
                
                # Compute expected virtual CAB name
                h = hashlib.md5(b"CUSTOM_colorless").hexdigest()
                expected_cab = f"CAB-{h}".encode('utf-8')
                
                self.assertIn(expected_cab, data)
                self.assertNotIn(b"CAB-698f1293cb9396443b3f13ebe0cec855", data)
        except urllib.error.URLError as e:
            self.fail(f"Failed to fetch asset: {e}")

    def test_routing_non_existent_404(self):
        # Check that unrelated non-existent assets still 404
        url = f"http://127.0.0.1:{self.port}/en_US/en_US_NONEXISTENT_1.unity3d"
        with self.assertRaises(urllib.error.HTTPError) as cm:
            urllib.request.urlopen(url, timeout=5)
        self.assertEqual(cm.exception.code, 404)

    def test_messaging_manifest_has_messaging_array(self):
        # null 'messaging' NREs ServerManifestDataRetriever on the Tournament scene
        import json
        url = f"http://127.0.0.1:{self.port}/patch/messaging/manifest.json?x=1"
        with urllib.request.urlopen(url, timeout=5) as response:
            self.assertEqual(response.status, 200)
            body = json.loads(response.read())
        self.assertIsInstance(body.get("messaging"), list)
        # the generic patcher manifest must still answer its own route
        url = f"http://127.0.0.1:{self.port}/patch/manifest.json"
        with urllib.request.urlopen(url, timeout=5) as response:
            body = json.loads(response.read())
        self.assertIn("LatestWindowsClientVersion", body)

if __name__ == '__main__':
    unittest.main()
