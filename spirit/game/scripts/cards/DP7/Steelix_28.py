"""STUB: effect not implemented — do not guess mechanics.
Steelix (DP7 #28): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="784a9a0b-846d-5896-b778-c3bb460dca32",
    key="DP7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Steelix.Name",
    display_name="Steelix",
    searchable_by=["Steelix", "Stage 1", "Steelix"],
    subtypes=["Stage 1"],
    collector_number=28,
    set_code="DP7",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Onix.Name",
    family_id=95,
    abilities=[
        Attack(
            title="Outbreak Power",
            game_text="Choose a number of your opponent's Pok\u00e9mon up to the amount of Energy attached to Steelix. This attack does 20 damage to each of them. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Iron Tail",
            game_text="Flip a coin until you get tails. This attack does 100 damage times the number of heads.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 2},
            damage=100,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)