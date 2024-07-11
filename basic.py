tilecolor = {'red':10,'gold':20,'white':60,'blue':30}



print('-----ราคากระเบื้อง-----')
for c,t in tilecolor.items():
    print('สี: {} ราคา: {}'.format(c,t))


print('------Calculate program by Temmy------')

try:
    tiles  = int(input('installation amount of : '))
    row = int(input('1 row installation amount of : '))
    color = input ('What color tiles do u want? [red/gold/white/blue]:')
    
except:
    print('Please fill in information is only number!')
    tiles  = int(input('installation amount of : '))
    row = int(input('1 row installation amount of : '))
    color = input ('What color tiles do u want? [red/gold/white]:')
    
print('----Calculate----')
total_row = tiles // row
remain_tiles = tiles % row


buy_more = row - remain_tiles

print(f'มีกระเบื้องทั้งหมด: {tiles} แผ่น')
print(f'1 แถวปูมีกระเบื้องได้ทั้งหมด: {row} แผ่น')
print('--------คำนวณ--------')
print('ต้องปูกระเบื้องทั้งหมด {} แถว'.format(total_row))
print('เหลือกระเบื้องที่ยังไม่ได้ปูเต็มแถว {} แผ่น'.format(remain_tiles))
print('ลูกค้าต้องซื้อกระเบื้องเพิ่ม {} แผ่น'.format(buy_more))
print('ยอดรวมทั้งหมดที่ต้องซื้อกระเบื้องเพิ่ม: {} บาท'.format(buy_more*tilecolor[color]))

#ลูกค้าต้องซื้อกระเบื้องเพิ่มอีกกี่แผ่น
print('-----The End-----')