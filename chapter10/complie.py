python_code = '''
def add_numbers(a, b):
    return a + b
result = add_numbers(5, 10)
print("Result : ", result)
'''

complied_code = compile(python_code, '<string>', 'exec')

exec(complied_code)