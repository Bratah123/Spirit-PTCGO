from spirit.game.card_effects.ex import black_suction_cups, ink_blast
"""STUB: effect not implemented — do not guess mechanics.
Dark Octillery (EX7 #8): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1ef27a67-fdab-5fe9-a583-ae084eb2e126",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkOctillery.Name",
    display_name="Dark Octillery",
    searchable_by=["Dark Octillery", "Stage 1", "DarkOctillery"],
    subtypes=["Stage 1"],
    collector_number=8,
    set_code="EX7",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.WATER, PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Remoraid.Name",
    family_id=223,
    abilities=[
        Attack(
            title="Black Suction Cups",
            game_text="Does 10 damage to each Defending Pok\u00e9mon. Flip a coin. If heads, each Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.WATER: 1},
            # STUB: attack effect not implemented
            effect=black_suction_cups(),
        ),
        Attack(
            title="Ink Blast",
            game_text="Does 30 damage plus 10 more damage for each Energy attached to Dark Octillery but not used to pay for this attack's Energy cost. You can't add more than 20 damage in this way.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=ink_blast(),
        ),
    ],
)