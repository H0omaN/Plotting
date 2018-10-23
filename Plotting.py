from netCDF4 import Dataset as NetCDFFile 
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.basemap import Basemap, cm
import matplotlib.colors as mcolors
nc = NetCDFFile('/home/z5194283/Mygit/Data/MRMS/NCs/MRMSGC6H2018091400.nc', 'r')
lat = nc.variables['latitude'][:]
lon = nc.variables['longitude'][:]
u = nc.variables['GaugeCorrQPE06H_0mabovemeansealevel'][:]
#u=np.transpose(u) # 10m u-component of winds
map = Basemap(projection='merc',llcrnrlon=-130.,llcrnrlat=20.,urcrnrlon=-60.,urcrnrlat=55.,resolution='i') # projection, lat/lon extents and resolution of polygons to draw
# resolutions: c - crude, l - low, i - intermediate, h - high, f - full
map.drawcoastlines()
map.drawstates()
map.drawcountries()
#map.drawlsmask(land_color='Linen', ocean_color='#CCFFFF') # can use HTML names or codes for colors
#map.drawcounties()
parallels = np.arange(20,60,15.) # make latitude lines ever 5 degrees from 30N-50N
meridians = np.arange(-130,-60,15.) # make longitude lines every 5 degrees from 95W to 70W
map.drawparallels(parallels,labels=[1,0,0,0],fontsize=10)
map.drawmeridians(meridians,labels=[0,0,0,1],fontsize=10)



lons,lats= np.meshgrid(lon,lat) # for this dataset, longitude is 0 through 360, so you need to subtract 180 to properly display on map
x,y = map(lons,lats)
a=np.max(u[0,:,:])
clevs = np.arange(0,a,(a-0)/20)
cmap_data = [(1.0, 1.0, 1.0),
             (0.3137255012989044, 0.8156862854957581, 0.8156862854957581),
             (0.0, 1.0, 1.0),
             (0.0, 0.8784313797950745, 0.501960813999176),
             (0.0, 0.7529411911964417, 0.0),
             (0.501960813999176, 0.8784313797950745, 0.0),
             (1.0, 1.0, 0.0),
             (1.0, 0.6274510025978088, 0.0),
             (1.0, 0.0, 0.0),
             (1.0, 0.125490203499794, 0.501960813999176),
             (0.9411764740943909, 0.250980406999588, 1.0),
             (0.501960813999176, 0.125490203499794, 1.0),
             (0.250980406999588, 0.250980406999588, 1.0),
             (0.125490203499794, 0.125490203499794, 0.501960813999176),
             (0.125490203499794, 0.125490203499794, 0.125490203499794),
             (0.501960813999176, 0.501960813999176, 0.501960813999176),
             (0.8784313797950745, 0.8784313797950745, 0.8784313797950745),
             (0.9333333373069763, 0.8313725590705872, 0.7372549176216125),
             (0.8549019694328308, 0.6509804129600525, 0.47058823704719543),
             (0.6274510025978088, 0.42352941632270813, 0.23529411852359772),
             (0.4000000059604645, 0.20000000298023224, 0.0)]
cmap = mcolors.ListedColormap(cmap_data, 'precipitation')
#cs = map.contourf(x,y,u[0,:,:],clevs,cmap=cm.s3pcpn)#colors='blue')#,linewidths=1.)
cs = map.imshow(u[0,:,:],cmap=cmap)# cmap=cm.s3pcpn)#, alpha = 0.5)
#plt.clabel(cs, fontsize=9, inline=1) # contour labels

cbar = map.colorbar(cs,location='right',pad="5%")
cbar.set_label('mm')

plt.title('MRMS - Precipitation')
#cs = map.imshow(u,x,y)     #contour(x,y,mslp[0,:,:]/100.,clevs,colors='blue',linewidths=1.)