#规则1：内容限定：中文、英文、数字、下划线_,不能以数字开头
#1name = "kun"  # 错误，变量名不能以数字开头
#name_!= "kun"  # 错误，包含非法字符 '!'
name_ = "kun"  # 正确，变量名以字母开头，包含下划线
_name = "kun"  # 正确，变量名以字母开头，包含下划线
print(name_, _name)
#规则2：大小写敏感
Name = "kun"  # 正确，变量名以字母开头，包含下划线
name = "雪豹"
print(Name,name)
#规则3：不能使用关键字
#class=1  # 错误，'class' 是 Python 的关键字
# def=2  # 错误，'def' 是 Python 的关键字
Class=1