# execute the comand pkill to terminate (-15) an specific process

exec { 'pkill':
  path => '/usr/bin/pkill -15 killmenow',

}
 