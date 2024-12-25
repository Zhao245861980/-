import os
import sys
import random

import django

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0, BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "swiper.settings")
django.setup()

from user.models import User

last_names = (
    '赵钱孙李周吴郑王冯陈褚维蒋沈韩杨'
    '朱秦尤许何吕施张孔曹严华金魏陶江'
    '戚谢邹喻柏水窦章云苏潘葛奚范彭郎'
    '鲁韦昌马苗凤花方俞任袁柳酆鲍史唐'
    '费廉岑薛雷贺倪汤滕殷罗毕郝邬安常'
    '乐于时傅皮卞齐康伍余元卜顾孟平黄'
)

first_names = {
    '男': [
        '致远', '骏驰', '雨泽', '华磊', '晟睿',
        '天佑', '文昊', '修洁', '黎析', '远航',
        '旭尧', '鸿涛', '伟奇', '荣轩', '越泽',
        '浩宇', '瑾瑜', '皓轩', '浦泽', '绍辉',
        '邵琪', '升荣', '圣杰', '晟睿', '思聪',
    ],
    '女': [
        '佩玲', '欣妍', '佳琪', '雅芙', '雨婷',
        '韵寒', '丽兹', '美西', '宁馨', '秒娑',
        '心琪', '飞鸢', '诗情', '露结', '静思',
        '雅兴', '灵韵', '清寒', '容月', '索菲',
        '雨佳', '雅思', '梦德', '梦海', '慧荣',
    ],
}


# 创建初始用户
def random_name():
    last_name = random.choice(last_names)
    sex = random.choice(list(first_names.keys()))
    first_name = random.choice(first_names[sex])
    return ''.join([last_name, first_name]), sex


for i in range(1000):
    try:
        name, sex = random_name()
        User.objects.create(
            phonenum='%s' % random.randrange(21000000000, 21900000000),
            nickname=name,
            sex=sex,
            birth_year=random.randint(1980, 2000),
            birth_month=random.randint(1, 12),
            birth_day=random.randint(1, 28),
            location=random.choice(['北京', '上海', '深圳', '成都', '西安', '沈阳', '武汉']),
        )
        print('created: %s %s' % (name, sex))
    except django.db.utils.IntegrityError:
        pass
