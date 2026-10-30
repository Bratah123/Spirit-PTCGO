"""STUB: effect not implemented — do not guess mechanics.
Rayquaza ex (EX3 #97): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import spiral_growth, dragon_burst

card = PokemonCardDef(
    guid="22151d83-5406-504e-aa1c-b325bf3af9da",
    key="EX3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rayquazaex.Name",
    display_name="Rayquaza ex",
    searchable_by=["Rayquaza ex", "Basic", "ex", "Rayquazaex"],
    subtypes=["Basic", "ex"],
    collector_number=97,
    set_code="EX3",
    rarity=Rarities.RareHoloEX,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.COLORLESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=384,
    abilities=[
        Attack(
            title="Spiral Growth",
            game_text="Flip a coin until you get tails. For each heads, search your discard pile for a basic Energy card and attach it to Rayquaza ex.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=spiral_growth(),
        ),
        Attack(
            title="Dragon Burst",
            game_text="Discard either all Fire Energy or all Lightning Energy attached to Rayquaza ex. This attack does 40 damage times the amount of Fire or Lightning Energy discarded.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.LIGHTNING: 1},
            damage=40,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=dragon_burst(40),
        ),
    ],
)