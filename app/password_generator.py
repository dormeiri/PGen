from random import randrange
from password_options import PasswordOptions


class PasswordGenerator:
    def __init__(self, opts: PasswordOptions):
        self.opts = opts
        

    def generate(self):
        s = ''

        for repo in self.opts.char_repos:
            for i in range(repo[0]):
                s += self.rand_char(repo[1])

        for i in range(len(s), self.opts.length):
            s += self.rand_char(self.opts.all_chars)

        password = self.shuffle(s)

        return password

    def shuffle(self, s):
        shuffled_s = ''

        while s:
            ch_idx = randrange(len(s))
            shuffled_s += s[ch_idx]
            s = s[:ch_idx] + s[ch_idx + 1:]
        
        return shuffled_s

    def rand_char(self, repo):
        char_idx = randrange(0, len(repo))
        char = repo[char_idx]

        return char


    def rand_repo(self):
        repos = self.opts.char_repos
        repo_idx = randrange(0, len(repos))
        repo = repos[repo_idx]

        return repo
        
