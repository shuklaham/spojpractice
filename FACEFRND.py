
def main():
	num_friends = int(raw_input())
	friends = set()
	connectedFriends = set()
	for i in range(num_friends):
		inp = [int(x) for x in raw_input().split()]
		friends.add(inp[0])
		connectedFriends = connectedFriends | set(inp[2:])
	print len(connectedFriends - friends)

main()
