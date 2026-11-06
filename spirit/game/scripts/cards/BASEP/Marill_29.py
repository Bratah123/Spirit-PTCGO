from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import unused_energy_bonus


card = PokemonCardDef(
    guid="65cc1add-2e0f-5d0e-9655-7b32a73cfb63",
    key="BASEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Marill.Name",
    display_name="Marill",
    searchable_by=["Marill", "Basic", "Marill"],
    subtypes=["Basic"],
    collector_number=29,
    set_code="BASEP",
    rarity=Rarities.RarePromo,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=183,
    abilities=[
        Attack(
            title="Water Gun",
            game_text="Does 20 damage plus 10 more damage for each Energy attached to Marill but not used to pay for this attack's Energy cost. You can't add more than 20 damage in this way.",
            cost={PokemonTypes.WATER: 2},
            damage=20,
            damage_operator="+",
            effect=unused_energy_bonus(10, 20),
        ),
    ],
)
