import os, sqlite3

db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)

# 初始数据:
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()

def get_score_in(low, high):#返回指定分数区间的名字，按分数从低到高排序
    conn=sqlite3.connect(db_file)
    cursor=conn.cursor()
    sql='select name,score from user where score>={0} and score<={1} order by score'.format(low,high)
    cursor.execute(sql)
    rst=cursor.fetchall()
    cursor.close()
    conn.close()
    l=[]
    for i in rst:
        l.append(i[0])
    return l
# 测试:assert condition,用来让程序测试这个condition，如果condition为false，那么raise一个AssertionError出来。
assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)

print('Pass')