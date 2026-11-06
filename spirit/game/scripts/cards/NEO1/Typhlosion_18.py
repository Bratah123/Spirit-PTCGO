from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import self_energy_discard_attack, spread_damage
from spirit.game.card_effects.ecard import fire_boost, has_typed_basic_energy


card = PokemonCardDef(
    guid="7c2092d5-71f9-520d-a788-e442ef2702da",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Typhlosion.Name",
    display_name="Typhlosion",
    searchable_by=["Typhlosion", "Stage 2", "Typhlosion"],
    subtypes=["Stage 2"],
    collector_number=18,
    set_code="NEO1",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Quilava.Name",
    family_id=155,
    abilities=[
        Ability(
            title="Fire Boost",
            game_text="When you play Typhlosion from your hand, you may flip a coin. If heads, search your deck for up to 4 Fire Energy cards and attach them to Typhlosion. Shuffle your deck afterward.",
            ability_type=AbilityTypes.POKE_POWER,
            trigger=Triggers.ON_EVOLVE,
            effect=fire_boost,
        ),
        Attack(
            title="Flame Wheel",
            game_text="Discard 3 Fire Energy cards attached to Typhlosion in order to use this attack. Do 20 damage to each Benched Pok\u00e9mon (yours and your opponent's). (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIRE: 4},
            damage=80,
            condition=has_typed_basic_energy(PokemonTypes.FIRE, 3),
            effect=self_energy_discard_attack(
                count=3, energy_type=PokemonTypes.FIRE, before_damage=True,
                also=spread_damage(20, side="both"),
            ),
        ),
    ],
)
