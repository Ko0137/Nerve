import os
class ProfileManager:
    def __init__(self):
        os.makedirs('nerve_app/config', exist_ok=True)
    def list_profiles(self): return []
