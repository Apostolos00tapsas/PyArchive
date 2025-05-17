<!DOCTYPE html>
<html>
<body>

<?php
class Node {
  // Properties
  public $id;
  public $hash;
  public $next_hush;
  public $prev_hush;

  // Methods
  function set_node($id,$hash,$next,$prev) {
    $this->id = $id;
    $this->hash = $hash;
    $this->next_hush = $next;
    $this->prev_hush = $prev;
  }
  function get_node() {
    print $this->id ."\n".  $this->hash ."\n". $this->next_hush ."\n". $this->prev_hush;
  }
}

$nd1 = new Node();
$nd1->set_node('23as1d68a4d2a1d56a4d68a1d56a1d56a','odkasdjapodapodsoapd0adsjada5sd2ad02a1d56qw4q','-1','-1');

echo $nd1->get_node();
?>
 
</body>
</html>