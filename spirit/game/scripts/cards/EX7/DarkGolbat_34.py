from spirit.game.card_effects.ex import night_ambush
"""STUB: effect not implemented — do not guess mechanics.
Dark Golbat (EX7 #34): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a49a654e-c27c-55eb-99e3-c5f805780ed2",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkGolbat.Name",
    display_name="Dark Golbat",
    searchable_by=["Dark Golbat", "Stage 1", "DarkGolbat"],
    subtypes=["Stage 1"],
    collector_number=34,
    set_code="EX7",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.GRASS, PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Zubat.Name",
    family_id=41,
    abilities=[
        Attack(
            title="Night Ambush",
            game_text="Does 30 damage to 1 of your opponent's Pok\u00e9mon. Dark Golbat can't attack during your next turn. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.GRASS: 1},
            # STUB: attack effect not implemented
            effect=night_ambush(),
        ),
    ],
)