#There is a string of size n containing only 'A' and 'O'. 'A' stands for Apple, and 'O' stands for Orange. We have m number of spells, each spell allows us to convert an orange into an apple.
#Find the longest sequence of apples you can make, given a string and the value of m.

class Solution:
    def appleSequences(self, n, m, arr):
        # code here 
        st=0;
        end=0;
        ans=0;
        while(end!=n):
            if(m>0):
                if(arr[end]=='O'):
                    m-=1;
            else:
                if(arr[end]=='O'):
                    while(arr[st]!='O'):
                        st+=1;
                    st+=1;       
            ans=max(ans,end-st+1);
            end+=1;
        return ans;
