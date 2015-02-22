echo $(($(head -n1 rosalind_tree\ \(1\).txt) - $(wc -l rosalind_tree\ \(1\).txt | awk '{print $1}')))
