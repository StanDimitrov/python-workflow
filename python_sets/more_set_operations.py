# cricket = {"India","England","Australia","New Zealand", "Pakistan","Bangladesh","South Africa"}
# soccer = {"England","India","Spain","Bangladesh","USA"}
#
# # either_or_both = cricket.union(soccer) # . union will unit the two sets and returning back to us all the characters
# # print(either_or_both) # we can use | for union
# # either_or_both = soccer | cricket
#
# # intersection will return to us only the comma elements in the two sets
# both = cricket.intersection(soccer) # we can use & operator
# print(both)
#
# # difference method will find the differencts elements in each ot the two sets
# only_cricket = cricket.difference(soccer) # we can use - for difference operator
# print(only_cricket)
#
# # symetric diffeerence will take the elements witch are not in comma from both of the sets
# either_or = cricket.symmetric_difference(soccer) # we can use ^ operator for this method
# print(either_or)

# set_a = {"H", "e", "l","l,","o"}
# if "e" in set_a: # we cat use not in
#     print("d exist as member")
# else:
#     print("d is not exist as member")

set_b = {"W","e","l","c","o","m","e"}
set_c = {"P","y","t","h","o","n"}
# set_b.difference_update(set_c) # difference_update will discard all the same elements from set_c to set_b
# print(set_b)
# set_b.symmetric_difference_update(set_c) # this method will remove all the same elements of the two sets
# print(set_b)

print(set_b.isdisjoint(set_c)) # this method will tell us if it doesn't have any comment elements of the two sets
print(set_b.issuperset(set_c)) # if all the charatcers in set_b are presented in set_c so the set_b is superset of set_c
print(set_b.issubset(set_c)) # if all the characters in set_c are presented in set_b so set_c is subset of set_