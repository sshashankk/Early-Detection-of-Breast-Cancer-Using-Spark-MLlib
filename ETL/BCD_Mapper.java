import java.lang.*;
import java.util.ArrayList;
import java.util.List;
import java.io.IOException;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class BCD_Mapper extends Mapper<LongWritable, Text, Text, Text> {

        private static final String Blank = " ";
        @Override
        public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {

        String line = value.toString();
        String k=" ";
        String[] features = null;
        List<String> val =new ArrayList<>();
        features=line.split(",");
        k = features[31];
        String delimiter=",";
        int len=features.length;
        String concat="";
       
        for(String feature:features)
        {
           concat=feature.concat(delimiter);
           val.add(concat);
        }
        
        String result="";
        
        for (int i = 1 ; i <=31 ; i++) {
            
        	result = result + features[i];

        }
        
        if (result != Blank)
        {
             context.write(new Text(), new Text(result));
        }
    }
}
