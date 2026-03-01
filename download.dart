import 'dart:io';
import 'dart:convert';

Future<void> main() async {
  final process = await Process.start('python3', [
    '-u',
    'download.py',
  ], runInShell: true);

  process.stdout.transform(utf8.decoder).listen((data) => stdout.write(data));

  process.stderr.transform(utf8.decoder).listen((data) => stderr.write(data));

  stdin.transform(utf8.decoder).listen((data) {
    process.stdin.write(data);
  });

  final code = await process.exitCode;
  print('\nPython exited with code $code');
}
