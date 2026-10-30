"""STUB: effect not implemented — do not guess mechanics.
Staraptor (DP1 #16): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import accelerative_dive
from spirit.game.card_effects.dp import brave_heart

card = PokemonCardDef(
    guid="80d7c6ea-d810-549a-98cc-ec6d7a5e5672",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Staraptor.Name",
    display_name="Staraptor",
    searchable_by=["Staraptor", "Stage 2", "Staraptor"],
    subtypes=["Stage 2"],
    collector_number=16,
    set_code="DP1",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Staravia.Name",
    family_id=396,
    abilities=[
        Attack(
            title="Accelerative Dive",
            game_text="Flip a coin. If tails, this attack does nothing. If heads, prevent all damage done to Staraptor by attacks (both yours and your opponent's) until the end of your next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=accelerative_dive(),
        ),
        Attack(
            title="Brave Heart",
            game_text="Flip a coin. If tails, Staraptor does 100 damage to itself.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=100,
            effect=brave_heart(100),
        ),
    ],
)