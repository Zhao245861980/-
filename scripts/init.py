#！/usr/bin/env python

import os
import sys
import random

import django

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0, BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "swiper.settings")
django.setup()

from user.models import User
from vip.models import Vip, Permission, VipPermRelation

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


def create_robots(n):
    # 创建初始用户
    for i in range(n):
        name, sex = random_name()
        try:
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


def init_permission():
    """创建权限模型"""
    permission_names = [
        'vipflag',         # 会员身份标识
        'superlike',       # 超级喜欢
        'rewind',          # 反悔功能
        'anylocation',     # 任意更改定位
        'unlimit_like',    # 无限喜欢次数
    ]

    for name in permission_names:
        perm, _ = Permission.objects.get_or_create(name=name)
        print('create permission %s' % perm.name)


def init_vip():
    for i in range(4):
        vip, _ = Vip.objects.get_or_create(
            name='会员-%d' % i,
            level=i,
            price=i * 5.0
        )
        print('create %s' % vip.name)


def create_vip_perm_relations():
    """创建 Vip 和 Permission 的关系"""
    # 获取 VIP
    vip1 = Vip.objects.get(level=1)
    vip2 = Vip.objects.get(level=2)
    vip3 = Vip.objects.get(level=3)

    # 获取权限
    permissions = {
        'vipflag': Permission.objects.get(name='vipflag'),
        'superlike': Permission.objects.get(name='superlike'),
        'rewind': Permission.objects.get(name='rewind'),
        'anylocation': Permission.objects.get(name='anylocation'),
        'unlimit_like': Permission.objects.get(name='unlimit_like')
    }

    vip_permissions = {
        1: ['vipflag', 'superlike'],
        2: ['vipflag', 'rewind', 'unlimit_like'],
        3: ['vipflag', 'superlike', 'rewind', 'anylocation', 'unlimit_like']
    }

    for level, perm_names in vip_permissions.items():
        try:
            vip = Vip.objects.get(level=level)
            for perm_name in perm_names:
                perm = permissions[perm_name]
                relation, created = VipPermRelation.objects.get_or_create(vip=vip, perm=perm)
                if created:
                    print(f"Added permission '{perm_name}' to VIP Level '{vip.name}'.")
        except (Vip.DoesNotExist, Permission.DoesNotExist) as e:
            print(f"Error creating relations for VIP level {level}: {e}")


if __name__ == '__main__':
    # create_robots(1000)
    init_permission()
    init_vip()
    create_vip_perm_relations()