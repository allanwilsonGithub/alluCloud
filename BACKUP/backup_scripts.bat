mysqldump -u root -palluCloudPassword booksdb authors categories formats titles rel_title_author series > D:\ALLUSTORE\alluCloud\BACKUP\book\booksback.sql
mysqldump -u root -palluCloudPassword filmdb titles > D:\ALLUSTORE\alluCloud\BACKUP\film\filmback.sql
mysqldump -u root -palluCloudPassword webdb searchstrings urls > D:\ALLUSTORE\alluCloud\BACKUP\web\webback.sql
mysqldump -u root -palluCloudPassword eventdb events eventtypes > D:\ALLUSTORE\alluCloud\BACKUP\event\eventback.sql
mysqldump -u root -palluCloudPassword dashdb configuration_items > D:\ALLUSTORE\alluCloud\BACKUP\dash\dashback.sql
mysqldump -u root -palluCloudPassword notedb notes > D:\ALLUSTORE\alluCloud\BACKUP\note\noteback.sql
D:\ALLUSTORE\alluCloud\BACKUP\backup.py