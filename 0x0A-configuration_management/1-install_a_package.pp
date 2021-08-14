#install puppet-lint

package { 'puppet-lint':
{
    ensure          => 'present',
    install_options => [ '-v 2.1.1' ]

}
