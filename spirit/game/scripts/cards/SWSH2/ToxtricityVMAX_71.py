from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8c646f71-da3c-5c18-892d-ca0b2adeff10",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ToxtricityVMAX.Name",
    display_name="Toxtricity VMAX",
    searchable_by=["Toxtricity VMAX", "VMAX", "ToxtricityVMAX"],
    subtypes=["VMAX"],
    collector_number=71,
    set_code="SWSH2",
    rarity=Rarities.RareHoloVMAX,
    hp=320,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.VMAX,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.ToxtricityV.Name",
    family_id=849,
    abilities=[
        Attack(
            title="G-Max Riot",
            game_text="If your opponent's Active Pok\u00e9mon is Poisoned, this attack does 80 more damage.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)