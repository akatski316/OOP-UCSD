import java.util.*;
public class PrimitiveCalculator
{
	private static List<Integer> optimal_sequence(int n)
{        List<Integer> sequence = new ArrayList<Integer>();               
			if(n == 1){
				sequence.add(n);
				return sequence;
				}
			int i ,j;
			int[][] d = new int[n + 1][2];
			d[1][1] = 1;
			d[1][0] = 1;
			d[2][0] = 1;
			d[2][1] = 1;
			d[3][1] = 1;
			d[3][0] = 1;
			int[] a = new int[4];
			a[0] = 0;
			for(i = 4;i <= n;i++)
			{
				for(j = 1;j <= 3;j++)
				{
					 if(j == 1)
					 {
						 a[j] = d[i - 1][0] + 1;
					 }
					 else if(i % j == 0)
					 {
						 a[j] = d[i/j][0] + 1;
					 }
					 else 
                     a[j] = 1000000;
				}
				d[i][0] = Math.min(Math.min(a[1],a[2]),a[3]);                    //takes all three possibilities in array a
				  d[i][1] = i;
				  if(d[i][0] == a[1])
					  d[i][1] = i - 1;
				  else if(d[i][0] == a[2])
				  {
					  d[i][1] = i/2;
				  }
				  else
				  {
					  d[i][1] = i/3;
				  }
		   }
			sequence.add(n); 
			i = n;
			while(i > 1){
				sequence.add(d[i][1]);
				i = d[i][1];
				}
			Collections.reverse(sequence);
			return sequence;
}
	
	 public static void main(String[] args)
	 {
		 Scanner scanner = new Scanner(System.in);
		 int n = scanner.nextInt();
		 List<Integer> sequence = optimal_sequence(n);
		 System.out.println(sequence.size() - 1);
		 for (Integer x : sequence)
		 {
			 System.out.print(x + " ");
	   	 }
		 
	 }
			
}
