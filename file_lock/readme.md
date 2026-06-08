[[_TOC_]]]

# About

How to lock a file in Python? **Short answer** - you follow different approaches depending on the underlying operating system

# Lessons learnt

You can place a lock on a file using msvcrt. You can read/write to the file. However, you cannot move/delete the file it is locked. You will have to come out of the `open` block or explicitly unlock using msvcrt to do the move/delete operation

# Next steps

We know we cannot delete/move while file is locked. Can we copy the contents to a file with the same name in another directory? And erase the contents while the file handle is still open. Thus we get a file whic his zero bytes in length,i.e. not much of any significance
