[app]
title = NerveApp
package.name = nerveapp
package.domain = org.nerve
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,txt
version = 1.0.0
requirements = python3,kivy,asyncio,attrs,charset-normalizer,multidict,yarl,frozenlist,idna,aiosignal
orientation = portrait
fullscreen = 0
android.permissions = INTERNET

android.api = 33
android.minapi = 24
android.ndk = 25b
android.sdk_build_tools_version = 33.0.0
android.accept_sdk_license = True
env.AIOHTTP_NO_EXTENSIONS = 1
