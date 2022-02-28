reset;

set port;
set vessel;

param c {port,vessel} >= 0;

param sp {port} >= 0;

param cp {port} >= 0;

param kv {vessel} >= 0;

param cv {vessel} >= 0;

param d >= 0;

var x {port,vessel} >= 0;

var k {port,vessel} binary;

var y {port} binary;

var z {vessel} binary;

minimize total_cost:
sum {i in port, j in vessel} c[i,j] * x[i,j] + sum {i  in port} cp[i] * y[i] + sum {i in vessel} cv[i] *  z[i];

subject to demand: sum {i in port, j in vessel} x[i,j] = d;

subject to supply {i in port}: sum {j in vessel} x[i,j] <= sp[i];

subject to capacity {j in vessel}: sum {i in port} x[i,j] <= kv[j];

subject to max_ports {j in vessel}: sum {i in port} k[i,j] <= 2;

subject to port_vessel_combo {i in port, j in vessel}: x[i,j] - k[i,j] * kv[j] <= 0;

subject to fixed_cost_port {i in port, j in vessel}: x[i,j] - y[i] * sp[i] <= 0;

subject to fixed_cost_vessel {i in port, j in vessel}: x[i,j] - z[j] * kv[j] <= 0;