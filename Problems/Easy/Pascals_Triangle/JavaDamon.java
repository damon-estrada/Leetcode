package Easy.Pascals_Triangle;

import java.util.ArrayList;
import java.util.List;

public class JavaDamon {
    public List<List<Integer>> generate(int numRows) {

        List<List<Integer>> allLevels = new ArrayList<>();
        // add the first row of the triangle
        allLevels.add(new ArrayList());
        allLevels.get(0).add(1);

        // THis method holds two poiters. One to the current level and one to the last level
        for (int curLvl = 1; curLvl < numRows; curLvl++) {
            List<Integer> level = new ArrayList<>();
            // always add one to the current level
            level.add(1);

            List<Integer> lstLvl = allLevels.get(curLvl - 1);

            for (int lvlElms = 1; lvlElms < curLvl; lvlElms++)
                // add the last level's element - 1 (*) and the lst lvl element (^) together to get lvlElm next.
                /*
                    1
                    * ^
                    1 1
                    * ^
                    1 2 1
                     (*^)
                    1 3 3 1
                       (*^)
                    1 4 6 4 1

                */
                level.add(lstLvl.get(lvlElms - 1) + lstLvl.get(lvlElms));

            // last lvl element is 1
            level.add(1);

            allLevels.add(level);
        }

        System.out.println(allLevels);

        return allLevels;
    }
}
