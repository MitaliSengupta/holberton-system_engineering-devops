# script to kill process
exec {'killmenow':
  command => '/usr/bin/pkill -f killmenow'
  }
