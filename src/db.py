from tkinter import messagebox

import pymysql

host = 'localhost'
user = 'root'
pwd = 'root'
db = 'answering_system'


class Database:

    def __init__(self):
        """初始化数据库连接"""
        try:
            self.conn = pymysql.connect(host=host, user=user, password=pwd, db=db, port=3306, charset='utf8')
            self.cursor = self.conn.cursor()
        except Exception as e:
            messagebox.showerror('错误', '连接失败，请检查信息是否正确!\n' + str(e))

    def query_question(self, _id: int) -> str:
        """Query_question"""
        question = '''SELECT q.question
                                FROM as_questions q
                                WHERE `id`= %s 
                    '''  # %s作为占位符，防止SQL注入
        self.cursor.execute(question, _id)
        data = self.cursor.fetchone()  # 查询到的数据为空，返回None
        if not data:
            # messagebox.showinfo('提示', '没有查询到该题号对应的题目')
            return "\n\n\n查询失败" + '\n' + "没有查询到该题号对应的题目" \
                                         "" + "\n\n" "注意:第一题查询失败并不是所有都不能显示，只是题号为 1 的题不存在"

        else:
            # 只有查询到数据才会又返回值索引！！！！！！！
            # 查询题目显示的一行，为元组类型(one,),取第一个索引切片拿到完整题目，带上题号
            return ("%d、" % _id) + data[0]

    # 查询成功不显示任何信息
    # else:
    #     messagebox.showinfo('提示', '查询成功')

    def query_answer(self, _id: int) -> str:
        """Query answer"""
        question = '''SELECT a.answer
                                FROM as_answers a
                                WHERE `id`= %s 
                            '''  # %s作为占位符，防止SQL注入
        self.cursor.execute(question, _id)
        data = self.cursor.fetchone()  # 查询到的数据为空，返回None
        if not data:
            messagebox.showinfo('提示', '没有查询到该题号对应的答案')
            # return "\n\n\n没有查询到该题号对应的答案"

        else:
            # 只有查询到数据才会又返回值索引！！！！！！！
            # 查询题目显示的一行，为元组类型(one,),取第一个索引切片拿到完整题目，带上题号
            return ("%d、" % _id) + data[0]
            # messagebox.showinfo("答案",)

    def question_count(self) -> int:
        """返回记录的条数"""
        query_count = '''SELECT COUNT(*) FROM as_questions LIMIT 1'''
        self.cursor.execute(query_count)
        data = self.cursor.fetchone()  # 返回元组
        for i in data:
            return i

    def question_id(self) -> list:
        """返回存在记录的题号,返回一个列表"""
        query_id = '''SELECT `id` FROM as_questions'''
        self.cursor.execute(query_id)
        data = self.cursor.fetchall()
        list_ = [j for i in data for j in i]  # 列表推导式，遍历二重元组
        # print(list_)
        return list_


if __name__ == '__main__':
    db = Database()
    print(db.question_id())
    a = db.question_id()
    print(2 in a)
