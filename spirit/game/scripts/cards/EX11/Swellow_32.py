"""STUB: effect not implemented — do not guess mechanics.
Swellow (EX11 #32): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.ex import steep_dive
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7558e887-1477-5517-b0e9-6dd097cc68d4",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Swellow.Name",
    display_name="Swellow",
    searchable_by=["Swellow", "Stage 1", "Swellow"],
    subtypes=["Stage 1"],
    collector_number=32,
    set_code="EX11",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Taillow.Name",
    family_id=276,
    abilities=[
        Attack(
            title="Steep Dive",
            game_text="Flip a coin. If heads, prevent all effects of an attack, including damage, done to Swellow during your opponent's next turn. If tails, during your next turn, Swellow's Glide attack's base damage is 100.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=steep_dive(),
        ),
        Attack(
            title="Glide",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
        ),
    ],
)