from marshmallow import fields, validate, Schema, post_load, validates_schema, ValidationError

LOWERS = tuple(chr(ch) for ch in range(ord('a'), ord('z') + 1))
UPPERS = tuple(chr(ch) for ch in range(ord('A'), ord('Z') + 1))
DIGITS = tuple(chr(ch) for ch in range(ord('0'), ord('9') + 1))
SYMBOLS = tuple('!@#$%^&*()_+[],./<>?;~')


class PasswordOptions:
    def __init__(
            self, 
            password_length: int, 
            lowers: bool, 
            uppers: bool,
            symbols: bool, 
            digits: bool
        ):

        self.password_length = password_length
        self.lowers = lowers
        self.uppers = uppers
        self.symbols = symbols
        self.digits = digits

        self.char_repos = tuple(
            repo
            for repo in (
                (self.lowers, LOWERS),
                (self.uppers, UPPERS),
                (self.symbols, SYMBOLS),
                (self.digits, DIGITS)
            )
            if repo[0]
        )
        self.all_chars = tuple(
            ch 
            for repo in self.char_repos 
            for ch in repo[1]
        )


class PasswordOptionsSchema(Schema):
    repo_validate = validate.Range(min=0)

    password_length = fields.Int(missing=12, validate=[validate.Range(min=6)])
    lowers = fields.Int(missing=1, validate=[repo_validate])
    uppers = fields.Int(missing=1, validate=[repo_validate])
    symbols = fields.Int(missing=1, validate=[repo_validate])
    digits = fields.Int(missing=1, validate=[repo_validate])

    @validates_schema
    def validate_password_length(self, data, **kwargs):
        min_password_length = sum(
            data[key]
            for key in (
                'lowers',
                'uppers',
                'symbols',
                'digits'
            )
        )

        l = data['password_length']
        if min_password_length > l:
            raise ValidationError(
                f'Minimum length ({min_password_length}) is greater than password length ({l})')

    @post_load
    def make_object(self, data, **kwargs):
        return PasswordOptions(**data)


password_options_schema = PasswordOptionsSchema()