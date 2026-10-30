from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import lightning_cut, unused_energy_bonus


card = PokemonCardDef(
    guid="5bb03942-cef5-5f7d-b9c2-6b131073414c",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ShiningKabutops.Name",
    display_name="Shining Kabutops",
    searchable_by=["Shining Kabutops", "Basic", "ShiningKabutops"],
    subtypes=["Basic"],
    collector_number=108,
    set_code="NEO4",
    rarity=Rarities.Shining,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=141,
    abilities=[
        Attack(
            title="Lightning Cut",
            game_text="Flip a coin. If heads, this attack does 30 damage plus 10 more damage and does 10 damage to each of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) If tails, this attack does 30 damage and Shining Kabutops does 10 damage to itself.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.LIGHTNING: 1},
            damage=30,
            damage_operator="+",
            effect=lightning_cut,
        ),
        Attack(
            title="Water Slash",
            game_text="Does 50 damage plus 10 more damage for each Water Energy attached to Shining Kabutops but not used to pay for this attack's Energy cost. Don't apply Resistance.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.WATER: 2},
            damage=50,
            damage_operator="+",
            effect=unused_energy_bonus(
                10, energy_type=PokemonTypes.WATER, ignore_resistance=True),
        ),
    ],
)
