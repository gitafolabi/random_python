import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt

projection = ccrs.PlateCarree()
fig, ax = plt.subplots(subplot_kw={'projection': projection})
ax.set_extent([-180, 180, -90, 90], crs=ccrs.PlateCarree())

ax.add_feature(cfeature.LAND, facecolor='lightgray')
ax.add_feature(cfeature.COASTLINE, edgecolor='black')
ax.add_feature(cfeature.BORDERS, edgecolor='black')
ax.add_feature(cfeature.LAKES, edgecolor='blue')
ax.add_feature(cfeature.RIVERS, edgecolor='blue')
ax.add_feature(cfeature.OCEAN, facecolor='lightblue')

ax.gridlines(draw_labels=True)
plt.show()