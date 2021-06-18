#encoding=utf-8
'''参考网址https://www.cnblogs.com/Detector/p/8085460.html'''

def get_target_value(key, dic, tmp_list):
    """
    :param key: 目标key值
    :param dic: JSON数据
    :param tmp_list: 用于存储获取的数据
    :return: list
    """
    if not isinstance(dic, dict) or not isinstance(tmp_list, list):  # 对传入数据进行格式校验
        return 'argv[1] not an dict or argv[-1] not an list '

    if key in dic.keys():
        tmp_list.append(dic[key])  # 传入数据存在则存入tmp_list

    for value in dic.values():  # 传入数据不符合则对其value值进行遍历
        if isinstance(value, dict):
            get_target_value(key, value, tmp_list)  # 传入数据的value值是字典，则直接调用自身
        elif isinstance(value, (list, tuple)):
            _get_value(key, value, tmp_list)  # 传入数据的value值是列表或者元组，则调用_get_value


    return tmp_list


def _get_value(key, val, tmp_list):
    for val_ in val:
        if isinstance(val_, dict):
            get_target_value(key, val_, tmp_list)  # 传入数据的value值是字典，则调用get_target_value
        elif isinstance(val_, (list, tuple)):
            _get_value(key, val_, tmp_list)   # 传入数据的value值是列表或者元组，则调用自身


