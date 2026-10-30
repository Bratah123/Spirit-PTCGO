"""STUB: effect not implemented — do not guess mechanics.
Chimchar (DPP #DP02): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="bc60eb5f-a7f9-5c2f-bfc5-f74a5fa6afbb",
    key="DPP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chimchar.Name",
    display_name="Chimchar",
    searchable_by=["Chimchar", "Basic", "Chimchar"],
    subtypes=["Basic"],
    collector_number=2,
    set_code="DPP",
    rarity=Rarities.RarePromo,
    hp=50,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=390,
    abilities=[
        Attack(
            title="Scratch",
            cost={},
            damage=10,
        ),
        Attack(
            title="Ember",
            game_text="Flip a coin. If tails, discard a Fire Energy attached to Chimchar.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)