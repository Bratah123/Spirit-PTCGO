"""STUB: effect not implemented — do not guess mechanics.
Jolteon ex (EX11 #109): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Ability, Attack, PokemonCardDef, Triggers, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import evolutionary_thunder_on_evolve, meditate_damage, second_bite


card = PokemonCardDef(
    guid="406ae801-126e-55ba-bb77-9581d11b5e6a",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jolteonex.Name",
    display_name="Jolteon ex",
    searchable_by=["Jolteon ex", "Stage 1", "ex", "Jolteonex"],
    subtypes=["Stage 1", "ex"],
    collector_number=109,
    set_code="EX11",
    rarity=Rarities.RareHoloEX,
    hp=100,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Ability(
            title="Evolutionary Thunder",
            game_text="Once during your turn, when you play Jolteon ex from your hand to evolve 1 of your Pok\u00e9mon, you may put 1 damage counter on each of your opponent's Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_POWER,
            trigger=Triggers.ON_EVOLVE,
            effect=evolutionary_thunder_on_evolve(1),
        ),
        Attack(
            title="Second Bite",
            game_text="Does 20 damage plus 10 more damage for each damage counter on the Defending Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=meditate_damage(20, 10),
        ),
        Attack(
            title="Thunder Blast",
            game_text="Discard a Lightning Energy card attached to Jolteon ex.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=second_bite(20, 10),
        ),
    ],
)