dict1={'result': '0',
 'msg': '',
 'nickname': '动起来赶走寂寞',
 'level': '145',
 'combat': '62060',
 'arena_rank': '黄金IV',
 'baseattr': [{'value': '391 + 6957', 'name': '生命'},
  {'value': '54 + 308', 'name': '力量'},
  {'value': '54 + 263', 'name': '敏捷'},
  {'value': '110 + 633', 'name': '速度'},
  {'value': '312', 'name': '固定伤害'},
  {'value': '386', 'name': '固定减伤'},
  {'value': '0', 'name': '真实伤害'}],
 'menpai': [{'value': '峨眉', 'name': '当前所属门派'},
  {'value': '门众', 'name': '门派职位'},
  {'value': '97%', 'name': '门派武器伤害'},
  {'value': '103%', 'name': '门派武器减免'},
  {'value': '22%', 'name': '门派技能伤害'},
  {'value': '22%', 'name': '门派技能减免'}],
 'five_ele': [{'atk': '85', 'dfs': '85', 'name': '金'},
  {'atk': '85', 'dfs': '60', 'name': '木'},
  {'atk': '48', 'dfs': '60', 'name': '水'},
  {'atk': '40', 'dfs': '65', 'name': '火'},
  {'atk': '52', 'dfs': '75', 'name': '土'}],
 'weaponatk': [{'name': '武器命中率',
   'weapon_hit': [{'value': '793%', 'name': '大型武器'},
    {'value': '767%', 'name': '中型武器'},
    {'value': '774%', 'name': '小型武器'},
    {'value': '770%', 'name': '投掷武器'}]},
  {'name': '武器暴击率',
   'weapon_crit': [{'value': '398%', 'name': '大型武器'},
    {'value': '396%', 'name': '中型武器'},
    {'value': '402%', 'name': '小型武器'},
    {'value': '398%', 'name': '投掷武器'}]},
  {'name': '武器暴击伤害', 'crit_damage': [{'value': '267%', 'name': '武器暴击伤害'}]},
  {'name': '武器伤害值/百分比',
   'weapon_damage': [{'value': '793/118%', 'name': '大型武器'},
    {'value': '721/123%', 'name': '中型武器'},
    {'value': '958/122%', 'name': '小型武器'},
    {'value': '762/122%', 'name': '投掷武器'}]},
  {'name': '武器穿透',
   'weapon_penetrate': [{'value': '77%', 'name': '大型武器'},
    {'value': '37%', 'name': '中型武器'},
    {'value': '83%', 'name': '小型武器'},
    {'value': '83%', 'name': '投掷型武器'}]},
  {'name': '抗武器韧性',
   'dec_weapon_toughness': [{'value': '13%', 'name': '大型武器'},
    {'value': '13%', 'name': '中型武器'},
    {'value': '17%', 'name': '小型武器'},
    {'value': '17%', 'name': '投掷型武器'}]}],
 'weapon_dfs': [{'name': '武器闪避率',
   'weapon_miss': [{'value': '703%', 'name': '大型武器'},
    {'value': '678%', 'name': '中型武器'},
    {'value': '684%', 'name': '小型武器'},
    {'value': '676%', 'name': '投掷武器'}]},
  {'name': '抗武器暴击率',
   'dec_weapon_crit': [{'value': '312%', 'name': '大型武器'},
    {'value': '310%', 'name': '中型武器'},
    {'value': '314%', 'name': '小型武器'},
    {'value': '312%', 'name': '投掷武器'}]},
  {'name': '抗武器暴击伤害',
   'dec_crit_damage': [{'value': '205%', 'name': '抗武器暴击伤害'}]},
  {'name': '抗武器伤害值/百分比',
   'dec_weapon_damage': [{'value': '675/75%', 'name': '大型武器'},
    {'value': '608/75%', 'name': '中型武器'},
    {'value': '746/75%', 'name': '小型武器'},
    {'value': '608/75%', 'name': '投掷武器'}]},
  {'name': '抗武器穿透',
   'dec_weapon_penetrate': [{'value': '17%', 'name': '大型武器'},
    {'value': '9%', 'name': '中型武器'},
    {'value': '17%', 'name': '小型武器'},
    {'value': '1%', 'name': '投掷型武器'}]},
  {'name': '武器韧性',
   'weapon_toughness': [{'value': '27%', 'name': '大型武器'},
    {'value': '27%', 'name': '中型武器'},
    {'value': '37%', 'name': '小型武器'},
    {'value': '37%', 'name': '投掷型武器'}]}],
 'suatk': [{'name': '命中率',
   'suhit': [{'value': '778%', 'name': '技能命中率'},
    {'value': '762%', 'name': '空手命中率'}]},
  {'name': '暴击率',
   'sucritrate': [{'value': '381%', 'name': '技能暴击率'},
    {'value': '360%', 'name': '空手暴击率'}]},
  {'name': '暴击伤害',
   'sucrit': [{'value': '182%', 'name': '技能暴击伤害'},
    {'value': '267%', 'name': '空手暴击伤害'}]},
  {'name': '伤害值/百分比',
   'sudamage': [{'value': '584/159%', 'name': '技能'},
    {'value': '529/71%', 'name': '空手'}]},
  {'name': '穿透',
   'supenettration': [{'value': '38%', 'name': '技能'},
    {'value': '1%', 'name': '空手'}]},
  {'name': '抗韧性', 'dec_sutoughness': [{'value': '11%', 'name': '技能'}]}],
 'sudef': [{'name': '闪避率',
   'sumiss': [{'value': '646%', 'name': '技能闪避率'},
    {'value': '646%', 'name': '空手闪避率'}]},
  {'name': '抗暴击率',
   'dsucritrate': [{'value': '280%', 'name': '抗技能暴击率'},
    {'value': '280%', 'name': '抗空手暴击率'}]},
  {'name': '抗暴击伤害',
   'dsucrit': [{'value': '170%', 'name': '抗技能暴击伤害'},
    {'value': '205%', 'name': '抗空手暴击伤害'}]},
  {'name': '抗伤害值/百分比',
   'dsudamage': [{'value': '504/66%', 'name': '技能'},
    {'value': '438/76%', 'name': '空手'}]},
  {'name': '抗穿透',
   'dec_supenettration': [{'value': '2%', 'name': '技能'},
    {'value': '1%', 'name': '空手'}]},
  {'name': '韧性', 'sutoughness': [{'value': '27%', 'name': '技能'}]}]}

print(get_target_value('name',dict1,[]))
