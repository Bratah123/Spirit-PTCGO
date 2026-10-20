"""STUB: effect not implemented — do not guess mechanics.
Haunter (XY8 #59): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6d1afc96-49a5-5d18-bdef-4559b8c02305",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Haunter.Name",
    display_name="Haunter",
    searchable_by=["Haunter", "Stage 1", "Haunter"],
    subtypes=["Stage 1"],
    collector_number=59,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gastly.Name",
    family_id=92,
    abilities=[
        Ability(
            title="Gothic Fear",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon, you may leave both Active Pok\u00e9mon Confused.",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Poison Ring",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned. That Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)