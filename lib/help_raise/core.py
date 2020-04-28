#!/usr/bin/evn python3


def confirm_attributions(tg_ins, attrs):
    emes_base = "{} doesn's have {} as a attribute."
    for atr in attrs:
        if not hasattr(tg_ins, atr):
            emes = emes_base.format(tg_ins, atr)
            raise AttributeError(emes)


def confirm_kwargs(kwargs_dict):
    if len(kwargs_dict) != 0:
        hmsg = "invalid argument are entered."\
               "kwargs is :{}".format(kwargs_dict)
        raise TypeError(hmsg)


def confirm_spclss(instance, spcls):
    if spcls not in type(instance).__bases__:
        mes = "{} is invalid type.\n"\
              "spcls must be {}".format(instance, spcls)
        raise TypeError(mes)


def confirm_type_list(target_li, type_ob=str):
    for ob in target_li:
        if type(ob) != type_ob:
            emes_base = "ob must be invalid type:{}"
            emes = emes_base.format(type_ob)
            raise TypeError(emes)


def confirm_attributions_list(target_li,
                              attr_name="__call__"):
    for ob in target_li:
        if not hasattr(ob, attr_name="__call__"):
            emes_base = "{} doesn't have attributions:{}"
            emes = emes_base.format(ob, attr_name)
            raise AttributeError(emes)
