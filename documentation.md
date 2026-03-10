glow its a programing language made in python, and this is glow documentation.

on the terminal:

    use the command "glow -ver" to see the version of glow.

    use the command "glow build" to run a .glow archive, example:
        glow build program.glow

on the glow archive:
    use the command "terminal.output" to write any thing on terminal, example:
        terminal.output "hello, world"
        result:
        hello, world
    
    use the command "var" to create a variable, example:
        var game = "minecraft"
        terminal.output game
        result:
        minecraft

    use the command "terminal.input" to ask any thing on terminal, example:
        var word = terminal.input "say any thing"
        terminal.output word
        result:
        say any thing: <the word>
        you sayed <the word>