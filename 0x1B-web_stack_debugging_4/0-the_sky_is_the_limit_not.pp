# Setting upper limit for the pinging requests
exec { 'upperlimit' :
     command =>  'sed -r -i "s/(ULIMIT =\"-n) [0-9]+/\1 10000" /etc/default/nginx; service nginx restart',
     path    =>  '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games',
     onlyif  =>  'test -e /etc/default/nginx',
}
