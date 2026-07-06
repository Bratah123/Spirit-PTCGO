from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4e2fa8bc-a6dc-5b4c-afe3-a14b191d970c",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Toxapex.Name",
    display_name="Toxapex",
    searchable_by=["Toxapex", "Stage 1", "Toxapex"],
    subtypes=["Stage 1"],
    collector_number=52,
    set_code="SWSH3",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Mareanie.Name",
    family_id=747,
    abilities=[
        Attack(
            title="Recover",
            game_text="Discard an Energy from this Pok\u00e9mon and heal all damage from it.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Poisonous Whip",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=unimplemented,
        ),
    ],
)