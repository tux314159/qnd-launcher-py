def parsedesktop(files):
    progs = []
    for cfilepath in files:
        with open(cfilepath, "r") as cfile:
            # Check if this is a valid Desktop file...
            cline = cfile.readline().strip()
            while cline[0] == "#" or cline[0] == "":
                cline = cfile.readline().strip()
            if cline != "[Desktop Entry]":
                continue  # if not, don't bother parsing

            # Look for keys
            cline = "_"
            cname = ""
            namep = False
            ccomment = ""
            commentp = False
            cexec = ""
            execp = False
            cterminal = ""
            terminalp = False
            while cline:
                cline = cfile.readline()
                if cline[:5] == "Name=" and not namep:
                    cname = cline[5:]
                    namep = True
                if cline[:8] == "Comment=" and not commentp:
                    ccomment = cline[8:]
                    commentp = True
                if cline[:5] == "Exec=" and not execp:
                    cexec = cline[5:]
                    execp = True
                if cline[:9] == "Terminal=" and not terminalp:
                    cterminal = cline[9:]
                    terminalp = True

            # Get rid of these things
            for c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
                cexec = cexec.replace("%" + c, "")
            # Finally, put them into progs, but only if it has a name!
            if cname.strip() != "":
                progs.append(
                    (cname.strip(), ccomment.strip(), cexec.strip(), cterminal.strip())
                )

    return sorted(progs)
