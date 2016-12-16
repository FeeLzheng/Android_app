import pymysql



def delete_outworkrecord():
    conn = pymysql.connect(host='192.168.1.37', port=3307, user='smartstage', passwd='Uni-Ubi@SS2016', db='smartstage')
    cur=conn.cursor()
    print("连接数据成功")
    try :
        sql = """delete from uniubi_employee2 where name="1zheng_ceshi12" and state =2"""
        cur.execute(sql)
        conn.commit()
        print("成功删除")

    except Exception as e:
        conn.rollback()
        print(e)
        print("删除失败")

    finally:
        cur.close()
        conn.close()
