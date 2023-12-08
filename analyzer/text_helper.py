import re

file = open('../symbolic_result.txt', 'r')
text = file.read()
file.close()

text = text.replace('0x', '')

text = text.replace('mem_fff8000000000000', 'p.type')
text = text.replace('mem_fff8000000000008', 'p.o1.value')
text = text.replace('mem_fff8000000000010', 'p.o2.value')
text = text.replace('mem_ffc0000000000000', 'target.type')
text = text.replace('mem_ffc0000000000008', 'target.o1.value')
text = text.replace('mem_ffc0000000000010', 'target.o2.value')

text = text.replace('fff8000000000000', '&p.type')
text = text.replace('fff8000000000008', '&p.o1.value')
text = text.replace('fff8000000000010', '&p.o2.value')
text = text.replace('ffc0000000000000', '&target.type')
text = text.replace('ffc0000000000008', '&target.o1.value')
text = text.replace('ffc0000000000010', '&target.o2.value')
text = text.replace("UNINITIALIZED", '')

text = text.replace(f"{{}}", '')

text = re.sub(r'_[0-9][0-9][0-9]_[0-9][0-9]', '', text)
text = re.sub(r' 0 ', ' SHL ', text)
text = re.sub(r' 1 ', ' MUL ', text)

# write to file
file = open('../symbolic_result.txt', 'w')
file.write(text)
file.close()