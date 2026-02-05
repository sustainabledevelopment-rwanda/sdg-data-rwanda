# Open SDG Rwanda - Data Repository

This repository holds the data for SDG reporting for Rwanda. 

The main SDG reporting site for Rwanda can be found at https://sustainabledevelopment-rwanda.github.io/.

# Structure

This **data repository** is part of the implementation of the [Open SDG](https://github.com/open-sdg/open-sdg) platform for Rwanda. [See here for documentation](https://open-sdg.readthedocs.io).

## Repositories

In total, three repositories are involved in the Open SDG implementation:
- Data repository: [sdg-data-rwanda](https://github.com/sustainabledevelopment-rwanda/sdg-data-rwanda) **(you are here!)**
- Staging site repository: [sdg-site-rwanda](https://github.com/sustainabledevelopment-rwanda/sdg-site-rwanda)
- Production site repository: [sustainabledevelopment-rwanda.github.io](https://github.com/sustainabledevelopment-rwanda/sustainabledevelopment-rwanda.github.io)

## Deployment

The three repositories described in the previous section are linked in the deployment process.

### Data site

The **data repository** is used to hold and update data for SDG reporting. 

The `develop` branch of the data respository serves from the `gh-pages` branch on this repository.

It deploys to the **data site** at https://sustainabledevelopment-rwanda.github.io/sdg-data-rwanda/.

It usually takes around 5 minutes after an update is merged to the data repository for the deployment to take place.

In the standard implementation of Open SDG, the data site is used to upload data updates directly. In this implementation, it is not used for this purpose, but is still used to hold data which is updated externally (see **Data update process** below). 

### Staging site

The **staging site repository** controls a copy of the main SDG reporting site, intended for testing. 

The `develop` branch of the staging site respository serves from the `gh-pages` branch on that repository.

It deploys to the **staging site** at https://github.com/sustainabledevelopment-rwanda/sdg-site-rwanda. 

When changes are deployed to the data site, this automatically triggers the staging site to deploy. This takes around 5 more minutes. Thus, the data repository also indirectly deploys to the staging site. Direct changes to the staging site repository will also deploy in the same way, but it is not recommended to use this repository for most changes.

### Production site

The **production site repository** controls the production site. This is the main public site used for SDG reporting.

The `develop` branch of the production site respository serves from the `github-pages` branch on that repository.

It deploys to the **production site** at https://sustainabledevelopment-rwanda.github.io/.  

When changes to data are deployed to the data site, they are automatically applied to the production site. There is no specific deployment process involved, instead the production site pulls data directly from the data site. Since the data site deploys when changes are merged to the `develop` branch, users should be careful only to merge changes to the `develop` branch of the data repository when these are ready to go live on the production site. 

When changes are merged to the `master` branch of the production site, changes to metadata from the data repository are applied to the production site. Without this refresh, changes to metadata in the data repository will only go to the staging site. 

To change the layout or content of the production site aside from the data and metadata content, code can be edited directly in the production site repository; changes will then deploy to the production site directly.

# Data update process

This section describes how to update existing data series or add new data series to the SDG reporting site. 

You will need to have write permissions in this repository to update data.

Data for SDG reporting is mainained through three files in this repository:
- Excel file: [2025_RW-SDG_Data.xlsx](https://github.com/sustainabledevelopment-rwanda/sdg-data-rwanda/blob/develop/data/2025_RW-SDG_Data.xlsx) (in the folder "data")
- SDMX file: [2025_RWA-SDG_Data.xml](https://github.com/sustainabledevelopment-rwanda/sdg-data-rwanda/blob/develop/sdmx-data/2025_RWA-SDG_Data.xml) (in the folder "sdmx-data")
- DSD file: [RWA_2025_SDG DSD.xml](https://github.com/sustainabledevelopment-rwanda/sdg-data-rwanda/blob/develop/RWA_2025_SDG%20DSD.xml)

## Step 1: Clone and branch

Clone this data repository and create a new branch. If you are not familiar with how to do this, please see [The Git User's Manual](https://git-scm.com/docs/user-manual).

## Step 2: Update Excel

Find and open the **Excel file** in your cloned repository. Find the relevant line and add your updated data, then save the file. 

You should always use the version of the file saved in the cloned repository, rather than downloading a new local copy. This will ensure the Excel file in the repository is always up to date. 

## Step 3: Update DSD (new data series only)

If you are updating an existing data series, ignore this step and move on to step 4.

If you are creating a new data series, find and open the **DSD file** in your cloned repository. The DSD file is a template which links the ID codes in the Excel and SDMX files to specific indicators on the reporting site. 

Scrolling down, you will find many chunks of code describing specific indicators. Find the indicator your new data series belongs to, or, if it is a completely new indicator, find the previous indicator in numerical order. 

Once you have found the appropriate place, copy one of the code blocks and paste it where you want your new data series belongs. 

Change the following details to correspond to your new data series (you can look at other code chunks as a reference):
- Code id: This should correspond to the value in the Series_Code column of the Excel file.
- Indicator: This should be the indicator number your new data series belongs to.
- IndicatorCode: This is the same indicator number, formatted with "C" at the beginning, and 0s instead of decimal points.
- IndicatorTitle: This should correspond to the official title of the indicator your new data series belongs to.
- Name, Description: These should both correspond to the value in the Description column of the Excel file.

If you are adding multiple new data series, you can add multiple code blocks in the same way.

## Step 4: Convert to SDMX

For this step, you will need the updated **Excel file** and **DSD file**.

Conversion to SDMX is done using the [Eurostat SDMX Converter](https://cros.ec.europa.eu/dashboard/sdmx-converter). 

If you do not have an account on the European Union service platform, you will need to create one. You will also need to link your account with a two-factor authentication method. If you experience issues, try switching to a different browser, such as Chrome.

Once you have an account, click "Login" on the [Eurostat SDMX Converter](https://cros.ec.europa.eu/dashboard/sdmx-converter) page. 

When the converter opens, you will see a list of options.
- Under **Operation**, select Convert.
- Under **Input**, upload the Excel file. Some fields will automatically populate.
- Under **Output**, insert the file name you want for the final SDMX output. Unless you have a specific reason to change the file name, you should use the same file name as the existing SDMX file in the repository. If you use a new name, you will need to change the site code where it refers to the file.

Click "Next".

On the following page:
- Under **Structure type**, make sure DSD is selected.
- Under **Structure**, upload the DSD file by clicking "Select". Some fields will automatically populate.

Click "Next".

On the following page, under **Header configuration**, select **Manual Config**.

Click "Next". 

On the following page, there is no need to fill in any of the fields.

Click "Next". 

The conversion should now take place. On the page that appears, click on **Download Result**.

## Step 5: Upload SDMX

In your cloned repository, find the existing SDMX file, which will be in the folder "sdmx-data". Delete and replace this file with your new SDMX file downloaded in the previous step.

If you have changed the name of the file, remember to change the site code where it refers to the file.

## Step 6: Publish changes

In your code editor or using Git Bash, stage your changes, commit them, and publish them. 

Back on this GitHub repository, create a pull request with a descriptive message explaining which data series you are updating. 

You may wish to have a colleague review your changes before merging, as the changes will go live on the production site directly. 

Finally, merge the pull request. The changes will now be live on the repository and the deployment process will begin shortly, first to the data site and then to the staging site. The production site will be updated once the deployment to the data site is complete.

If you are not sure how to complete the actions described in this step, please see [The Git User's Manual](https://git-scm.com/docs/user-manual).

## Step 7: Update metadata

Once you have updated or added a data series, you will most likely need to update the metadata associated with the indicator. At the least, you may wish to change the last updated date to match your recent update. If you have added a new data series, you may need to fill in the metadata from scratch.

This repository contains a folder, "meta", which holds metadata files for all indicators. Editing these files will update the metadata on the staging site. Then, a merge to the `master` branch of the production site repository will deploy the updates to the production site.

You will need to have write permissions in the production site repository to update metadata on the production site.

# Contact

SDG reporting for Rwanda, including this repository, is managed by the [National Institute of Statistics of Rwanda (NISR)](https://statistics.gov.rw/). NISR can be contacted at [info@statistics.gov.rw](mailto:info@statistics.gov.rw).


