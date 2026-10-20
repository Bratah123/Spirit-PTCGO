from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import (
    condition_attack, damage_per, count_energy,
)

card = PokemonCardDef(
    guid="08c6a493-931a-57d1-b60a-c0c2042e555c",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Alomomola.Name",
    display_name="Alomomola",
    searchable_by=["Alomomola", "Basic", "Alomomola"],
    subtypes=["Basic"],
    collector_number=39,
    set_code="BW1",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=594,
    abilities=[
        Attack(
            title="Water Pulse",
            game_text="The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
        Attack(
            title="Hydro Pump",
            game_text="Does 10 more damage for each Water Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            damage_operator="+",
            effect=damage_per(
                count_energy("self", energy_type=PokemonTypes.WATER), 10, base=40
            ),
        ),
    ],
)
