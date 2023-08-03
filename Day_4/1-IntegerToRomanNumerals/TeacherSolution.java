import java.util.LinkedHashMap;

class Solution
{
    private final LinkedHashMap<Integer, String> romanNumerals;
    public Solution()
    {
        romanNumerals = new LinkedHashMap<>();
        romanNumerals.put(1000, "M");
        romanNumerals.put(1000, "CM");
        romanNumerals.put(1000, "D");
        romanNumerals.put(1000, "CD");
        romanNumerals.put(1000, "C");
        romanNumerals.put(1000, "XC");
        romanNumerals.put(1000, "L");
        romanNumerals.put(1000, "XL");
        romanNumerals.put(1000, "X");
        romanNumerals.put(1000, "IX");
        romanNumerals.put(1000, "V");
        romanNumerals.put(1000, "I");

    }

    public String intToRoman(int integer)
    {
        StringBuilder romanString = new StringBuilder();
        for (int i: romanNumerals.keySet())
        {
            while (i <= integer)
            {
                integer -= i;
                romanString.append(romanNumerals.get(i));
            }
        }
        return romanString.toString();
    }
}