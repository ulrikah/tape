MIDIClient.init // list names

~midiOut = MIDIOut.newByName("Arturia MicroFreak", "")

~dirt.soundLibrary.addMIDI(\freak, ~midiOut);

~midiOut.latency = 0.45;
