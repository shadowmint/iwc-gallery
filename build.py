#!/usr/local/bin/python
import ruff
import ruffx.utility
import ruffx.command
import ruffx.typescript
import ruffx.sass
import ruffx.npm


# Paths
base = ruff.path(__file__, __file__)


## Common libraries
def libs():

  # Clean
  #build = ruff.build()
  #build.depend(ruffx.utility.clean(base, ['public', 'css'], ['.*\.css$']))
  #build.depend(ruffx.utility.clean(base, ['public', 'js'], ['.*\.ts$', '.*\.js$']))
  #build.chdir(ruff.path(__file__))
  #build.execute()

  # Sass
  #ruffx.sass.compile(base, ['public', 'css', 'styles.scss.css'], ['src', 'css', 'styles.scss'])

  # Typescript
  #ruffx.typescript.compile(base, ['public', 'js', 'dsync.js'], ['src', 'demo', 'deps', 'dsync.ts'], source_folder=['lib', 'dsync', 'src'])
  #ruffx.typescript.compile(base, ['public', 'js', 'xn.js'],    ['src', 'demo', 'deps', 'xn.ts'],    source_folder=['lib', 'xn', 'src', 'xn'])
  #ruffx.typescript.compile(base, ['public', 'js', 'live.js'],  ['src', 'demo', 'deps', 'live.ts'],  source_folder=['lib', 'live', 'src', 'live'])
  #ruffx.typescript.compile(base, ['public', 'js', 'syn.js'],   ['src', 'demo', 'deps', 'syn.ts'],   source_folder=['lib', 'live', 'src', 'syn'])
  #ruffx.typescript.compile(base, ['public', 'js', 'z3d.js'],   ['src', 'demo', 'deps', 'z3d.ts'],   source_folder=['lib', 'zgl', 'src', 'z3d'])
  #ruffx.typescript.compile(base, ['public', 'js', 'demo.js'],  ['src', 'demo', '__init__.ts'])

  # Tests
  #ruffx.typescript.test(base, ['public', 'js', 'tests.js'], ['src', 'tests', '__init__.ts'])
  pass


## Serve content for dev
def server(build=False):

  # Npm
  ruffx.npm.install(base)

  # Republish dependencies
  ruffx.npm.bower_publish(base, ['public', 'js', 'libs'], ['platform.js'])

  # Common libraries
  libs()

  # Start a local server
  ruff.serve('0.0.0.0', 3001, ruff.path(__file__, 'public'))

  # Watch for changes
  ruff.run(build=build)


if __name__ == '__main__':
  ruffx.command.register('rebuild', lambda: server(True))
  ruffx.command.register('server', server)
  ruffx.command.register('default', 'rebuild')
  ruffx.command.run()
