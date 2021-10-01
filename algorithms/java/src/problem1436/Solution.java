package problem1436;

import java.util.HashSet;
import java.util.List;
import java.util.Set;

/**
 * @author Xavier Li
 */
public class Solution {

    /**
     * 哈希表
     */
    public String destCity(List<List<String>> paths) {
        Set<String> cityA = new HashSet<>(paths.size());
        for (List<String> path : paths) {
            cityA.add(path.get(0));
        }
        for (List<String> path : paths) {
            if (!cityA.contains(path.get(1))) {
                return path.get(1);
            }
        }
        return null;
    }
}