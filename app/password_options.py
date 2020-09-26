from marshmallow import fields, validate, Schema, post_load, validates_schema, ValidationError

LOWERS = tuple(chr(ch) for ch in range(ord('a'), ord('z') + 1))
UPPERS = tuple(chr(ch) for ch in range(ord('A'), ord('Z') + 1))
DIGITS = tuple(chr(ch) for ch in range(ord('0'), ord('9') + 1))
SYMBOLS = tuple('!@#$%^&*()_+[],./<>?;~')


class PasswordOptions:
    def __init__(
            self, 
            length: int, 
            lowers: bool, 
            uppers: bool,
            symbols: bool, 
            digits: bool
        ):

        self.length = length
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

    length = fields.Int(missing=12, validate=[validate.Range(min=6)])
    lowers = fields.Int(missing=1, validate=[repo_validate])
    uppers = fields.Int(missing=1, validate=[repo_validate])
    symbols = fields.Int(missing=1, validate=[repo_validate])
    digits = fields.Int(missing=1, validate=[repo_validate])

    @validates_schema
    def validate_length(self, data, **kwargs):
        min_length = sum(
            data[key]
            for key in (
                'lowers',
                'uppers',
                'symbols',
                'digits'
            )
        )

        l = data['length']
        if min_length > l:
            raise ValidationError(
                f'sum of min length per charcter type ({min_length}) is lower than length ({l})')

    @post_load
    def make_object(self, data, **kwargs):
        return PasswordOptions(**data)


password_options_schema = PasswordOptionsSchema()