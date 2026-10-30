from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, unimplemented
from spirit.game.attributes import AbilityTypes, PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.ex import crush_and_burn, extra_energy_bomb, poke_power_condition

card = PokemonCardDef(
    guid="606e6205-9bb1-5875-92d3-2b83e7837d44",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Electrodeex.Name",
    display_name="Electrode ex",
    searchable_by=["Electrode ex", "Stage 1", "ex", "Electrodeex"],
    subtypes=["Stage 1", "ex"],
    collector_number=107,
    set_code="EX6",
    rarity=Rarities.RareHoloEX,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Voltorb.Name",
    family_id=100,
    abilities=[
        Ability(
            title="Extra Energy Bomb",
            game_text="Once during your turn (before your attack), you may discard Electrode ex and all the cards attached to it (this counts as Knocking Out Electrode ex). If you do, search your discard pile for 5 Energy cards and attach them to any of your Pok\u00e9mon (excluding Pok\u00e9mon-ex) in any way you like. This power can't be used if Electrode ex is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=poke_power_condition(),
            effect=extra_energy_bomb(),
        ),
        Attack(
            title="Crush and Burn",
            game_text="You may discard as many Energy as you like attached to your Pok\u00e9mon in play. If you do, this attack does 30 damage plus 20 more damage for each Energy you discarded.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=crush_and_burn(30, 20),
        ),
    ],
)