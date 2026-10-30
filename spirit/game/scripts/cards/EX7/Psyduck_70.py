from spirit.game.card_effects.ex import headache_lock_trainers
"""STUB: effect not implemented — do not guess mechanics.
Psyduck (EX7 #70): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f17f9b9a-0d1e-5d03-b832-32459dc94f01",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Psyduck.Name",
    display_name="Psyduck",
    searchable_by=["Psyduck", "Basic", "Psyduck"],
    subtypes=["Basic"],
    collector_number=70,
    set_code="EX7",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=54,
    abilities=[
        Attack(
            title="Gentle Slap",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Headache",
            game_text="Flip a coin. If heads, your opponent can't play a Trainer card from his or her hand until the end of your opponent's next turn.",
            cost={PokemonTypes.WATER: 1},
            # STUB: attack effect not implemented
            effect=headache_lock_trainers(),
        ),
    ],
)