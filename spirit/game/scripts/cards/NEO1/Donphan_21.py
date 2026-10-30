from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_counters_on, damage_per
from spirit.game.card_effects.ecard import rapid_spin


card = PokemonCardDef(
    guid="f82ffe30-fdbf-5f81-bb7a-7f2ca1dad025",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Donphan.Name",
    display_name="Donphan",
    searchable_by=["Donphan", "Stage 1", "Donphan"],
    subtypes=["Stage 1"],
    collector_number=21,
    set_code="NEO1",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Phanpy.Name",
    family_id=231,
    abilities=[
        Attack(
            title="Flail",
            game_text="Does 10 damage times the number of damage counters on Donphan.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
            damage_operator="x",
            effect=damage_per(damage_counters_on("self"), 10),
        ),
        Attack(
            title="Rapid Spin",
            game_text="If your opponent has any Benched Pok\u00e9mon, he or she chooses 1 of them and switches it with his or her Active Pok\u00e9mon, then, if you have any Benched Pok\u00e9mon, you switch 1 of them with your Active Pok\u00e9mon. (Do the damage before switching the Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 3},
            damage=50,
            effect=rapid_spin,
        ),
    ],
)
