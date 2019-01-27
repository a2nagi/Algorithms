int firstMissingPositive(vector<int>& nums) {
        for (int i=0;i<nums.size(); i++)
        {
            while(nums[i] > 0 && nums[i] <= nums.size() && nums[nums[i] - 1] != nums[i])
            {
                int temp = nums[i];
                nums[i] = nums[nums[i]-1];
                nums[nums[i]-1] = temp;
            }
        }
        
        for(int m =0; m<nums.size();m++)
        {
            cout<<nums[m]<<endl;
        }
        
        for (int j=0; j<nums.size(); j++)
        {
            if (nums[j] != j+1)
            {
                return j+1;
            }
        }
        return nums.size()+1;
        
    }
