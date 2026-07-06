from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b99dc7d4-f6ac-53b0-be4b-7ae2d8fd8b99",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianBasculegion.Name",
    display_name="Hisuian Basculegion",
    searchable_by=["Hisuian Basculegion", "Stage 1", "HisuianBasculegion"],
    subtypes=["Stage 1"],
    collector_number=45,
    set_code="SWSH11",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianBasculin.Name",
    family_id=550,
    abilities=[
        Attack(
            title="Upstream Spirits",
            game_text="This attack does 20 damage for each basic Energy card in your discard pile. Then, shuffle those cards into your deck.",
            cost={},
            damage=20,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Water Shot",
            game_text="Discard an Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1},
            damage=70,
            effect=unimplemented,
        ),
    ],
)