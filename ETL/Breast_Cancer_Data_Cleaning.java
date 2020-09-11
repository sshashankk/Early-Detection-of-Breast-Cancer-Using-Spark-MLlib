import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class Breast_Cancer_Data_Cleaning {

	public static void main(String[] args) throws Exception{
		if (args.length != 2) {
			System.err.println("Invalid Input. Please try again.");
			System.exit(0);
		}
		else {
			//Making use of only mapper function since we only need to drop a column for ETL and Cleaning
			Job job = new Job();
			job.setJarByClass(Breast_Cancer_Data_Cleaning.class);
			job.setJobName("Breast_Cancer_Data_Cleaning");
			FileInputFormat.addInputPath(job,new Path(args[0]));
			FileOutputFormat.setOutputPath(job,new Path(args[1]));
			job.setMapperClass(BCD_Mapper.class);
			job.setNumReduceTasks(0);
			job.setOutputKeyClass(Text.class);
	        job.setOutputValueClass(Text.class);
	        job.setNumReduceTasks(1);
	        System.exit(job.waitForCompletion(true) ? 0 : 1);
			}
	}
}