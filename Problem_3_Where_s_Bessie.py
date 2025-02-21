from typing import List

MAX_N = 20


class PCL:
	def __init__(self, i1: int, j1: int, i2: int, j2: int):
		self.i1 = i1
		self.j1 = j1
		self.i2 = i2
		self.j2 = j2

	def is_inside(self, other: "PCL") -> bool:
		return (
			self.i1 >= other.i1
			and self.i2 <= other.i2
			and self.j1 >= other.j1
			and self.j2 <= other.j2
		)


image = [[""] * MAX_N for _ in range(MAX_N)]
visited = [[False] * MAX_N for _ in range(MAX_N)]


def floodfill(i: int, j: int, color: str):
	"""Floodfill to find the connected regions"""
	stack = [(i, j)]
	visited[i][j] = True
	while stack:
		cur_i, cur_j = stack.pop()
		for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
			new_i, new_j = cur_i + di, cur_j + dj
			if (
				i_min <= new_i <= i_max
				and j_min <= new_j <= j_max
				and not visited[new_i][new_j]
				and image[new_i][new_j] == color
			):
				visited[new_i][new_j] = True
				stack.append((new_i, new_j))


def is_pcl(i1: int, j1: int, i2: int, j2: int) -> bool:
	""":returns: whether the given rectangle forms a PCL"""
	global i_min, i_max, j_min, j_max
	# Keep track of number of regions for each color
	region_count = [0] * 26

	# Set bounds for floodfill
	i_min, i_max, j_min, j_max = i1, i2, j1, j2

	# Count connected regions for each color within the rectangle bounds
	for i in range(i1, i2 + 1):
		for j in range(j1, j2 + 1):
			if not visited[i][j]:
				curr_color = image[i][j]
				region_count[ord(curr_color) - ord("A")] += 1
				floodfill(i, j, curr_color)

	# Reset visited array for the current rectangle
	for i in range(i1, i2 + 1):
		for j in range(j1, j2 + 1):
			visited[i][j] = False

	# Verify PCL conditions
	color_count = 0
	color_with_one_region = False
	color_with_more_regions = False
	for count in region_count:
		if count != 0:
			color_count += 1
		if count == 1:
			color_with_one_region = True
		if count > 1:
			color_with_more_regions = True

	return color_count == 2 and color_with_one_region and color_with_more_regions


n = int(input().strip())
image = [list(input().strip()) for _ in range(n)]

pcl_list = []
# Brute force every rectangle to find PCLs
for i1 in range(n):
	for j1 in range(n):
		for i2 in range(i1, n):
			for j2 in range(j1, n):
				if (i2 - i1 + 1) * (j2 - j1 + 1) < 2:
					continue
				if is_pcl(i1, j1, i2, j2):
					pcl_list.append(PCL(i1, j1, i2, j2))

pcl_count = 0
# Check each PCL and ensure it is not inside another PCL
for i in range(len(pcl_list)):
	valid_pcl = True
	for j in range(len(pcl_list)):
		if i == j:
			continue
		if pcl_list[i].is_inside(pcl_list[j]):
			valid_pcl = False
			break
	pcl_count += valid_pcl

print(pcl_count)