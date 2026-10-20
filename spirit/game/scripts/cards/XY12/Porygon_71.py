from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.passives import Passive, carrier_pokemon


_TYPES = ['GRASS', 'FIRE', 'WATER', 'LIGHTNING', 'PSYCHIC', 'FIGHTING', 'DARKNESS', 'METAL', 'FAIRY', 'DRAGON']


class _Converted(Passive):
    def __init__(self, type_value):
        self.type_value = type_value

    def modify_weakness(self, calc, carrier):
        if calc.target is carrier_pokemon(carrier) and calc.weak_types:
            calc.weak_types = [self.type_value]


async def _conversion_3(ctx):
    """Choose a type; the Defending Pokemon's Weakness is now that type until
    the end of your next turn (the amount doesn't change)."""
    d = ctx.opponent_active()
    if d is None or ctx.effects_blocked(d):
        return
    pick = await ctx.choose("Conversion 3: new Weakness type", [t.title() for t in _TYPES])
    ctx.add_passive_through_own_next_turn(d, _Converted(getattr(PokemonTypes, _TYPES[pick]).value))


card = PokemonCardDef(
    guid="7f5f22ce-592c-5f45-b1fd-d18681eccc94",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Porygon.Name",
    display_name="Porygon",
    searchable_by=["Porygon", "Basic", "Porygon"],
    subtypes=["Basic"],
    collector_number=71,
    set_code="XY12",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=137,
    abilities=[
        Attack(
            title="Conversion 3",
            game_text="Choose Grass, Fire, Water, Lightning, Psychic, Fighting, Darkness, Metal, Fairy, or Dragon type. The Defending Pok\u00e9mon's Weakness is now that type until the end of your next turn. (The amount of Weakness doesn't change.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_conversion_3,
        ),
    ],
)