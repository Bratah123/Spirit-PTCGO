"""STUB: effect not implemented — do not guess mechanics.
Blaziken ex (EX4 #89): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.ex import hypno_wave, volcanic_ash

card = PokemonCardDef(
    guid="4cd5e3be-d712-5687-b53f-9d3447f39951",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Blazikenex.Name",
    display_name="Blaziken ex",
    searchable_by=["Blaziken ex", "Stage 2", "ex", "Blazikenex"],
    subtypes=["Stage 2", "ex"],
    collector_number=89,
    set_code="EX4",
    rarity=Rarities.RareHoloEX,
    hp=150,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Combusken.Name",
    family_id=257,
    abilities=[
        Attack(
            title="Blaze Kick",
            game_text="Flip a coin. If heads, this attack does 30 damage plus 20 more damage. If tails, this attack does 30 damage and the Defending Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=hypno_wave(20, SpecialConditions.BURNED),
        ),
        Attack(
            title="Volcanic Ash",
            game_text="Discard 2 Fire Energy attached to Blaziken ex and then choose 1 of your opponent's Pok\u00e9mon. This attack does 100 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            # STUB: attack effect not implemented
            effect=volcanic_ash(),
        ),
    ],
)