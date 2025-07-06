#方式1：使用print直接输出类型信息
print(type("kun"))
print(type(123))
print(type(12.3))
#方式2：使用type()语句的结果
string_type = type("kun")
int_type = type(123)
float_type = type(12.3)
print(string_type)
print(int_type)
print(float_type)
#方式3：使用type()语句，查看变量中储存的数据类型信息
name = "kun"
name_type = type(name)
print(name_type)