from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

from spirit.game.card_effects.sm8 import (
    intercept_gx,
    mirror_counter,
)

async def feint(ctx):
    """30. This attack's damage isn't affected by Resistance."""
    await ctx.deal_damage(ignore_resistance=True)

card = PokemonCardDef(
    guid="70124643-3b1e-540d-8ae0-cd1f0cffb92c",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SigilyphGX.Name",
    display_name="Sigilyph-GX",
    searchable_by=["Sigilyph-GX", "Basic", "GX", "SigilyphGX"],
    subtypes=["Basic", "GX"],
    collector_number=222,
    set_code="SM8",
    rarity=Rarities.RareRainbow,
    hp=170,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=561,
    abilities=[
        Ability(
            title="Mirror Counter",
            game_text="If this Pok\u00e9mon is your Active Pok\u00e9mon and is damaged by an attack from your opponent's Pok\u00e9mon-GX or Pok\u00e9mon-EX (even if this Pok\u00e9mon is Knocked Out), put damage counters on the Attacking Pok\u00e9mon equal to the damage done to this Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=mirror_counter,
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
        ),
        Attack(
            title="Sonic Wing",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=feint,
        ),
        Attack(
            title="Intercept-GX",
            game_text="This attack does 60 damage times the amount of Energy attached to your opponent's Active Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="x",
            effect=intercept_gx
        ),
    ],
)