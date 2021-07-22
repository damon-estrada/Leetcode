class Solution {
    public List<String> findRepeatedDnaSequences(String s) {

        HashSet<String> seqs = new HashSet<>();
        HashSet<String> repeats = new HashSet<>();

        int maxSeqLen = 10;
        String seq;

        // We want to loop until our last check includes the last character in the s string.
        for (int i = 0; i + maxSeqLen <= s.length(); i++) {
            seq = s.substring(i, i + maxSeqLen); // get the sub-sequence from now until 10 from now
            if (seqs.contains(seq))
                repeats.add(seq); // If we have seen this sequence before.
            else
                seqs.add(seq); // add sequence to the map for future checking.
        }

        return new ArrayList<String>(repeats);
    }
}