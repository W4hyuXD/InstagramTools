#! usr/bin/python3
#! Copyright by WahyuXD


import instaloader, os

def username():
    print('\n\n\nInstagram Profile Downloader')
    print('=============================')
    # input
    profile = input('\n[•] Enter Username: ')
    print('\n\n')
    # convert
    ig = instaloader.Instaloader()
    dl = ig.download_profile(profile,profile_pic_only=True)
    # print
    print('\n[✓] Download Success!')
    print('[•] Photos Saved In Folder: {}'.format(profile))
    print("============================")

if __name__=='__main__':
    try:
        os.system('git pull')
    except:pass
    username()