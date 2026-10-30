from spirit.game.card_effects.ex import darkness_switch
"""STUB: effect not implemented — do not guess mechanics.
Rocket's Mewtwo ex (EX7 #99): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="4cbb18b0-4058-57ca-9c3d-e0ffc8874e03",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RocketsMewtwoex.Name",
    display_name="Rocket's Mewtwo ex",
    searchable_by=["Rocket's Mewtwo ex", "Basic", "ex", "RocketsMewtwoex"],
    subtypes=["Basic", "ex"],
    collector_number=99,
    set_code="EX7",
    rarity=Rarities.RareHoloEX,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=150,
    abilities=[
        Attack(
            title="Darkness Switch",
            game_text="Discard an Energy card attached to Rocket's Mewtwo ex, and then switch all damage counters on Rocket's Mewtwo ex with those on the Defending Pok\u00e9mon. (If an effect of this attack is prevented, this attack does nothing.)",
            cost={PokemonTypes.PSYCHIC: 1},
            # STUB: attack effect not implemented
            effect=darkness_switch(),
        ),
        Attack(
            title="Hypnoblast",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.ASLEEP, flip=True),
        ),
        Attack(
            title="Psyburn",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 3},
            damage=70,
        ),
    ],
)