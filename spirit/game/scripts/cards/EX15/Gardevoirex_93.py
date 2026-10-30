"""STUB: effect not implemented — do not guess mechanics.
Gardevoir ex δ (EX15 #93): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.ex import flame_ball, imprison_marker
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="64f165ed-b132-5990-a63f-167768987ba9",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gardevoirex.Name",
    display_name="Gardevoir ex δ",
    searchable_by=["Gardevoir ex \u03b4", "Stage 2", "ex", "Gardevoirex"],
    subtypes=["Stage 2", "ex"],
    collector_number=93,
    set_code="EX15",
    rarity=Rarities.RareHoloEX,
    hp=150,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kirlia.Name",
    family_id=280,
    abilities=[
        Ability(
            title="Imprison",
            game_text="Once during your turn (before your attack), if Gardevoir ex is your Active Pok\u00e9mon, you may put an Imprison marker on 1 of your opponent's Pok\u00e9mon. Any Pok\u00e9mon that has any Imprison markers on it can't use any Pok\u00e9-Powers or Pok\u00e9-Bodies. This power can't be used if Gardevoir ex is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=imprison_marker(),
        ),
        Attack(
            title="Flame Ball",
            game_text="You may move a Fire Energy card attached to Gardevoir ex to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            # STUB: attack effect not implemented
            effect=flame_ball(),
        ),
    ],
)