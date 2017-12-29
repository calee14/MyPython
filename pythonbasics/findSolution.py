def findSolution(target):
  def find(current, history):

    if current == target:
      #base case 1
      #if we actually find the number
      return history
    elif current > target:
      #base case 2
      #if the path we took is bigger than the target
      return None
    else:
      #base case 3
      #if current is less than target create a new path and call recursive function
      return find(current + 5, str("(" + history + " + 5)")) or find(current * 3, str("(" + history + " * 3)"))
  return find(1,"1")
print(findSolution(18));