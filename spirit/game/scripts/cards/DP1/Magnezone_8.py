"""STUB: effect not implemented — do not guess mechanics.
Magnezone (DP1 #8): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import metal_blast
from spirit.game.card_effects.dp import magnetize_passive, metal_blast

card = PokemonCardDef(
    guid="eee01583-530d-5049-a7ea-7247aa0c7d84",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magnezone.Name",
    display_name="Magnezone",
    searchable_by=["Magnezone", "Stage 2", "Magnezone"],
    subtypes=["Stage 2"],
    collector_number=8,
    set_code="DP1",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magneton.Name",
    family_id=81,
    abilities=[
        Ability(
            title="Magnetize",
            game_text="If you have any Metal Energy attached to your Active Pok\u00e9mon, the Retreat Cost for that Pok\u00e9mon is 0.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=magnetize_passive(),
        ),
        Attack(
            title="Metal Blast",
            game_text="Does 50 damage plus 10 more damage for each Metal Energy attached to Magnezone.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=metal_blast(),
        ),
    ],
)