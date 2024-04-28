import sqlite3

def delete_order_if_empty(order_id, conn):
    cur = conn.cursor()
    # Проверяем, есть ли в заказе товары с количеством больше 0
    cur.execute("SELECT COUNT(*) FROM Orders WHERE id = ? AND quantity > 0", (order_id,))
    count = cur.fetchone()[0]

    if count == 0:
        # Если в заказе нет товаров, спрашиваем пользователя, хочет ли он удалить заказ
        response = input("В вашем заказе нет активных товаров. Хотите удалить заказ? (да/нет): ")
        if response.lower() == 'да':
            # Пользователь подтвердил удаление, удаляем заказ
            cur.execute("DELETE FROM Orders WHERE id = ?", (order_id,))
            conn.commit()
            print("Заказ удален.")
        else:
            print("Удаление заказа отменено.")
    else:
        print("В заказе есть активные товары. Удаление не выполнено.")

    cur.close()






























