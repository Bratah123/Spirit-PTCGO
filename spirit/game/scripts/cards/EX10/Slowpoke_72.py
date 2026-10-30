"""STUB: effect not implemented — do not guess mechanics.
Slowpoke (EX10 #72): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import fishing_tail
from spirit.game.card_effects.attacks_common import flip_bonus


card = PokemonCardDef(
    guid="3bc056d6-7380-5d25-9f83-4ad81fd3df9f",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name",
    display_name="Slowpoke",
    searchable_by=["Slowpoke", "Basic", "Slowpoke"],
    subtypes=["Basic"],
    collector_number=72,
    set_code="EX10",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=79,
    abilities=[
        Attack(
            title="Fishing Tail",
            game_text="Search your discard pile for a Basic Pok\u00e9mon, Evolution card, or basic Energy card, show it to your opponent, and put it into your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=fishing_tail(),
        ),
        Attack(
            title="Trip Over",
            game_text="Flip a coin. If heads, this attack does 20 damage plus 10 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=flip_bonus(10),
        ),
    ],
)