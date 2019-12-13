# Enhancing Seattle's SCADA System

## Leighlyn Ha

The main aim of this capstone project was to enhance the Seattle Public Utilities (SPU) Supervisory Control and Data Acquisition (SCADA) system that collects and stores Washington environmental and Seattle utilities data for clients to use. These are important for resource planning, performance analysis, monitoring, and maintenance of Seattle’s infrastructure and utilities systems, weather and sewage flow modeling, and project planning.

Infrastructure, client, and developer requirements have changed since the SCADA system was first implemented. New data sources needed to be incorporated and data sources no longer relevant to clients needed to be historicized (stop pulling live data). The SCADA databases were in need of restructuring to accommodate these existing and new data sources, using only SQL databases (with which the Wonderware SCADA system works best with). Data retrieval applications needed to be refactored for better readability, maintainability, and to pull data for newly requested data sources. A custom .NET application (called Zonar) was also requested by clients to analyze utility truck driver performance.

My work involved completing many diverse tasks from of this major body of work. I worked with clients to historicize Duwamish Tidal and Genesee CSO site tags, making changes to the Oracle and SQL databases. I created and modified .NET code (such as creating and testing the USGS class) on the SDSP and Historian Operations .NET applications, gaining experience working with these legacy systems and code. I also created a database and .NET application to pull and store requested Zonar data, researching C# techniques for working with APIs and SQL databases. All changes were thoroughly documented and communicated to other team members and clients.

Although this body of work is still ongoing, clients are now able to view data from requested USGS, NOAA, NOAA Tides, and vendor-contracted FlowWorks data sources, enabling them to make better decisions for resource planning, performance, operation, maintenance, and project planning. Data retrieval classes were simplified (derived from a base class) and have unit tests. Selected data points for Duwamish Tidal and Genesee Combined Sewage Overflow sites were historicized and approved by user acceptance testing. There are many more sites planned for historization, but this work has been backlogged due to higher priority .NET and database work. The initial version of the Zonar application .NET code, unit tests, and database have been completed, successfully pulling and storing data. Further unit testing and construction of the Excel spreadsheet to display the data is in progress.


***

[Yusuf Pisan](https://pisanorg.github.io/yusuf/) | [Computing & Software Systems (CSS)](https://www.uwb.edu/css) | [University of Washington Bothell](https://www.uwb.edu/)
