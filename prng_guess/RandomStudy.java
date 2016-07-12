import java.util.*;

public class RandomStudy {

	// public boolean 
	private static class TimeRange {
		public long start;
		public long end;

		public long getStart() {
			return start;
		}

		public void setStart(long startValue) {
			start = startValue;
		}

		public long getEnd() {
			return end;
		}

		public void setEnd(long endValue) {
			end = endValue;
		}
		
		public TimeRange(long start, long end) {
			setStart(start);
			setEnd(end);
		}
	}

	public static void main(String[] args) {

		// Random r = new Random(1374037200);
		// long start = 1374037200;
		// long end = 1374123600;

		List<Integer> knownList = new ArrayList<Integer>();
		knownList.add(643);
		knownList.add(953);
		knownList.add(522);
		knownList.add(277);
		knownList.add(464);
		knownList.add(366);
		knownList.add(321);
		knownList.add(409);
		knownList.add(227);
		knownList.add(702);

		Long start = Long.parseLong(args[0]);
		Long end = Long.parseLong(args[1]);

		TimeRange tr = new TimeRange(start, end);

		long diff = tr.getEnd() - tr.getStart();

		Random r = null;
		List<Integer> outputList = null;
		Long timestamp = null;
		Boolean foundTimestamp = false;
		for (int i = 0; i <= diff; i++) {
			if (!foundTimestamp) {
				Boolean go = false;
				if (i % 10000 == 0) {
					go = true;
					System.out.println(start + i);
				}
	
				r = new Random(start + i);
				// outputList = new ArrayList<Integer>();
				Boolean match = true;
				for (int j = 0; j < 10; j++){
					// outputList.add(r.nextInt(1000));
					if (match) {
						Integer nextInt = r.nextInt(1000);
						if (!(knownList.get(j).equals(nextInt))) {
							// if (go) {
							// 	System.out.println("j");
							// 	System.out.println(j);
							// 	System.out.println("knownList.get(j)");
							// 	System.out.println(knownList.get(j));
							// 	System.out.println("nextInt");
							// 	System.out.println(nextInt);
							// }
							match = false;
						}
					}
				}
				if (match) {
					// System.out.println("Made it?");
					foundTimestamp = true;
					timestamp = start + i;
				}
			}
		}

		if (foundTimestamp){
			System.out.println("timestamp");
			System.out.println(timestamp);
		}
		// 1374123600

		// for (int i = 0; i < 20; i++) {
		// 	System.out.println(r.nextInt(1000));
		// }
	}
}