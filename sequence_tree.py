class String
  def look_and_say_regexp
    self.gsub(/(.)\1*/) { |match| "#{match.size}#{match[0]}" }
  end

  def look_and_say_chunk
    self.chars.chunk { |c| c }.map { |c, arr| [arr.size, c] }.join
  end

  def look_and_say_manual
    cluster = []
    self.each_char do |c|
      if cluster.last && cluster.last.last == c
        cluster.last << c
      else
        cluster << [c]
      end
    end

    cluster.map { |e| [e.size, e.last] }.join
  end
end


puts "look_and_say_regexp"
puts s = '1'
10.times { puts s = s.look_and_say_regexp }
puts "================================"

puts "look_and_say_chunk"
puts s = '1'
10.times { puts s = s.look_and_say_chunk }
puts "================================"

puts "look_and_say_manual"
puts s = '1'
10.times { puts s = s.look_and_say_manual }
puts "================================"