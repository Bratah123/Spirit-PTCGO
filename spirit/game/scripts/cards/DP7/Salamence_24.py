"""STUB: effect not implemented — do not guess mechanics.
Salamence (DP7 #24): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="2af9361d-c877-5b78-8842-eb7f07e5d5d2",
    key="DP7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Salamence.Name",
    display_name="Salamence",
    searchable_by=["Salamence", "Stage 2", "Salamence"],
    subtypes=["Stage 2"],
    collector_number=24,
    set_code="DP7",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.COLORLESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shelgon.Name",
    family_id=371,
    abilities=[
        Ability(
            title="Battle Rush",
            game_text="If your opponent has any Pok\u00e9mon in play that has maximum HP of 120 or more, ignore all Colorless Energy necessary to use Salamence's attacks.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Combustion",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
        Attack(
            title="Steam Twister",
            game_text="Discard a Fire Energy and a Water Energy attached to Salamence.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)