"""STUB: effect not implemented — do not guess mechanics.
Florges (XY8 #103): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="287a701b-8d36-53bf-a705-b7f8f060a745",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Florges.Name",
    display_name="Florges",
    searchable_by=["Florges", "Stage 2", "Florges"],
    subtypes=["Stage 2"],
    collector_number=103,
    set_code="XY8",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Floette.Name",
    family_id=669,
    abilities=[
        Ability(
            title="Calming Aroma",
            game_text="Each of your Pok\u00e9mon's attacks costs Fairy less.",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Wonder Shine",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.FAIRY: 3},
            damage=70,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)