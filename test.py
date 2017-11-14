import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.basemap import Basemap

m = Basemap(projection='merc',
            llcrnrlat=52.0,urcrnrlat=58.0,
            llcrnrlon=19.0,urcrnrlon=40.0,
            rsphere=6371200.,resolution='h',area_thresh=10)

fig = plt.figure()
ax = Axes3D(fig)
ax.add_collection3d(m.drawcoastlines(linewidth=0.25))
ax.add_collection3d(m.drawcountries(linewidth=0.35))
ax.add_collection3d(m.drawrivers(color='blue'))

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Height')

fig.show()