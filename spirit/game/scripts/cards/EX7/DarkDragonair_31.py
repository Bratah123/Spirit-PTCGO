from spirit.game.card_effects.ex import evolutionary_light
"""STUB: effect not implemented — do not guess mechanics.
Dark Dragonair (EX7 #31): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="f435bcaa-9911-5673-877c-0f8dbdb12bfd",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkDragonair.Name",
    display_name="Dark Dragonair",
    searchable_by=["Dark Dragonair", "Stage 1", "DarkDragonair"],
    subtypes=["Stage 1"],
    collector_number=31,
    set_code="EX7",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.COLORLESS,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dratini.Name",
    family_id=147,
    abilities=[
        Ability(
            title="Evolutionary Light",
            game_text="Once during your turn (before your attack), if Dark Dragonair is your Active Pok\u00e9mon, you may search your deck for an Evolution card. Show it to your opponent and put it into your hand. Shuffle your deck afterward. This power can't be used if Dark Dragonair is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=evolutionary_light(),
        ),
        Attack(
            title="Dragon Rage",
            cost={PokemonTypes.WATER: 1, PokemonTypes.LIGHTNING: 1},
            damage=30,
        ),
    ],
)