from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import hyper_pump, salt_water

card = PokemonCardDef(
    guid="c86b12f6-a91d-52f0-8f73-37b4f95bec54",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kingler.Name",
    display_name="Kingler",
    searchable_by=["Kingler", "Stage 1", "Kingler"],
    subtypes=["Stage 1"],
    collector_number=26,
    set_code="EX6",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Krabby.Name",
    family_id=98,
    abilities=[
        Attack(
            title="Salt Water",
            game_text="Search your deck for up to 2 Water Energy cards and attach them to Kingler. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=salt_water(),
        ),
        Attack(
            title="Hyper Pump",
            game_text="Does 30 damage plus 20 more damage for each basic Energy attached to Kingler but not used to pay for this attack's Energy cost. You can't add more than 40 damage in this way.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=hyper_pump(30, 20),
        ),
    ],
)