#include <assert.h>
#include <sstream>
#include <unordered_map>
#include <fstream>
#include <iostream>
#include <vector>
#include <set>

using namespace std;
typedef unordered_map<string, string> stringmap;

string get_complement(string str) {
  static unordered_map<char, char> bp({{'A','T'}, {'T','A'}, {'C','G'}, {'G','C'}});
  ostringstream comp;
  for (int i = str.length() - 1; i >= 0; i--) {
    comp << bp[str[i]];
  }
  return comp.str();
}

void insert_orfs(set<string> &orfs, stringmap aa_by_codon, const string seq) {
  // check for ORF at any pos on forward strand
  for (int start = 0; start < seq.length() - 2; start++) { // note fenceposts!
    if (seq.substr(start, 3) == "ATG") {
      ostringstream cur_prot("M");
      for (int pos = start+3; pos < seq.length() - 2; pos+=3) {
        string aa = aa_by_codon[seq.substr(pos, 3)];
        if (aa == "Stop") {
          orfs.insert(cur_prot.str());
          break;
        }
        cur_prot << aa;
      }
    }
  }
}

string get_seq_from_stdin() {
  string line;
  ostringstream seq_ss;
  while (getline(cin, line))
    if (line[0] != '>')
      seq_ss << line;
  return seq_ss.str();
}

stringmap get_aa_by_codon_map() {
  ifstream codon_f("codon-table.txt");
  string bases, aa;
  stringmap aa_by_codon;
  while (codon_f >> bases >> aa)
    aa_by_codon[bases] = aa;
  return aa_by_codon;
}

int main() {
  stringmap aa_by_codon = get_aa_by_codon_map();
  string seq = get_seq_from_stdin();

  set<string> orfs;
  insert_orfs(orfs, aa_by_codon, seq);
  seq = get_complement(seq);
  insert_orfs(orfs, aa_by_codon, seq);

  for (auto it = orfs.begin(); it != orfs.end(); ++it){
    cout << *it << endl; // Note the "*" here
  }

  return 0;
}
