from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import unused_energy_bonus


card = PokemonCardDef(
    guid="7338511b-5a91-5b85-bd83-65ebf408883c",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Totodile.Name",
    display_name="Totodile",
    searchable_by=["Totodile", "Basic", "Totodile"],
    subtypes=["Basic"],
    collector_number=85,
    set_code="NEO4",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=158,
    abilities=[
        Attack(
            title="Water Gun",
            game_text="Does 10 damage plus 10 more damage for each Water Energy attached to Totodile but not used to pay for this attack's Energy cost. You can't add more than 20 damage in this way.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            damage_operator="+",
            effect=unused_energy_bonus(10, 20, energy_type=PokemonTypes.WATER),
        ),
    ],
)
