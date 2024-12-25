from django.db import models
from django.db.models import Q

from user.models import User


class Swiper(models.Model):
    """滑动记录"""
    STATUS = (
        ('superlike', '超级喜欢'),
        ('like', '喜欢'),
        ('dislike', '不喜欢')
    )

    uid = models.IntegerField(verbose_name='划动者的 UID')
    sid = models.IntegerField(verbose_name='被划动者的 UID')
    status = models.CharField(max_length=8, choices=STATUS)
    time = models.DateTimeField(auto_now_add=True)

    @classmethod
    def mark(cls, uid, sid, status):
        """标记一次滑动"""
        if status in ['superlike', 'like', 'dislike']:
            defaults = {'status': status}
            cls.objects.create(uid=uid, sid=sid, defaults=defaults)

    @classmethod
    def is_liked(cls, uid, sid):
        """检查是否喜欢过某人"""
        return cls.objects.filter(uid=uid, sid=sid,
                                  status__in=['like', 'superlike']).exists()


class Friend(models.Model):
    """好友"""
    uid1 = models.IntegerField()
    uid2 = models.IntegerField()

    @classmethod
    def be_friends(cls, uid1, uid2):
        """成为好友"""
        uid1, uid2 = (uid1,uid2) if uid1 < uid2 else (uid2, uid1)
        cls.objects.get_or_create(uid1=uid1, uid2=uid2)

    @classmethod
    def is_friend(cls, uid1, uid2):
        """检查是否是好友关系"""
        condition = Q(uid1=uid1, uid2=uid2) | Q(uid1=uid2, uid2=uid1)
        return cls.objects.filter(condition).exists()

    @classmethod
    def break_off(cls, uid1, uid2):
        """断交"""
        uid1, uid2 = (uid1, uid2) if uid1 < uid2 else (uid2, uid1)
        try:
            cls.objects.get(uid1=uid1, uid2=uid2).delete()
        except cls.DoesNotExist:
            pass

    @classmethod
    def friends(cls, uid):
        candition = Q(uid1=uid) | Q(uid2=uid)
        relations = cls.objects.filter(candition)

        friend_id_list = []
        for r in relations:
            friend_id = r.uid2 if r.uid1 == uid else r.uid1
            friend_id_list.append(friend_id)

        return User.objects.filter(id__in=friend_id_list)