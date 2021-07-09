#!/usr/bin/knife exec

##
# Dump a JSON representation of Chef client config
# Use configure third-party REST API clients, for example Py3Chef
# :D
##
require 'chef/application/client'
require 'json'

# Initialize a new Chef client instance
client = Chef::Application::Client.new
# Set Chef::Config instance variables
client.configure_chef
# Write JSON to STDOUT
puts JSON.pretty_generate(Chef::Config.configuration)


## If you ever need to debug this app, uncomment the following line(s)
## Create breakpoint
# require 'pry'; binding.pry

## Inspect Chef::Application::Client instance
# client.inspect
#
## Inspect Chef::Config configuration state
# Chef::Config.configration

## Inspect other Chef::Config instance variables (state loaded by client.configure_chef)
# Chef::Config.instance_variables

## Inspect the knife executable to get a full picture by running `vim $(which knife)`
## $cat $(which knife)
#!/opt/chef/embedded/bin/ruby --disable-gems
#--APP_BUNDLER_BINSTUB_FORMAT_VERSION=1--
# ENV["GEM_HOME"] = ENV["GEM_PATH"] = nil unless ENV["APPBUNDLER_ALLOW_RVM"] == "true"
# require "rubygems"
# ::Gem.clear_paths

# <gem pins ommitted for brevity>
# gem "chef", "= 12.22.5"

# spec = Gem::Specification.find_by_name("chef", "= 12.22.5")
# bin_file = spec.bin_file("knife")
# Kernel.load(bin_file)
