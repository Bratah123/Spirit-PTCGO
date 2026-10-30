"""STUB: effect not implemented — do not guess mechanics.
Jolteon ★ (EX16 #101): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers, unimplemented
from spirit.game.card_effects.ex import agility_flip_protect, yellow_ray_on_bench
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="2a6c09e0-6b16-5331-89a1-e41786cecb33",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jolteon.Name",
    display_name="Jolteon ★",
    searchable_by=["Jolteon \u2605", "Basic", "Star", "Jolteon"],
    subtypes=["Basic", "Star"],
    collector_number=101,
    set_code="EX16",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    family_id=135,
    abilities=[
        Ability(
            title="Yellow Ray",
            game_text="Once during your turn, when you put Jolteon Star from your hand onto your Bench, you may put 1 damage counter on each Active Pok\u00e9mon (both yours and your opponent's).",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=yellow_ray_on_bench(),
            trigger=Triggers.ON_PLAY,
        ),
        Attack(
            title="Agility",
            game_text="Flip a coin. If heads, prevent all effects of an attack, including damage, done to Jolteon Star during your opponent's next turn.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
            # STUB: attack effect not implemented
            effect=agility_flip_protect(),
        ),
    ],
)