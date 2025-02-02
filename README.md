<div align="center">

# ZFS Bookmark

![badge](https://badgen.net/badge/version/v1.0.0/orange?style=flat-square)
![badge](https://badgen.net/badge/platform/Linux/green?style=flat-square)
![badge](https://badgen.net/badge/Python/3.12/yellow?style=flat-square)

<p align = "center">
  <img width="300px" src="https://github.com/user-attachments/assets/e251ee70-9d65-4bb8-91ff-a81e1ff00928">
</p>

A simple script to bookmark all existing snapshots matching some pattern

</div>

# How to Use

These setup steps are for a TrueNAS Scale system, as the script requires [py-libzfs](https://github.com/truenas/py-libzfs).

### 1. Create a user

- Follow the steps in the [TrueNAS documentation](https://www.truenas.com/docs/scale/scaletutorials/credentials/managelocalusersscale/#creating-user-accounts)
to create a new user called "bookmark-user"
- Run `sudo zfs allow -u bookmark-user bookmark pool_name`, replacing `pool_name` with your actual pool name. This gives our new user the ability to manage bookmarks.

### 2. Download the script

Download the Python script and place it wherever you like. Then run `chmod +x bookmark_all.py` to make it executable.

### 3. Run the script automatically

Following the cron steps in the [TrueNAS documentation](https://www.truenas.com/docs/scale/scaletutorials/systemsettings/advanced/managecronjobsscale/)
to create a job with the folling parameters:

- Description: `Bookmark all snapshots matching some pattern`
- Command: `/path/to/script/bookmark_all.py pattern`
  - replace the path and pattern with the correct values
- Run As User: `bookmark-user`
- Schedule: `Monthly`
  - This should be less than the lifetime of your snapshots to guarentee we capture them all
- Hide Standard Output: `Unchecked`
- Hide Standard Error: `Unchecked`
  - This setting and the previous setting can be checked if you don't want to recieve status emails
- Enabled: `Checked`
