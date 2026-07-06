from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6cbb866b-c7db-52cf-a07c-eebaebb46086",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.StonjournerVMAX.Name",
    display_name="Stonjourner VMAX",
    searchable_by=["Stonjourner VMAX", "VMAX", "StonjournerVMAX"],
    subtypes=["VMAX"],
    collector_number=116,
    set_code="SWSH1",
    rarity=Rarities.RareHoloVMAX,
    hp=330,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.VMAX,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.StonjournerV.Name",
    family_id=874,
    abilities=[
        Attack(
            title="Stone Gift",
            game_text="Attach a Fighting Energy card from your hand to 1 of your Pok\u00e9mon. If you do, heal 120 damage from that Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Max Rockfall",
            cost={PokemonTypes.FIGHTING: 3},
            damage=200,
        ),
    ],
)