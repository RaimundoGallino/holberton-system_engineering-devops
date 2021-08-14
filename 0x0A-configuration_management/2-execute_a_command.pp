# execute the comand pkill

exec { 'pkill':
    command => '/usr/bin/pkill -15 killmenow',
}
 