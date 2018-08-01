# create file in /tmp
file { '/tmp/holberton':
  owner   => www-data,
  group   => www-data,
  mode    => '0744',
  content => 'I love Puppet'
  }
