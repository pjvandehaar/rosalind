echo $(($(head -n1 rosalind_tree.txt) - $(wc -l rosalind_tree.txt | awk '{print $1}')))
