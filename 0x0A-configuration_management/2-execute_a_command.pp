# execute the comand pkill to terminate (-15) process

exec { 'pkill':
    command => '/usr/bin/pkill -15 killmenow',
}
 