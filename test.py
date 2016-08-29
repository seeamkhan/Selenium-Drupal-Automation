# l = 3
# for count in range(0,l):
# 	for i in range(count,l):
# 	  for j in range(count,i+1):
# 	    print [j],
# 	  print

# for test1 in xrange(3):
# 	# print "output test1"
# 	for test2 in xrange(test1+1):
# 		print "output test2"
# 		for test3 in xrange(test2+1):
# 			print "output test3"

#PHP code
# $str_arr = array('P', 'E', 'N', 'D');
# for($i = 0; $i < count($str_arr); $i++){
#  $index = array();
#  for($j = $i; $j < count($str_arr); $j++){
#   $index[] = $j;
#   $output = '';
#   for( $k = 0; $k < count($index); $k++ ){
#    $output .= $str_arr[$index[$k]];
#   }
#   echo $output."<br/>";
#  }
# }

l = 3
for count in range(0,l):
	for i in range(count,l):
		x = []
		for j in range(count,i+1):
			x.append(j)
		print x
