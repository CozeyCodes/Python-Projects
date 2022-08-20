import instaloader

ig = instaloader.Instaloader()
dp = input("Username ->>> ")

ig.download_profile(dp, profile_pic_only=True)
