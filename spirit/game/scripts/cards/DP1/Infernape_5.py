"""STUB: effect not implemented — do not guess mechanics.
Infernape (DP1 #5): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import spiral_rush
from spirit.game.card_effects.dp import flare_blitz_all_fire


card = PokemonCardDef(
    guid="02d25ae6-ac4e-5120-a5f9-cb58c37f59b2",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Infernape.Name",
    display_name="Infernape",
    searchable_by=["Infernape", "Stage 2", "Infernape"],
    subtypes=["Stage 2"],
    collector_number=5,
    set_code="DP1",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Monferno.Name",
    family_id=390,
    abilities=[
        Attack(
            title="Meteor Punch",
            game_text="Flip a coin until you get tails. This attack does 30 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="x",
            effect=spiral_rush(),
        ),
        Attack(
            title="Flare Blitz",
            game_text="Discard all Fire Energy attached to Infernape.",
            cost={PokemonTypes.FIRE: 2},
            damage=90,
            effect=flare_blitz_all_fire(),
        ),
    ],
)