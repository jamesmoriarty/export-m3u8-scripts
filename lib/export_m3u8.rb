require 'pathname'
require 'fileutils'

if not Pathname.new(ARGV[0]).exist?
  puts "m3u8 file not found!"
  puts "usage: #{__FILE__} path/to/playlist.m3u8"
  exit(1)
end

playlist_path   = ARGV[0]
playlist_name   = File.basename(playlist_path, ".*")

folder_path     = File.join(Dir.pwd, playlist_name)
FileUtils.mkdir_p(folder_path)

IO.read(playlist_path).split("\r").each_with_index do |file_path, index|
  next unless Pathname.new(file_path).exist?

  file_name = "#{index} " + File.basename(file_path)
  puts "Copying... #{file_name}"
  FileUtils.cp(file_path, File.join(folder_path, file_name))
end

puts "Finished."
