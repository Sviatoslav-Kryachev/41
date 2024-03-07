int_num = 5
float_num = 4.5
print(int_num + float_num)

bool_val = True
int_val = 7
print(bool_val + int_val)

# поменял местами порядок оперантов
int_num = 5
float_num = 4.5
print(float_num + int_num)

bool_val = True
int_val = 7
print(int_val + bool_val)

int_num = 50
float_num = 7.5

# print(int_num * float_num)
print(int_num.__mul__(float_num))
# NotImplemented
print(float_num.__rmul__(int_num))

int_num = 50
str_val = 'abc'

print(int_num*str_val)

# меняю порядок операндов при умножении
int_num = 50
str_val = 'abc'

print(str_val*int_num)
