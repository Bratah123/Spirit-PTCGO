from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, damage_counters_on, self_energy_discard_attack


card = PokemonCardDef(
    guid="1e82c884-6033-5141-a9b6-c6cd8999cf1f",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.KyuremEX.Name",
    display_name="Kyurem-EX",
    searchable_by=["Kyurem-EX", "Basic", "EX", "KyuremEX"],
    subtypes=["Basic", "EX"],
    collector_number=30,
    set_code="BW10",
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    family_id=646,
    abilities=[
        Attack(
            title="Outrage",
            game_text="Does 10 more damage for each damage counter on this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=damage_per(damage_counters_on('self'), 10, base=30),
        ),
        Attack(
            title="Giga Frost",
            game_text="Discard 2 Water Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=150,
            effect=self_energy_discard_attack(count=2, energy_type=PokemonTypes.WATER),
        ),
    ],
)