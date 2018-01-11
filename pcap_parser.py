import pyshark


def get_headers():
    return "avg_len,avg_interval,avg_ttl,avg_ack,avg_syn,avg_fin,outgoing_rate,category".split(',')


def parse(pcap_file):

    print("Parsing file:{}".format(pcap_file))
    cap = pyshark.FileCapture(pcap_file)

    # package info
    pkg_cnt = 0
    total_pkg_len = 0

    last_sniff_ts = None
    total_interval = 0

    # direction
    src_ip = None
    outgoing_cnt = 0

    # time to live
    total_ttl = 0

    # tcp flags
    # 0x10 ACK
    # 0x02 SYN
    # 0x01 FIN
    ack_key = 0x10
    syn_key = 0x02
    fin_key = 0x01

    total_ack = 0
    total_syn = 0
    total_fin = 0

    for pkg in cap:
        if pkg_cnt > 1000:
            break
        # get layers
        if "TCP" not in str(pkg.layers):
            print("tcp not found")
            continue

        eth, ip, tcp = pkg.eth, pkg.ip, pkg.tcp

        # increase package count
        pkg_cnt += 1
        total_pkg_len += int(pkg.length)

        # count package interval
        if last_sniff_ts is None:
            last_sniff_ts = float(pkg.sniff_timestamp)
        else:
            cur_sniff_ts = float(pkg.sniff_timestamp)
            total_interval += cur_sniff_ts - last_sniff_ts
            last_sniff_ts = cur_sniff_ts

        # count outgoing package
        if src_ip is None:
            src_ip = str(ip.src)
            outgoing_cnt = 1
        elif src_ip == str(ip.src):
            outgoing_cnt += 1

        # total time to live
        total_ttl += int(ip.ttl)

        # TCP flags
        tcp_flag = tcp.flags.hex_value
        if tcp_flag == ack_key:
            total_ack += 1
        elif tcp_flag == syn_key:
            total_syn += 1
        elif tcp_flag == fin_key:
            total_fin += 1

    if pkg_cnt < 2:
        print("Encounter Error with file:"+pcap_file)
        print("    Package count:{}".format(pkg_cnt))
        print("    Total package length:{}".format(total_pkg_len))
        print("    Total sniff time interval:{}".format(total_interval))
        print("    Total outgoing package count:{}".format(outgoing_cnt))
        return None

    avg_len = float(total_pkg_len)/pkg_cnt
    avg_interval = float(total_interval)/(pkg_cnt-1)
    avg_ttl = float(total_ttl)/pkg_cnt
    outgoing_rate = float(outgoing_cnt)/pkg_cnt
    avg_ack = float(total_ack)/pkg_cnt
    avg_syn = float(total_syn) / pkg_cnt
    avg_fin = float(total_fin) / pkg_cnt

    # print("    Package count:{}".format(pkg_cnt))
    # print("    Total package length:{}".format(total_pkg_len))
    # print("    Total sniff time interval:{}".format(total_interval))
    # print("    Total outgoing package count:{}".format(outgoing_cnt))
    # avg_len, avg_interval, avg_ttl, avg_ack, avg_syn, avg_fin, outgoing_rate
    return str(avg_len), str(avg_interval), str(avg_ttl), str(avg_ack), str(avg_syn), str(avg_fin), str(outgoing_rate)


def main():
    result = parse("test.pcap")
    print(result)

if __name__ == "__main__":
    main()
