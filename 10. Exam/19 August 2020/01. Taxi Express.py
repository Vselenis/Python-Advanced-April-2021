# customers = [int(number) for number in input().split(", ")]
# taxis = [int(number) for number in input().split(", ")]
#
#
#
# total_time = 0
#
# while True:
#     if len(customers) == 0:
#         print("All customers were driven to their destinations")
#         print(f"Total time: {total_time} minutes")
#         break
#     elif len(taxis) == 0 and len(customers) > 0:
#         print("Not all customers were driven to their destinations")
#         print(f'Customers left: {", ".join([str(c)for c in customers])}')
#         break
#
#     customer = customers[0]
#     taxi = taxis[-1]
#
#     if taxi >= customer:
#         total_time += customer
#         customers.pop(0)
#         taxis.pop(-1)
#     else:
#         taxis.pop(-1)


n = -6 / 2
print(abs(n))