"""STUB: effect not implemented — do not guess mechanics.
Typhlosion ex (EX10 #110): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Triggers, PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import bursting_up_on_evolve, kindle_discard_both

card = PokemonCardDef(
    guid="19c55d76-8a78-5405-aecb-cb32c97f75a0",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Typhlosionex.Name",
    display_name="Typhlosion ex",
    searchable_by=["Typhlosion ex", "Stage 2", "ex", "Typhlosionex"],
    subtypes=["Stage 2", "ex"],
    collector_number=110,
    set_code="EX10",
    rarity=Rarities.RareHoloEX,
    hp=150,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Quilava.Name",
    family_id=155,
    abilities=[
        Ability(
            title="Bursting Up",
            game_text="Once during your turn when you play Typhlosion ex from your hand to evolve 1 of your Pok\u00e9mon, count the number of your opponent's Benched Pok\u00e9mon. You may search your deck for up to that number of Fire Energy cards and attach them to 1 of your Fire Pok\u00e9mon. Shuffle your deck afterward.",
            ability_type=AbilityTypes.POKE_POWER,
            trigger=Triggers.ON_EVOLVE,
            # STUB: ability effect not implemented
            effect=bursting_up_on_evolve(),
        ),
        Attack(
            title="Kindle",
            game_text="Discard an Energy card attached to Typhlosion ex and then discard an Energy card attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            # STUB: attack effect not implemented
            effect=kindle_discard_both(),
        ),
    ],
)