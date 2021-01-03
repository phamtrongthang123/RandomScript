import requests
import os
from PIL import Image
from io import BytesIO
from tqdm import tqdm


def get_and_filtering_chapter_list(cid, lang_filter='English', start_chapter=1, last_chapter=None):
    list_chapter_raw = requests.get(f'https://mangadex.org/api/?id={cid}&type=manga').json()['chapter']
    filtered_list_chapter = []
    for k,v in list_chapter_raw.items():
        if v['lang_name'] == lang_filter:
            chapter_order = float(v['chapter'])
            if last_chapter == None:
                if start_chapter > chapter_order:
                    continue
            else:
                if last_chapter < chapter_order or start_chapter > chapter_order:
                    continue
            filtered_list_chapter.append([k,v])
    return filtered_list_chapter

def start_download(root, filtered_list_chapter):
    missing_list = []
    for chaptid,v in tqdm(filtered_list_chapter, total=len(filtered_list_chapter)):
        try:
            title = v['title'].replace('?','')
            chapt_data = requests.get(f'https://mangadex.org/api/?id={chaptid}&server=null&saver=0&type=chapter').json()
            chapter_order = chapt_data['chapter']
            hash_code = chapt_data['hash']
            list_pages = chapt_data['page_array']
            server = chapt_data['server'] # example: https://mangadex.org/data/
            group_name = chapt_data['group_name'].replace('?','')
            try:
                os.mkdir(f'{root}/{group_name}_{chapter_order}_{chaptid}')
            except:
                pass

            im_list = []
            for page_name in list_pages:
                # no / between server and hash code
                img_raw_url = f'{server}{hash_code}/{page_name}'
                r = requests.get(img_raw_url, allow_redirects=True)
                filename = img_raw_url.split('/')[-1]
                save_path = f'{root}/{group_name}_{chapter_order}_{chaptid}/{filename}'
                open(save_path, 'wb').write(r.content)
                img = Image.open(BytesIO(r.content))
                img.load()
                img = img.convert('RGB')
                im_list.append(img)
            pdf_fn = f'{root}/Ch. {chapter_order}-{title}-{group_name}.pdf'
            im_list[0].save(pdf_fn, "PDF" ,resolution=100.0, save_all=True, append_images=im_list[1:])

        except:
            missing_list.append(float(v['chapter']))
    if len(missing_list) >0:
        print('missing those ', missing_list)