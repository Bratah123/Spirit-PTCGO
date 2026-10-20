"""STUB: effect not implemented — do not guess mechanics.
Mothim (XY10 #4): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="364d0364-661b-56cd-b813-732258b681f4",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mothim.Name",
    display_name="Mothim",
    searchable_by=["Mothim", "Stage 1", "Mothim"],
    subtypes=["Stage 1"],
    collector_number=4,
    set_code="XY10",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Burmy.Name",
    family_id=412,
    abilities=[
        Ability(
            title="Wormadam First",
            game_text="As often as you like during your turn (before your attack), you may move 1 damage counter from 1 of your Wormadam to another of your Pok\u00e9mon.",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Gust",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
        ),
    ],
)