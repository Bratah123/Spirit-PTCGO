from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import juxtapose


card = PokemonCardDef(
    guid="a5fb9a10-e503-500c-b81e-9d30000ed958",
    key="BP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RocketsMewtwo.Name",
    display_name="Rocket's Mewtwo",
    searchable_by=["Rocket's Mewtwo", "Basic", "RocketsMewtwo"],
    subtypes=["Basic"],
    collector_number=8,
    set_code="BP",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=150,
    abilities=[
        Attack(
            title="Juxtapose",
            game_text="Flip a coin. If heads, switch the number of damage counters on Rocket's Mewtwo with the number of damage counters on the Defending Pok\u00e9mon (even if it would Knock Out either Pok\u00e9mon). (It's okay if 1 of the Pok\u00e9mon has no damage counters on it.)",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=juxtapose,
        ),
        Attack(
            title="Hypnoblast",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=20,
            effect=condition_attack(SpecialConditions.ASLEEP, flip=True),
        ),
        Attack(
            title="Psyburn",
            cost={PokemonTypes.PSYCHIC: 3, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)
