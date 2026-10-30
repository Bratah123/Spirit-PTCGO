"""STUB: effect not implemented — do not guess mechanics.
Swampert ex (EX4 #95): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import crushing_wave, extra_energy_damage

card = PokemonCardDef(
    guid="52669517-e280-58c5-b766-f243f7b6c806",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Swampertex.Name",
    display_name="Swampert ex",
    searchable_by=["Swampert ex", "Stage 2", "ex", "Swampertex"],
    subtypes=["Stage 2", "ex"],
    collector_number=95,
    set_code="EX4",
    rarity=Rarities.RareHoloEX,
    hp=150,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Marshtomp.Name",
    family_id=260,
    abilities=[
        Attack(
            title="Hyper Pump",
            game_text="Does 20 damage plus 20 more damage for each basic Energy attached to Swampert ex but not used to pay for this attack's Energy cost. You can't add more than 80 damage in this way.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=extra_energy_damage(20, base=20, energy_type=PokemonTypes.WATER),
        ),
        Attack(
            title="Crushing Wave",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 40 damage to that Pok\u00e9mon. After doing damage, flip a coin. If heads, your opponent discards an Energy card, if any, attached to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            # STUB: attack effect not implemented
            effect=crushing_wave(),
        ),
    ],
)