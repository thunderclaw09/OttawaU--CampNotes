public class Data_Structures {
    public static void myFunc(int[] nums, int target)
    {
        for (int i = 0; i < nums.length; i++)
        {
            for (int j = i; j < nums.length; j++)
            {
                if (i != j)
                {
                    if (nums[i] + nums[j] == target)
                    {
                        System.out.println("(" + Integer.toString(i) + ", " + Integer.toString(j) + ")");
                    }
                }
            }
        }
    }


    public static void main(String[] args) 
    {
        // Enter code here. 
        int[] nums = {2, 7, 11, 15};
        int target = 9;

        myFunc(nums, target);
    }
}