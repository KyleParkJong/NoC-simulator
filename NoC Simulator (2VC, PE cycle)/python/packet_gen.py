def write(num_pck, mu, src, dst, vch, len):    
    if mu:
        lis = []
        for i in range(int(dst[-1])+1):
            if i in dst:
                lis.append(1)
            else:
                lis.append(0)
        lis.reverse()
        one_hot = "".join(map(str, lis))
        
        print(f'    $write("*** Send multicast (num_packets: {num_pck} src: {src} dst: {",".join(map(str,dst))} num_vch: {vch} len: {len}) *** \\n");')
        print(f"    send_packet_m_{src} ({num_pck}, 56'b{one_hot}, {vch}, {len});")
    else:
        print(f'    $write("*** Send unicast (num_packets: {num_pck} src: {src} dst: {dst[0]} num_vch: {vch} len: {len}) *** \\n");')
        print(f"    send_packet_u_{src} ({num_pck}, {dst[0]}, {vch}, {len});")
        

src = list(map(int, input("Initial source (split by space): ").split()))

for src0 in src:
    print(f"/* packet generator for n{src0} */")
    num_pck = int(input("Number of packet : "))
    mu = int(input("Multicast-1, Unicast-0 : "))
    dst = list(map(int, input("Destination (if mult, ascending order) : ").split()))
    vch = int(input("Number of vch : "))
    len = int(input("Packet length : "))
    
    print("initial begin")
    print("    #(STEP / 2);")
    print("    #(STEP * 10);")
    print("    while (~ready) begin")
    print("        #(STEP);")
    print("    end")
    print("")
    write(num_pck, mu, src0, dst, vch, len)
    print("end")
    print("")
    
