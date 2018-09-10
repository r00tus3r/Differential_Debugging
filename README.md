# Differential Debugging

I tried to find the sorting algorithms used in `ls` command in linux and Mac OS by reverse engineering it. While trying it, I learnt about differential debugging. That was a while back, I was doing it just for fun. I might publish a detailed blog on the same sometime later. This method is really useful when debugging large binaries.

Briefly there are two steps in differential debugging. The first one is to get a trace of the instructions being executed and the second step is to mark the same instructions in the disassembly. This enables you to focus on the only parts required.

Since we only need the instruction trace, I wrote a small GDB script. You can use tools like PIN or r2 as well to get the same. Put a breakpoint at start address i.e. the address from which you want to start the trace. Run a loop till the end address, single stepping each instruction. The output will be logged into the file out.

```
define func
    b *0x401150
    set disassembly-flavor intel
    set pagination off
    set logging file out
    set logging on
    r
    while $rip != 0x4011CF
        si
        x/i $rip
    end
end
```

After that, I used python to get only the addresses of the instructions from the log file. I wrote a for loop for saving only the addresses into another file named trace.

```
f = open("out", "r")
data = f.readlines()
w = open("trace", "w")

for i in data:
    for j in i.split():
        if '0x4' in j:
            try:
                int(j.strip(':'), 16)
            except:
                continue
            w.write(j.strip(':') + '\n')

```

In the end, exported those addresses to IDA using the following IDAPython script and colored the instructions executed.

```
f = open("trace", "r")
addr = f.readlines()

for i in addr:
     SetColor(int(i, 16), CIC_ITEM, 0x0000ff)

```

Done. Now, I only need to focus on the colored instructions in the disassembly. The CFG will look something like the following image.
[[https://github.com/r00tus3r/Differential_Debugging/blob/master/CFG.PNG]]

I hope this helps!
