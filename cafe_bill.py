latte_price = 400
muffin_price = 250
water_price = 100

latte_ordered = 2
muffin_ordered = 3
water_ordered = 1

total_bill = (latte_price * latte_ordered) + (muffin_price * muffin_ordered) + (water_price * water_ordered)
service_charged = 150
final_bill = total_bill + service_charged

print("Your total bill is:", final_bill)
friends_sharing = 3
split_amount = final_bill/ friends_sharing
print("Each friend should pay:", split_amount)
