import pcl
import numpy as np
points_1 = np.array([0,0,0,
                     1,0,0,
                     0,1,0,
                     1,1,0], dtype=np.float32).reshape([4,3])
points_2 = np.array([0,0,0.2,
                     1,0,0,
                     0,1,0,
                     1.1,1,0.5], dtype=np.float32).reshape([4,3])

print 'pc_1:'
print points_1
print '\npc_2:'
print points_2
print '\n'
pc_1 = pcl.PointCloud()
pc_1.from_array(points_1)
pc_2 = pcl.PointCloud()
pc_2.from_array(points_2)
kd = pc_1.make_kdtree_flann()
# find the single closest points to each point in point cloud 2
# (and the sqr distances)
indices, sqr_distances = kd.nearest_k_search_for_cloud(pc_2, 1)
for i in range(pc_1.size):
    print 'index of the closest point in pc_1 to point ' + `i` + \
        ' in pc_2 is ' + `indices[i,0]`
    print 'the squared distance between these two points is ' + \
        `sqr_distances[i,0]` + '\n'
