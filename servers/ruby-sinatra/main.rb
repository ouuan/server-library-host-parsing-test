require 'sinatra/base'
require 'webrick'

class MyHTTPServer < Sinatra::Base
  configure do
    set :server, :webrick
    set :port, 3005
  end

  enable :sessions

  get '/' do
    headers['Connection'] = 'close'
    "[#{request.host}]"
  end
end

MyHTTPServer.run!
