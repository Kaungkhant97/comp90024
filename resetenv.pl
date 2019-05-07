use strict;
use warnings;

my @pids = qx(ps -C bash -o pid=);
my $foo  = $ARGV[0];
print "changing user to $foo";
print @pids;

open( my $gdb, "|gdb" ) || die "$! gdb";
select($gdb);
$|++;
for my $pid ( @pids ) {
    print "attach $pid\n";
    sleep 1;
    print 'call bind_variable("USER","' . $foo . '",0)' . "\n";
    sleep 1;
    print "detach\n";
}
