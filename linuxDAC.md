Term,Description,Command Example,Permission Values
User,An individual account on the system with a unique UID (User ID).,useradd alice,N/A
Group,A collection of users that can share common access permissions, identified by a unique GID (Group ID).,groupadd developers,N/A
Owner,The user who owns the file. A file has one owner, typically the user who created it.,chown alice example.txt,N/A
Group (Owner),The group associated with the file. Files can belong to a group, and users in that group may share certain permissions.,chown :developers example.txt,N/A
Others,All other users who are neither the owner nor in the group.,N/A,N/A
Read (r),Permission to view the contents of a file or list a directory’s contents.,chmod u+r example.txt,4 (read permission)
Write (w),Permission to modify or delete the file, or add/remove files in a directory.,chmod g+w example.txt,2 (write permission)
Execute (x),Permission to run a file as a program or script, or search a directory.,chmod o+x example.txt,1 (execute permission)
Owner Permissions,The permissions granted to the file owner (user).,chmod u=rwx example.txt,7 (read, write, execute)
Group Permissions,The permissions granted to the group associated with the file.,chmod g=rw example.txt,6 (read, write)
Other Permissions,The permissions granted to users outside of the owner and group.,chmod o=r example.txt,4 (read)
Full Permissions Example,Example of full permissions for the owner, read/write for group, and read for others.,chmod 764 example.txt,7 (owner: read, write, execute)  6 (group: read, write)  4 (others: read)