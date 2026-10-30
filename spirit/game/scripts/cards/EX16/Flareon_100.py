"""STUB: effect not implemented — do not guess mechanics.
Flareon ★ (EX16 #100): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers, unimplemented
from spirit.game.card_effects.ex import crimson_ray_on_bench, flamethrower_discard_fire
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="cf063794-9356-5643-839d-7d071217dd36",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flareon.Name",
    display_name="Flareon ★",
    searchable_by=["Flareon \u2605", "Basic", "Star", "Flareon"],
    subtypes=["Basic", "Star"],
    collector_number=100,
    set_code="EX16",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=136,
    abilities=[
        Ability(
            title="Crimson Ray",
            game_text="Once during your turn, when you put Flareon Star from your hand onto your Bench, you may use this power. Each Active Pok\u00e9mon (both yours and your opponent's) is now Burned.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=crimson_ray_on_bench(),
            trigger=Triggers.ON_PLAY,
        ),
        Attack(
            title="Flamethrower",
            game_text="Discard a Fire Energy attached to Flareon Star.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            # STUB: attack effect not implemented
            effect=flamethrower_discard_fire(),
        ),
    ],
)