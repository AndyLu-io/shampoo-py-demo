from crawel.charles.maoyan.basic.my_contacts import fetch_my_maoyan_contacts
from crawel.charles.maoyan.performance.create_order import handle_create_order
from crawel.charles.maoyan.performance.create_order_v2 import handle_create_order1

watch_name_list = ['卢晓波']


def get_watch_contacts(watch_name_list):
    result_list = []
    my_maoyan_contacts = fetch_my_maoyan_contacts()
    for contact in my_maoyan_contacts:
        if contact['userName'] in watch_name_list:
            result_list.append(contact)

    return result_list


watch_contacts = get_watch_contacts(watch_name_list)
print(watch_contacts)


projectId = 366138
showId = 2284212
ticketId =23029014
price = 680
num = len(watch_contacts)
watch_contacts_str= str(watch_contacts)

# handle_create_order(projectId, showId, ticketId, price, num, watch_contacts_str)

handle_create_order1(projectId, showId, ticketId, price, num, watch_contacts_str)