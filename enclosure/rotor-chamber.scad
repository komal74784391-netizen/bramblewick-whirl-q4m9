// Whirl rotor chamber
$fn = 96;

chamber_outer = 74;
chamber_height = 52;

difference() {
    cylinder(h = chamber_height, d = chamber_outer, center = true);
    translate([0, 0, 2])
        cylinder(h = chamber_height, d = 62, center = true);
}
translate([0, 0, chamber_height / 2 - 2])
    cube([14, 10, 4], center = true);
