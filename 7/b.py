from helper import GroupsParser, flatten, stdin
import re
from pprint import pprint


if __name__ == "__main__":
    res = 0
    cwd = None
    files = dict()
    dirs = dict()
    all_dirs = set([""])
    space_used = 0
    for line in stdin:
        if (m := re.match("^\\$ cd (.*)$", line)) is not None:
            dir_change = m.group(1)
            if dir_change == "/":
                cwd = [""]
            elif dir_change == '..':
                cwd.pop()
            else:
                cwd.append(dir_change)
        elif (m := re.match("^\\$ ls$", line)) is not None:
            pass
        elif (m := re.match("dir (.*)$", line)) is not None:
            child_name = m.group(1)
            child = "/".join(cwd + [child_name])
            cur_dirs = dirs.get("/".join(cwd), [])
            cur_dirs.append(child)
            dirs["/".join(cwd)] = cur_dirs
            all_dirs.add(child)
        elif (m := re.match("(\\d*) (.*)$", line)) is not None:
            size = int(m.group(1))
            cur_files = files.get("/".join(cwd), [])
            # bug: could possibly add same file twice
            cur_files.append(size)
            space_used += size
            files["/".join(cwd)] = cur_files
        else:
            print(f"Unable to match: {line}")
            assert False
    space_needed = space_used - 40000000
    print(space_needed)
    best_size = space_used
    best = ""

    def process(path):
        global best_size, best
        cur_dirs = dirs.get(path, [])
        cur_files = files.get(path, [])
        size = 0
        size += sum([process(child_dir) for child_dir in cur_dirs])
        size += sum(cur_files)
        print(path, size)
        if size >= space_needed and size < best_size:
            best_size = size
            best = path
        return size
    process("")
    print(best, best_size)
